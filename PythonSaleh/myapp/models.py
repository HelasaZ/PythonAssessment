from django.db import models

class Mcom(models.Model):
    guest_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    flat_booked = models.CharField(max_length=255)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    creation_log = models.DateTimeField()
    booking_value = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.guest_name
