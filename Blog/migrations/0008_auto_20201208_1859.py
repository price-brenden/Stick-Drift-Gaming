# Generated by Django 3.1.1 on 2020-12-08 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20201208_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created',
            field=models.DateField(default=datetime.date.today, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, verbose_name='Draft/Publish'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated',
            field=models.DateField(blank=True, null=True, verbose_name='Date Updated'),
        ),
    ]