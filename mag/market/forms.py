from django import forms
from .models import *

class RegForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['placeholder'] = visible.field.label
	username = forms.CharField(max_length=256, label='Имя пользователя')
	password = forms.CharField(max_length=256, label='Пароль')

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ["name", "price", "image"]