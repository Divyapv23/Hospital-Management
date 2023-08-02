from django.db import models

# Create your models here.

from django.db import models
from django.core.exceptions import ValidationError
from datetime import date,time
import phonenumbers


def validate_future_date(value):
    if value < date.today():
        raise ValidationError("Date must be in the future.")

def validate_phone_number(value):
    try:
        parsed_number = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError('Invalid phone number.')
    except phonenumbers.NumberParseException:
        raise ValidationError('Invalid phone number.')

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date_field = models.DateField(validators=[validate_future_date])
    choose_doctor = models.CharField(max_length=100)
    choose_department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email_id = models.EmailField()
    time_slot = models.TimeField()

    def clean(self):

        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)



class logindb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    mail=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
