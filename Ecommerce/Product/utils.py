from django.utils.text import slugify
import random
import string 
def clean_title(title):
	final=""
	for i in title:
		if(i.isalpha() or i.isnumeric() or i==" "):
			final+=i
		else:
			final+=" "
	return final

def string_generator(size=5,chars=string.ascii_lowercase+string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 

def slug_generator(instance,new_slug=None):
	if new_slug is not None:
		slug=new_slug
	else:
		if instance.title:
			slug=slugify(clean_title(instance.title))
		else:
			slug=slugify(string_generator())
	qs_exists =instance.__class__.objects.filter(slug =slug).exists() 
	if qs_exists:
		new_slug="{slug}-{randstr}".format(slug=slug,randstr=string_generator(size=4))     
		return slug_generator(instance,new_slug=new_slug) 
	return slug