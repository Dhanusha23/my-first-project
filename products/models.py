from django.db import models
from django.contrib.auth.models import User  # Import the User model



# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length= 255)
    price = models.FloatField()
    stock=models.IntegerField
    image =models.CharField(max_length=2500)

class Kids(models.Model):
    id = models.AutoField(primary_key=True)  # Add an AutoField as the primary key
    kname=models.CharField(max_length= 255)
    kprice = models.FloatField()
    kstock=models.IntegerField
    kimage =models.CharField(max_length=2500)

class Women(models.Model):
    id = models.AutoField(primary_key=True)
    wname=models.CharField(max_length=225)
    wprice=models.FloatField()
    wstock=models.IntegerField
    wimage=models.CharField(max_length=2500)

class Men(models.Model):
    id = models.AutoField(primary_key=True)
    mname=models.CharField(max_length=225)
    mprice=models.FloatField()
    mstock=models.IntegerField
    mimage=models.CharField(max_length=2500)

class Unisex(models.Model):
    id = models.AutoField(primary_key=True)
    uname=models.CharField(max_length=225)
    uprice=models.FloatField()
    ustock=models.IntegerField
    uimage=models.CharField(max_length=2500)


class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)  # Add a ForeignKey to User
    cname=models.CharField(max_length=225, default='default_cname')
    cprice=models.FloatField( default=0.0)
    cstock=models.IntegerField(default=0)
    cimage=models.CharField(max_length=225,default='default_image.jpg')

    ctotal=models.CharField(max_length=225)
    shp=models.CharField(max_length=225)
    tot=models.CharField(max_length=225)

        # Add the 'user' field with a default value of None
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        # Check if the 'user' field is not set (None) and set it to a default user
        if self.user is None:
            # You can set the default user based on your criteria here
            # For example, you can set it to the first active user in your User model
            default_user = User.objects.filter(is_active=True).first()
            self.user = default_user

        super().save(*args, **kwargs)

'''
    @classmethod
    def create_from_women(cls, women):
        cart = cls(cname=women.wname, cprice=women.wprice, cstock=women.wstock, cimage=women.wimage)
        cart.save()
        return cart

    @classmethod
    def create_from_men(cls, men):
        cart = cls(cname=men.mname, cprice=men.mprice, cstock=men.mstock, cimage=men.mimage)
        cart.save()
        return cart

    @classmethod
    def create_from_kids(cls, kids):
        cart = cls(cname=kids.kname, cprice=kids.kprice, cstock=kids.kstock, cimage=kids.kimage)
        cart.save()
        return cart
    
    @classmethod
    def create_from_unisex(cls, unisex):
        cart = cls(cname=unisex.uname, cprice=unisex.uprice, cstock=unisex.ustock, cimage=unisex.uimage)
        cart.save()
        return cart
    '''