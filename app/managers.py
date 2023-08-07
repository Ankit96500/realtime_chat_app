from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class Custom_Manager(BaseUserManager):
    def create_user(self,password=None,**extra_fields):

        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        extra_fields.setdefault('is_online',False)
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self,password=None,**extra_fields):

        extra_fields.setdefault('is_staff',True)   
        extra_fields.setdefault('is_superuser',True)   
        extra_fields.setdefault('is_active',True)


        user = self.create_user(password,**extra_fields)
        user.save(using=self._db)
        
        return user

   