# Generated by Django 4.2.1 on 2023-08-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0004_logindb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
