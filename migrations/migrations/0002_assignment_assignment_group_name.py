# Generated by Django 3.1.1 on 2020-09-22 22:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='assignment_group_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
