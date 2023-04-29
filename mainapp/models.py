from django.db import models

# Create your models here.

class Employee(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    spesifikation = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='employee/')
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    salary = models.FloatField()
    
    def __str__(self):
        return self.full_name
    
    def final_salary(self):
        one_per = self.salary / 100
        ten_per = one_per * 10
        final_salary = self.salary - ten_per 
        return final_salary
    
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.DateField()
    end_date = models.DateField()
    quontity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
    def total_amounts(self):
        total_amounts = self.price * self.quontity
        return total_amounts 
    

class Fruit(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    

class Meat(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
    
class Futbolka(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    

    def __str__(self):
        return self.title
    
    
class Koylak(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    

class Kepka(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
    
class Non(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
    
class Suv(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
    
class Muzqaymoq(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
    
    
class Shokolod(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
    
class Milk(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
    
class Flour(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
    
class Vegetable(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
    
class Watch(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
    
class Shoes(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
    
class Jilet(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
    
    
class Vetrovka(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
    
class Paypoq(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    description = models.TextField() 
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title