from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()

class Brands(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()

class Contacts(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()

class BrandsLogo(models.Model):
    firstImage = models.ImageField()
    secondImage = models.ImageField()
    thirdImage = models.ImageField()
    fourthImage = models.ImageField()

class Category(models.Model):
    name = models.CharField(max_length=250)


class Cloth(models.Model):
    gender_choices = [
        ('М','Мужской'),
        ('Ж',':Женский'),
    ]
    gender = models.CharField(
        max_length=1,
        choices= gender_choices,
        default='М'
    )
    color = models.CharField(max_length=250)
    size_choices = [
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL')
    ]
    size = models.CharField(max_length=2,
    choices=size_choices,
    default='S'
    )
    price_manufacturer = models.FloatField()
    price = models.FloatField()
    categoryObject = models.ForeignKey(Category, on_delete=models.CASCADE)
    mainImage = models.ImageField()

class ItemImages(models.Model):
    image = models.ImageField()
    gender_choices = [
        ('М','Мужской'),
        ('Ж',':Женский'),
    ]
    gender = models.CharField(
        max_length=1,
        choices= gender_choices,
        default='М'
    )
    clothObject = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    