# Generated by Django 4.0.1 on 2022-06-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(),
        ),
    ]