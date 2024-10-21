from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_period = models.IntegerField() 
    course_description = models.TextField()
    course_code = models.PositiveSmallIntegerField()
    course_department = models.CharField(max_length=20)
    course_status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return self.course_name
     