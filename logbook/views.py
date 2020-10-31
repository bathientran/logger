from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .models import Day, Activity
from .forms import DayForm, ActivityForm
import arrow, datetime

#Shows activities for one day and allows adding new entries
def dayView(request, day_id):
    day = get_object_or_404(Day, id=day_id)
    if request.method == 'POST':
        p = request.POST.copy()
        form = ActivityForm(p)
        form.data["startTime"] = arrow.get(request.POST["startTime"],'YYYY-MM-DDTHH:mm').datetime
        form.data["endTime"] = arrow.get(request.POST["endTime"],'YYYY-MM-DDTHH:mm').datetime
        print(form.data)
        if form.is_valid():
            activity = Activity()
            activity.day = day
            activity.startTime = arrow.get(request.POST["startTime"],'YYYY-MM-DDTHH:mm').datetime
            print(type(activity.startTime))
            activity.endTime = arrow.get(request.POST["endTime"],'YYYY-MM-DDTHH:mm').datetime
            print(type(activity.endTime))
            activity.description = form.cleaned_data["description"]
            activity.category = form.cleaned_data["category"]
            activity.save()
            messages.success(request, ('Activity has been added!'))
            return render(request, 'logbook/day-detail.html', {'day': day})

        else:
            messages.error(request, ('Error: Try again.'))
            return render(request, 'logbook/day-detail.html', {'day': day})

    else:
        return render(request, 'logbook/day-detail.html', {'day': day})

def logbookView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)
        # create a form instance and populate it with data from the request:
        form = DayForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            formDate = request.POST.get('entryDate')
            entry = Day.objects.filter(entryDate = formDate)
            if entry.exists():
                messages.error(request, ('Error: Day already exists.'))
                all_days = Day.objects.order_by("id").all()
                return render(request, 'logbook/logbook-view.html', {'all_days': all_days})
            else:
                form.save()
                all_days = Day.objects.order_by("-entryDate").all()
                messages.success(request, ('Day has been added.'))
                return render(request, 'logbook/logbook-view.html', {'all_days': all_days})

        else:
            all_days = Day.objects.order_by("-entryDate").all()
            messages.error(request, ('Error: No date added.'))
            return render(request, 'logbook/logbook-view.html', {'all_days': all_days})

    # if a GET (or any other method) we'll create a blank form
    else:
        all_days = Day.objects.order_by("-entryDate").all()
        return render(request, 'logbook/logbook-view.html', {'all_days': all_days})

#deletes entries
def deleteActivity(request, activity_id):
    activity = Activity.objects.get(id = activity_id)
    day = activity.day
    activity.delete()
    messages.success(request, ('Activity has been deleted!'))
    return redirect('logbook:day-view', day.id)

#shows analytics
def analyticsView(request):
    categories = ["Sleep", "Academics", "Leisure", "Mental Health","Personal Development", "Professional Development", "Operational", "Excercise", "Health"]
    average_time = {"Sleep":0, "Academics":0, "Leisure":0, "Mental Health":0,"Personal Development":0, "Professional Development":0, "Operational":0, "Excercise":0, "Health":0}
    
    for category in categories:
        initial = datetime.timedelta(minutes=0)
        for timedelta in Activity.objects.filter(category=category):
            initial = initial + timedelta.get_duration()
        if Activity.objects.filter(category=category).count() > 0:
            average_time[category] = initial/Activity.objects.filter(category=category).count()
    
    return render(request, 'logbook/analytics.html', {'data': average_time, 'categories': categories})

