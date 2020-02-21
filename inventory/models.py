from django.db import models

class Item(models.Model):

    CHOICES = (
        ('General Medical Equipment and Supplies', 'General Medical Equipment and Supplies'),
        ('Anaesthesiology', 'Anaesthesiology'),
        ('Apparel', 'Apparel'),
        ('Cardiology', 'Cardiology'),
        ('Dental equipment and supplies', 'Dental equipment and supplies'),
        ('Gynecology & Urology', 'Gynecology & Urology'),
        ('Laboratory', 'Laboratory'),
        ('Nephrology', 'Nephrology'),
        ('Neurology', 'Neurology'),
        ('Obstetrics and Maternity Care', 'Obstetrics and Maternity Care'),
        ('Ophthalmology and Optometry', 'Ophthalmology and Optometry'),
        ('Otology and Neurotology', 'Otology and Neurotology'),
        ('Physical and Occupational Therapy', 'Physical and Occupational Therapy'),
        ('Radiology', 'Radiology'),
        ('Sterilization', 'Sterilization'),
        ('Surgery', 'Surgery')
    )

    name = models.CharField(max_length=200, null=True, unique=True)
    quantity = models.IntegerField()
    category = models.CharField(max_length=200, null=True, choices=CHOICES)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    