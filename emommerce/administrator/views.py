from django.shortcuts import render,redirect
from .models import Items
# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passw = request.POST.get('pass')

        if email == 'admin@gmail.com' and passw == 'admin':
            return redirect('home')
    
    return render(request,'login.html')
 
def inventory(request):

    if request.method == 'POST':
       
        item = Items()

        item.name= request.POST.get('name')
        item.category = request.POST.get('category')
        item.quantity = request.POST.get('quantity')
        item.price = request.POST.get('price')
        item.image = request.FILES['image']
        item.save()

        return render(request,'inventory.html')

    return render(request,'inventory.html')
    
def manage(request):

    if request.method == 'POST':

  
        delete_item = request.POST.get('delete')
        Items.objects.get(name=delete_item).delete()
        
        return redirect('manage')
    
    else:
        items = Items.objects.all()
        print(items)
        return render(request,'manage.html',{'items_display':items})

def update(request):
   
    update_item = request.POST.get('update')

   
    if request.POST.get("form_type") == 'update_form' and request.method == 'POST':

        change = Items.objects.get(name = update_item)
        print(request.POST.get('quantity'))
        #change.name= request.POST.get('name')
        #change.category = request.POST.get('category')
        #change.quantity = request.POST.get('quantity')
        #change.price = request.POST.get('price')

        #change.save()

        return render(request,'manage.html')
    
    else:
            
        print(update_item)
        items = Items.objects.filter(name=update_item).values()
        print(items)
      
        return render(request,'update.html',{'update_items':items})