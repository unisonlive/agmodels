# Generated by Django 3.1.2 on 2020-12-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20201214_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_extra_credit',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]