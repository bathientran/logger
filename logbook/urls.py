from django.urls import path

from . import views

app_name = 'logbook'
urlpatterns = [
    path('', views.logbookView, name='home'),
    path('<int:day_id>/', views.dayView, name='day-view'),
    path('delete/<int:activity_id>/', views.deleteActivity, name='delete-activity'),
    path('analytics/', views.analyticsView, name='analytics'),
]