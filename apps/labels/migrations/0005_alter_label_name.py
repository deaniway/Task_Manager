# Generated by Django 5.0.6 on 2024-06-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0004_alter_label_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='name'),
        ),
    ]
