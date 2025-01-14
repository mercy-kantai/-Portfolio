# Generated by Django 5.0.7 on 2024-08-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classperiod', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classperiod',
            name='classroom',
        ),
        migrations.AlterField(
            model_name='classperiod',
            name='day_of_week',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='classperiod',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='classperiod',
            name='start_time',
            field=models.TimeField(),
        ),
        migrations.AddField(
            model_name='classperiod',
            name='classroom',
            field=models.CharField(default='Lovelace', max_length=23),
            preserve_default=False,
        ),
    ]
