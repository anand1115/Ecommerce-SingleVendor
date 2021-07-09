from django import forms


state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),
	            ("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),
	            ("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),
	            ("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),
	            ("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),
	            ("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),
	            ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
	            ("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

class AddressForm(forms.Form):
	Name=forms.CharField(widget=forms.TextInput,label="")
	HouseNumber=forms.CharField(widget=forms.TextInput,label="")
	Area=forms.CharField(widget=forms.TextInput,label="")
	Landmark=forms.CharField(widget=forms.TextInput,label="")
	City=forms.CharField(widget=forms.TextInput,label="")
	State=forms.ChoiceField(choices=state_choices,widget=forms.Select,label="")
	Pincode=forms.IntegerField(widget=forms.NumberInput,label="")
	Mobile=forms.IntegerField(widget=forms.NumberInput,label="")
	AltMobile=forms.IntegerField(widget=forms.NumberInput,label="")
	Type=forms.ChoiceField(choices=(('Home','Home'),('Work','Work')),widget=forms.Select,label="")

	def __init__(self,*args,**kwargs):
		super(AddressForm,self).__init__(*args,**kwargs)
		self.fields['Name'].widget.attrs['class']='name'
		self.fields['Name'].widget.attrs['id']='name'
		self.fields['Name'].widget.attrs['placeholder']='Full Name'
		self.fields['HouseNumber'].widget.attrs['class']='name'
		self.fields['HouseNumber'].widget.attrs['id']='name'
		self.fields['HouseNumber'].widget.attrs['placeholder']='House Number'
		self.fields['Area'].widget.attrs['class']='name'
		self.fields['Area'].widget.attrs['id']='name'
		self.fields['Area'].widget.attrs['placeholder']='Area'
		self.fields['Landmark'].widget.attrs['class']='name'
		self.fields['Landmark'].widget.attrs['id']='name'
		self.fields['Landmark'].widget.attrs['placeholder']='Landmark'
		self.fields['City'].widget.attrs['class']='name'
		self.fields['City'].widget.attrs['id']='name'
		self.fields['City'].widget.attrs['placeholder']='City'
		self.fields['State'].widget.attrs['class']='name'
		self.fields['State'].widget.attrs['id']='name'
		self.fields['State'].widget.attrs['placeholder']='State'
		self.fields['Pincode'].widget.attrs['class']='name'
		self.fields['Pincode'].widget.attrs['id']='name'
		self.fields['Pincode'].widget.attrs['placeholder']='Pincode'
		self.fields['Mobile'].widget.attrs['class']='name'
		self.fields['Mobile'].widget.attrs['id']='name'
		self.fields['Mobile'].widget.attrs['placeholder']='Mobile'
		self.fields['AltMobile'].widget.attrs['class']='name'
		self.fields['AltMobile'].widget.attrs['id']='name'
		self.fields['AltMobile'].widget.attrs['placeholder']='Alternate Mobile'
		self.fields['Type'].widget.attrs['class']='name'
		self.fields['Type'].widget.attrs['id']='name'
		self.fields['Type'].widget.attrs['placeholder']='Address Type'

	def clean_Name(self):
		name=self.cleaned_data.get('Name',None)
		if name and name.isalpha() and 3<len(str(name))<=20:
			pass
		else:
			raise forms.ValidationError("Please Enter Valid Name .!")
		return name

	def clean_HouseNumber(self):
		housenumber=self.cleaned_data.get('HouseNumber',None)
		if housenumber and 3<=len(str(housenumber))<30:
			pass
		else:
			raise forms.ValidationError("Please Provide Valid House Number .!")
		return housenumber

	def clean_Area(self):
		area=self.cleaned_data.get('Area',None)
		if area and 3<len(str(area))<40:
			pass
		else:
			raise forms.ValidationError("Please Provide Valid Area .!")
		return area

	def clean_Landmark(self):
		landmark=self.cleaned_data.get('Landmark',None)
		if landmark and 3<len(str(landmark))<50:
			pass
		else:
			raise forms.ValidationError("Please Provide Valid Landmark .!")
		return landmark

	def clean_City(self):
		city=self.cleaned_data.get('City',None)
		if city and 3<=len(str(city))<=50:
			pass
		else:
			raise forms.ValidationError("Please Provide Valid City .!")
		return city

	def clean_State(self):
		state=self.cleaned_data.get('State',None)
		if state:
			pass
		else:
			raise forms.ValidationError("Please Provide Valid State .!")
		return state

	def clean_Pincode(self):
		pincode=self.cleaned_data.get('Pincode',None)
		if pincode and str(pincode).isnumeric() and len(str(pincode))==6:
			pass
		else:
			raise forms.ValidationError("Please Provide Valid Pincode .!")
		return pincode

	def clean_Mobile(self):
		mobile=self.cleaned_data.get('Mobile',None)
		if mobile and str(mobile).isnumeric() and len(str(mobile))==10:
			pass
		else:
			raise forms.ValidationError("Please Provide Valid Mobile Number .!")
		return mobile

	def clean_AltMobile(self):
		altmobile=self.cleaned_data.get('AltMobile',None)
		mobile=self.clean_Mobile()
		if altmobile and str(altmobile).isnumeric() and len(str(altmobile))==10:
			pass
		else:
			raise forms.ValidationError("Please Provide Valid Mobile Number .!")
		if altmobile and mobile==altmobile:
			raise forms.ValidationError("Mobile Number And Alternate Mobile Number must be different .!")
		return altmobile

	def clean_Type(self):
		Type=self.cleaned_data.get('Type',None)
		if Type:
			pass
		else:
			raise forms.ValidationError("Please Provide Valid Address Type .!")
		return Type


