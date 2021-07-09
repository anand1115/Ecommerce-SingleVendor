from django.db import models
from .utils import slug_generator
from django.urls import reverse
from Accounts.models import User



def mypath(instance,filename):
	return "Products/Product_{}/Main_{}".format(instance.id,filename)


def mypath_2(instance,filename):
	return "Products/Product_{}/Side_{}".format(instance.product.id,filename)


class Product(models.Model):
	id=models.CharField(primary_key=True,editable=False,max_length=50)
	title=models.CharField(max_length=255)
	slug=models.SlugField(null=True,blank=True)
	marked_price=models.DecimalField(max_digits=10,decimal_places=2)
	selling_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	discount_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	discount=models.PositiveSmallIntegerField()
	image=models.ImageField(upload_to=mypath)


	def save(self,*args,**kwargs):
		if not self.id:
			total=Product.objects.count()
			self.id="{}{:05d}".format('PRODUCT', int(total)+1 if total is not None else 1)
		if not self.slug:
			self.slug=slug_generator(self)
		if not 0<=self.discount<=99:
			self.discount=0
			self.discount_price=0
			self.selling_price=self.marked_price
		else:
			self.discount_price=(self.marked_price*self.discount)//100
			self.selling_price=self.marked_price-((self.marked_price*self.discount)//100)
		super().save(*args,**kwargs)

	@property	
	def image_url(self):
		try:
			url=self.image.url
		except:
			url=""
		return url

	def get_absolute_url(self):
		return reverse('Product:Product',kwargs={"slug":self.slug})

	def __str__(self):
		return str(self.id)








class ProductImages(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	image=models.ImageField(upload_to=mypath_2)

	@property	
	def image_url():
		try:
			url=self.image.url
		except:
			url=""
		return url



class WishListProduct(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.PositiveSmallIntegerField()
	active=models.BooleanField(default=True)

	def __str__(self):
		return str(self.user)+" "+str(self.product)

	def save(self,*args,**kwargs):
		if(self.quantity<0):
			self.quantity=1
		super().save(*args,**kwargs)



	




