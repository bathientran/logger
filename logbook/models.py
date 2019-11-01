from django.db import models

# Create your models here.

class Day(models.Model):
    entryDate = models.DateField('Date of Day')

class Activity(models.Model):
    CATEGORY_CHOICES = (
        ('Sleep','SLEEP'),
        ('Academics','ACADEMICS'),
        ('Leisure','LEISURE'),
        ('Mental Health','MENTAL HEALTH'),
        ('Personal Development', 'PERSONAL DEVELOPMENT'),
        ('Professional Development', 'PROFESSIONAL DEVELOPMENT'),
        ('Operational', 'OPERATIONAL'),
        ('Excercise', 'EXCERCISE'),
        ('Health', 'HEALTH')
    )

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.description

    def get_duration(self):
        return self.endTime - self.startTime
 