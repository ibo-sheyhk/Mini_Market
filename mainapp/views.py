from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('dashboard')
        
    context = {
        'form': form
    } 
    return render(request,'mainapp/registrations.html')


def test(request):
    return render(request,'mainapp/forms.html')


def dashboard(request):
    return render(request,'mainapp/index.html')


def chartjs(request):
    return render(request,'mainapp/chartjs.html')

    
def forms(request):
    return render(request,'mainapp/forms.html')


def fruitTable(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits,
    }
    return render(request,'mainapp/f-table.html',context)


def createFruit(request):
        form = CreateFruitForm()
        if request.method == "POST":
            form = CreateFruitForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('f_table')
            else:
                form = CreateFruitForm()
                
                
        context = {
            'form':form
        }
        return render(request,'mainapp/f-create.html',context)
    
    
def updateFruit(request,pk):
    fruit = Fruit.objects.get(id=pk)
    form = CreateFruitForm(instance=fruit)
    if request.method == "POST":
        form = CreateFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('f_table')
        
    context = {
        'form': form
    }
    
    return render(request, 'mainapp/f-create.html',context)
    
    
    
def fruitDelete(request,pk):
    fruit = Fruit.objects.get(id=pk)
    if request.method == "POST":
        fruit.delete()
        return redirect('f_table')
    
    context = {
        'fruit': fruit
    }    
    return render(request, 'mainapp/f-delete.html', context)



def meatTable(request):
    meats = Meat.objects.all()
    context = {
        'meats': meats,
    }
    return render(request,'mainapp/m-table.html',context)


def createMeat(request):
        form = CreateMeatForm()
        if request.method == "POST":
            form = CreateMeatForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('m_table')
            else:
                form = CreateMeatForm()
                
                
        context = {
            'form':form
        }
        return render(request,'mainapp/m-create.html',context)
    
    
def updateMeat(request,pk):
    meat = Meat.objects.get(id=pk)
    form = CreateMeatForm(instance=meat)
    if request.method == "POST":
        form = CreateMeatForm(request.POST, instance=meat)
        if form.is_valid():
            form.save()
            return redirect('m_table')
        
    context = {
        'form': form
    }
    
    return render(request, 'mainapp/f-create.html',context)
    
    
    
def meatDelete(request,pk):
    meat = Meat.objects.get(id=pk)
    if request.method == "POST":
        meat.delete()
        return redirect('m_table')
    
    context = {
        'meat': meat
    }    
    return render(request, 'mainapp/m-delete.html', context)



def futbolkaTable(request):
    futbolkas = Futbolka.objects.all()
    context = {
        'futbolkas': futbolkas,
    }
    return render(request,'mainapp/fu-table.html',context)

def koylakTable(request):
    koylaks = Koylak.objects.all()
    context = {
        'koylaks': koylaks,
    }
    return render(request,'mainapp/k-table.html',context)

def kepkaTable(request):
    kepkas = Kepka.objects.all()
    context = {
        'kepkas': kepkas,
    }
    return render(request,'mainapp/kepka.html',context)



def nonTable(request):
    nons = Non.objects.all()
    context = {
        'nons': nons,
    }
    return render(request,'mainapp/non.html',context)


def createNon(request):
        form = CreateNonForm()
        if request.method == "POST":
            form = CreateNonForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('n_table')
            else:
                form = CreateNonForm()
                
                
        context = {
            'form':form
        }
        return render(request,'mainapp/n-create.html',context)
    
    
def updateNon(request,pk):
    non = Non.objects.get(id=pk)
    form = CreateNonForm(instance=non)
    if request.method == "POST":
        form = CreateNonForm(request.POST, instance=non)
        if form.is_valid():
            form.save()
            return redirect('n_table')
        
    context = {
        'form': form
    }
    
    return render(request, 'mainapp/n-create.html',context)
    
    
    
def nonDelete(request,pk):
    non = Non.objects.get(id=pk)
    if request.method == "POST":
        non.delete()
        return redirect('n_table')
    
    context = {
        'non': non
    }    
    return render(request, 'mainapp/n-delete.html', context)



def suvTable(request):
    suvs = Suv.objects.all()
    context = {
        'suvs': suvs,
    }
    return render(request,'mainapp/suv.html',context)



def createSuv(request):
        form = CreateSuvForm()
        if request.method == "POST":
            form = CreateSuvForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('s_table')
            else:
                form = CreateSuvForm()
                
                
        context = {
            'form':form
        }
        return render(request,'mainapp/suv-create.html',context)
    
    
def updateSuv(request,pk):
    suv = Suv.objects.get(id=pk)
    form = CreateSuvForm(instance=suv)
    if request.method == "POST":
        form = CreateSuvForm(request.POST, instance=suv)
        if form.is_valid():
            form.save()
            return redirect('s_table')
        
    context = {
        'form': form
    }
    
    return render(request, 'mainapp/suv-create.html',context)
    
    
    
def suvDelete(request,pk):
    suv = Suv.objects.get(id=pk)
    if request.method == "POST":
        suv.delete()
        return redirect('s_table')
    
    context = {
        'suv': suv
    }    
    return render(request, 'mainapp/suv-delete.html', context)



def muzTable(request):
    muzs = Muzqaymoq.objects.all()
    context = {
        'muzs': muzs,
    }
    return render(request,'mainapp/muz-table.html',context)


def createMuz(request):
        form = CreateMuzqaymoqForm()
        if request.method == "POST":
            form = CreateMuzqaymoqForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('muz_table')
            else:
                form = CreateMuzqaymoqForm()
                
                
        context = {
            'form':form
        }
        return render(request,'mainapp/muz-create.html',context)
    
    
def updateMuz(request,pk):
    muzqaymoq = Muzqaymoq.objects.get(id=pk)
    form = CreateMuzqaymoqForm(instance=muzqaymoq)
    if request.method == "POST":
        form = CreateMuzqaymoqForm(request.POST, instance=muzqaymoq)
        if form.is_valid():
            form.save()
            return redirect('muz_table')
        
    context = {
        'form': form
    }
    
    return render(request, 'mainapp/muz-create.html',context)
    
    
    
def muzDelete(request,pk):
    muzqaymoq = Muzqaymoq.objects.get(id=pk)
    if request.method == "POST":
        muzqaymoq.delete()
        return redirect('muz_table')
    
    context = {
        'muzqaymoq': muzqaymoq
    }    
    return render(request, 'mainapp/muz-delete.html', context)



def shokolodTable(request):
    shokolods = Shokolod.objects.all()
    context = {
        'shokolods': shokolods,
    }
    return render(request,'mainapp/sh-table.html',context)


def createShokolod(request):
        form = CreateShokoladForm()
        if request.method == "POST":
            form = CreateShokoladForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('sh_table')
            else:
                form = CreateShokoladForm()
                
                
        context = {
            'form':form
        }
        return render(request,'mainapp/sh-create.html',context)
    
    
def updateShokolod(request,pk):
    shokolod = Shokolod.objects.get(id=pk)
    form = CreateShokoladForm(instance=shokolod)
    if request.method == "POST":
        form = CreateShokoladForm(request.POST, instance=shokolod)
        if form.is_valid():
            form.save()
            return redirect('sh_table')
        
    context = {
        'form': form
    }
    
    return render(request, 'mainapp/sh-create.html',context)
    
    
    
def shokolodDelete(request,pk):
    shokolod = Shokolod.objects.get(id=pk)
    if request.method == "POST":
        shokolod.delete()
        return redirect('sh_table')
    
    context = {
        'shokolod': shokolod
    }    
    return render(request, 'mainapp/sh.delete.html',context)


def milkTable(request):
    milks = Milk.objects.all()
    context = {
        'milks': milks,
    }
    return render(request,'mainapp/sut-table.html',context)


def flourTable(request):
    flours = Flour.objects.all()
    context = {
        'flours': flours,
    }
    return render(request,'mainapp/un-table.html',context)


def vegetableTable(request):
    vegetables = Vegetable.objects.all()
    context = {
        'vegetables': vegetables,
    }
    return render(request,'mainapp/sab-table.html',context)


def watchTable(request):
    watchs = Watch.objects.all()
    context = {
        'watchs': watchs,
    }
    return render(request,'mainapp/soat.html',context)

def watch_about(request):
    return render(request,'mainapp/qwer.html')


def shoesTable(request):
    shoess = Shoes.objects.all()
    context = {
        'shoess': shoess,
    }
    return render(request,'mainapp/kr-table.html',context)


def jiletTable(request):
    jilets = Jilet.objects.all()
    context = {
        'jilets': jilets,
    }
    return render(request,'mainapp/j-table.html',context)


def ventrovkaTable(request):
    ventrovkas = Vetrovka.objects.all()
    context = {
        'ventrovkas': ventrovkas,
    }
    return render(request,'mainapp/v-table.html',context)


def paypoqTable(request):
    paypoqs = Paypoq.objects.all()
    context = {
        'paypoqs': paypoqs,
    }
    return render(request,'mainapp/pa-table.html',context)


def employeetable(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request,'mainapp/e-table.html',context)


def productTable(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request,'mainapp/p-table.html',context)


def createProduct(request):
        form = CreateProductForm()
        if request.method == "POST":
            form = CreateProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('p_table')
            else:
                form = CreateProductForm()
                
                
        context = {
            'form':form
        }
        return render(request,'mainapp/p-create.html',context)
    
    
def updatePro(request,pk):
    product = Product.objects.get(id=pk)
    form = CreateProductForm(instance=product)
    if request.method == "POST":
        form = CreateProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('p_table')
        
    context = {
        'form': form
    }
    
    return render(request, 'mainapp/p-create.html',context)
    
 
def proDelete(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('p_table')
    
    context = {
        'product': product
    }    
    return render(request, 'mainapp/p-delete.html', context)   
    
    


def createEmployee(request):
        form = CreateEmployeeForm()
        if request.method == "POST":
            form = CreateEmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('e_table')
            else:
                form = CreateEmployeeForm()
                
                
        context = {
            'form':form
        }
        return render(request,'mainapp/e-create.html',context)
    
    
    
    
def updateEmp(request,pk):
    employee = Employee.objects.get(id=pk)
    form = CreateEmployeeForm(instance=employee)
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('e_table')
        
    context = {
        'form': form
    }
    
    return render(request, 'mainapp/e-create.html',context)


def empDelete(request,pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('e_table')
    
    context = {
        'employee': employee
    }    
    return render(request, 'mainapp/e-delete.html', context)