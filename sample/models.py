from django.db import models

# Create your models here.
class Usb(models.Model):
    usb_serial_number = models.CharField(max_length=50)
    def __str__(self):
        return self.usb_serial_number
