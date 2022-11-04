from django.db import models 

class CarProducer(models.Model):
    name = models.CharField("Назва", max_length=255)

class Auto(models.Model):
    model = models.CharField("Модель", max_length=255)
    producer = models.ForeignKey()
