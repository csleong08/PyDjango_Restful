from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['email']) < 7:
            errors['email'] = "Email address should be at least 7 characters"
        return errors
    # def basic_validator(self, postData):
    #     errors = {}
    #     if len(postData['email']) < 7:
    #         errors.append("Email address should be at least 7 characters")
    #     return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()