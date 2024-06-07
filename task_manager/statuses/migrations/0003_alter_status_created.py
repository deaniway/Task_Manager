# Generated by Django 5.0.6 on 2024-06-07 13:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_alter_status_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created'),
        ),
    ]