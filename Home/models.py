
from django.db import models
from django.contrib.auth.models import User



class Account_Details(models.Model):


    First_Name = models.CharField(max_length=30)
    Lasst_Name = models.CharField(max_length=30)
    Emails = models.CharField(max_length=50)
    Contact_No = models.IntegerField(12)
    Address = models.TextField()

    def _str_(self):
        return self.name

class Hermes(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name


class Zara(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name


class Chanel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name

class Kurtis(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name

class Hoodie(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name


class Lehanga(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name


class Night(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name


class Traditional(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name


class Western(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name


class Paulmi(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name


class Shirts(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()

    def _str_(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()




    def _str_(self):
        return self.name