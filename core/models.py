from django.db import models


# Create your models here.


class Profession(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class DataSheet(models.Model):
    description = models.CharField(max_length=50)
    historical_data = models.TextField()

    def __str__(self):
        return self.description


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    professions = models.ManyToManyField(Profession)
    data_sheet = models.OneToOneField(DataSheet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Document(models.Model):

    PP = 'PP'
    ID = 'ID'
    OT = 'OTHER_DOC'

    DOC_TYPES = (
        (PP, 'Passport'),
        (ID, 'Identity card'),
        (OT, 'Other document')
    )

    doc_type = models.CharField(choices=DOC_TYPES, max_length=2)
    doc_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - n: {}".format(self.doc_type, self.doc_number)
