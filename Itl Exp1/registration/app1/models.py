from django.db import models

class PartyDetails(models.Model):
    first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField()
    # party_date = models.DateField()
    # suppliers_date = models.DateField()
    guest_count = models.IntegerField()
    # party_type = models.CharField(max_length=100)
    budget = models.IntegerField()
    # theme = models.CharField(max_length=100)
    # additional_info = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 100)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name



# Create your models here.
