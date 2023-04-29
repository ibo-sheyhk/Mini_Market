from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'birth_date', 'spesifikation', 'country', 'city', 'adress', 'salary']
        
class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'create_date', 'end_date', 'quontity', 'description', 'price']
        
        
class CreateNonForm(forms.ModelForm):
    class Meta:
        model = Non
        fields = ['title', 'created_date', 'description', 'price']
        
        
class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['title', 'created_date','end_date', 'description', 'price']
        
        

class CreateMeatForm(forms.ModelForm):
    class Meta:
        model = Meat
        fields = ['title', 'created_date','end_date','description', 'price']
        
        
        
class CreateSuvForm(forms.ModelForm):
    class Meta:
        model = Suv
        fields = ['title', 'created_date', 'description', 'price']
        
        
        
class CreateMuzqaymoqForm(forms.ModelForm):
    class Meta:
        model = Muzqaymoq
        fields = ['title', 'created_date', 'description', 'price']
        
        
class CreateShokoladForm(forms.ModelForm):
    class Meta:
        model = Shokolod
        fields = ['title', 'created_date', 'description', 'price']
        
        
        
class CreateMilkForm(forms.ModelForm):
    class Meta:
        model = Milk
        fields = ['title', 'created_date','end_date', 'description', 'price']
        
        
        
class CreateFlourForm(forms.ModelForm):
    class Meta:
        model = Flour
        fields = ['title', 'created_date','end_date','description', 'price']
        
        

class CreateVegetablesForm(forms.ModelForm):
    class Meta:
        model = Vegetable
        fields = ['title', 'created_date','end_date','description', 'price']