# Generated by Django 5.0.7 on 2024-08-08 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_remove_classroom_class_teacher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='class_name',
        ),
    ]
