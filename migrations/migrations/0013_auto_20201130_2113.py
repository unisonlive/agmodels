# Generated by Django 3.1.2 on 2020-11-30 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201130_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filenamematch',
            name='task_as_submission_filename',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submission_filenames', to='main.task'),
        ),
    ]
