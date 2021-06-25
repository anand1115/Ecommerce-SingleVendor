from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import MyUserManager


class User(AbstractBaseUser,PermissionsMixin):
	id=models.CharField(max_length=555,primary_key=True,editable=False)
	full_name=models.CharField(max_length=255)
	email=models.CharField(max_length=255,unique=True)
	phonenumber=models.CharField(max_length=255,unique=True)
	active=models.BooleanField(default=False)
	admin=models.BooleanField(default=False)
	email_verify=models.BooleanField(default=False)
	phonenumber_verify=models.BooleanField(default=False)
	added_on=models.DateTimeField(auto_now_add=True)
	referred_by=models.CharField(max_length=255,null=True,blank=True)
	referral_code=models.CharField(max_length=255,null=True,blank=True,unique=True)

	USERNAME_FIELD="phonenumber"
	REQUIRED_FIELDS=['full_name','email']

	objects=MyUserManager()

	def __str__(self):
		return str(self.id)

	def save(self,*args,**kwargs):
		if not self.id:
			total=User.objects.count()
			self.id="{}{:08d}".format("ACCNO",int(total)+1 if total is not None else 1)
		super().save(*args,**kwargs)
	@property
	def is_active(self):
		return self.active

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_staff(self):
		return True

	def has_perm(self,perm,obj=None):
		return True

	def has_perms(self,perms,obj=None):
		return True

	def has_module_perms(self,app_label):
		return True




