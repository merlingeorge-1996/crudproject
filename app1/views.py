import os
from django.shortcuts import render,redirect
from .models import product

# Create your views here.
def index(request):
    return render(request,'addproduct.html')

def add_product(request):
    if request.method == 'POST':
        pname=request.POST['pname']
        qty=request.POST['qty']  
        price=request.POST['prc']
        #request.POST.get(')
        #image=request.FILES['file']
        image=request.FILES.get('file')
        prd = product(product_name=pname,quantity=qty,price=price,image=image)
        print("Save data...")
        prd.save()
        return redirect('show_products')
def show_products(request):
    prdts = product.objects.all()
    return render(request,'show_product.html',{'prdts':prdts})

def editpage(request,pk):
    prdts = product.objects.get(id=pk)
    return render(request,'Edit.html',{'prdts':prdts})

def edit_product(request,pk):    
    if request.method=='POST':
        prdcts = product.objects.get(id=pk)
        prdcts.product_name = request.POST.get('pname')
        prdcts.price = request.POST.get('price')
        prdcts.quantity = request.POST.get('qty')
        if len(request.FILES)!=0:
            if len(prdcts.image)>0:
                os.remove(prdcts.image.path)
            prdcts.image = request.FILES.get('file')
        prdcts.save()
        return redirect('show_products')
    return render(request, 'Edit.html',)

def delete(request,pk):
    p = product.objects.filter(id=pk)
    p.delete()
    return redirect('show_products')
    