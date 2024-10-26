from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=25)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.street}, {self.number}, {self.city}, {self.state}"
    