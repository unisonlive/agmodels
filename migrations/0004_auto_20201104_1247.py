# Generated by Django 3.1.2 on 2020-11-04 12:47

from django.db import migrations, models
import django.db.models.deletion
from main.lms.agmodels.models import resource_filepath_function


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_testcase_rng_seed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_resources',
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=resource_filepath_function)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                           related_name='task_resources', to='main.task')),
                ('testcase_as_input',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='input_resources', to='main.testcase')),
                ('testcase_as_output',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='output_resources', to='main.testcase')),
            ],
        ),
    ]
