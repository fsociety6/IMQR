# Generated by Django 3.0.1 on 2020-01-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200115_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date_of_service',
            field=models.DateTimeField(auto_now=True),
        ),
    ]