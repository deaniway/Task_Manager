# Generated by Django 5.0.6 on 2024-06-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0005_alter_status_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='name'),
        ),
    ]
