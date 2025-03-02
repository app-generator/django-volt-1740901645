# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=255, null=True, blank=True)
    price = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Category(models.Model):

    #__Category_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    icon = models.IntegerField(null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Subcategory(models.Model):

    #__Subcategory_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    icon = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    #__Subcategory_FIELDS__END

    class Meta:
        verbose_name        = _("Subcategory")
        verbose_name_plural = _("Subcategory")


class User(models.Model):

    #__User_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")



#__MODELS__END
