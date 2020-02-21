from django.db import models

class Patient(models.Model):

    medicalId = models.CharField(max_length=200, null=True, unique=True)
    lastName = models.CharField(max_length=200, null=True)
    firstName = models.CharField(max_length=200, null=True)
    middleName = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipCode = models.CharField(max_length=10, null=True)
    phoneNumber = models.CharField(max_length=15, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.medicalId + ' - ' + self.lastName + ', ' + self.firstName + ' ' + self.middleName
