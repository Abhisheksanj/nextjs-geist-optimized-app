from django.db import models

class PhoneDirectoryEntry(models.Model):
    number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.number} - {self.name or 'Unknown'}"

class SimCardData(models.Model):
    number = models.CharField(max_length=20, unique=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    carrier_type = models.CharField(max_length=50, blank=True, null=True)  # prepaid/postpaid

    def __str__(self):
        return f"{self.number} - {self.provider or 'Unknown'}"

class LeakedIdentityData(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name or 'Unknown'} - {self.phone or 'No Phone'}"
