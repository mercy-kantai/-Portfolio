from django.db import models
from teacher.models import Teacher


# Create your models here.
class Classroom(models.Model):
        class_code = models.PositiveSmallIntegerField()
        class_speciality= models.TextField()
        enrollment_date= models.TimeField()
        max_students = models.PositiveSmallIntegerField()
        academic_year = models.PositiveSmallIntegerField()
        capacity = models.PositiveSmallIntegerField()
        start_date= models.PositiveSmallIntegerField()
        end_date= models.PositiveSmallIntegerField()
        teacher= models.ForeignKey(Teacher,on_delete=models.SET_NULL, null=True, related_name='teacher')


        def __str__(self):
            return f"{self.class_name} {self.class_code}"
