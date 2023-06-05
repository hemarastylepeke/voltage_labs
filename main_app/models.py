from django.db import models


# model for creating customer quote.
class Project(models.Model):
    email = models.EmailField(max_length=255)
    confirm_email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=255)
    business_address = models.CharField(max_length=255)
    project_description = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
