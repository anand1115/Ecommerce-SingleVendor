from django.db import models
from Accounts.models import User
from Product.models import Product


class Address(models.Model):
	id=models.CharField(primary_key=True,editable=False,max_length=50)
	User=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
	Name=models.CharField(max_length=200)
	HouseNumber=models.CharField(max_length=500,null=False)
	Area=models.CharField(max_length=500,null=False)
	Landmark=models.CharField(max_length=500,null=False)
	City=models.CharField(max_length=500,null=False)
	State=models.CharField(max_length=200,null=False)
	Pincode=models.CharField(max_length=200,null=False)
	AddedOn=models.DateTimeField(auto_now_add=True)
	EditedOn=models.DateTimeField(auto_now=True)
	Mobile=models.CharField(max_length=200)
	AltMobile=models.CharField(max_length=200)
	Type=models.CharField(max_length=200)
	Active=models.BooleanField(default=True)

	def save(self,*args,**kwargs):
		if not self.id:
			count=Address.objects.count()
			self.id="ADDR{:08d}".format(int(count)+1 if count is not None else 1)
		super().save(*args,**kwargs)

	def __str__(self):
		return str(self.id)

class Order(models.Model):
	id=models.CharField(primary_key=True,editable=False,max_length=50)
	user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
	address=models.ForeignKey(Address,on_delete=models.SET_NULL,null=True,blank=True)
	status=models.BooleanField(default=False)

	def save(self,*args,**kwargs):
		count=Order.objects.count()
		self.id="{:08}".format(int(count)+1 if count is not None else 1)
		super().save(*args,**kwargs)


	@property
	def total_selling_price(self):
		orderitems=self.orderitem_set.all()
		total_price=sum([i.item_selling_price for i in orderitems])
		return total_price

	@property
	def total_marked_price(self):
		orderitems=self.OrderItem_set.all()
		total_price=sum([i.item_marked_price for i in orderitems])
		return total_price
	@property
	def total_discount_price(self):
		orderitems=self.OrderItem_set.all()
		total_price=sum([i.item_discount_price for i in orderitems])
		return total_price


class OrderItem(models.Model):
	id=models.CharField(primary_key=True,editable=False,max_length=50)
	product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
	order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
	quantity=models.PositiveIntegerField(default=0)
	added_on=models.DateTimeField(auto_now_add=True)

	def save(self,*args,**kwargs):
		if not self.id:
			count=OrderItem.objects.count()
			self.id="{:08d}".format(int(count)+1 if count is not None else 1)
		super().save(*args,**kwargs)

	@property
	def item_selling_price(self):
		return self.product.selling_price*self.quantity

	@property
	def item_discount_price(self):
		return self.product.discount_price*self.quantity

	@property
	def item_marked_price(self):
		return self.product.marked_price*self.quantity







