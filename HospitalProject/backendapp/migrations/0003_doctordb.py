# Generated by Django 4.2.1 on 2023-08-01 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0002_departmentdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctordb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Drname', models.CharField(blank=True, max_length=100, null=True)),
                ('Dept', models.CharField(blank=True, max_length=100, null=True)),
                ('Drimage', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('Qul', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
