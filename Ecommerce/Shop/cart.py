from .models import *
from Accounts.models import User

class Cart:
	def __init__(self,request):
		self.request=request
		self.user=User.objects.get(id=request.user.id)

	def add(self,product,count=1):
		print(product)
		item=self.get_item(product)
		item.quantity+=count
		item.save()

	def remove(self,product,count=1):
		item=self.get_item(product)
		if(item.quantity<=1):
			self.clear(product)
			return
		else:
			item.quantity-=count
		item.save()

	def clear(self,product):
		self.get_item(product).delete()

	def get_order(self):
		order,created=Order.objects.get_or_create(user=self.user,status=False)
		return order

	def get_item(self,product):
		item,created=OrderItem.objects.get_or_create(order=self.get_order(),product=product)
		return item

	def count(self):
		items=OrderItem.objects.filter(order=self.get_order())
		return sum([int(i.quantity) for i in items])

	@property
	def get_items(self):
		return OrderItem.objects.filter(order=self.get_order())
