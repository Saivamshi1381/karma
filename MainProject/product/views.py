from django.shortcuts import render
from.models import product,Category



def products(request):
    data = product.objects.all()
    cat = Category.objects.all()
   #type = product_type.objects.all()
    
    context = {
        'products':data,
        'cat':cat,
    } 
    return render(request,'product/products_list.html',context)

