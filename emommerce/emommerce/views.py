from django.shortcuts import redirect, render
from administrator.models import Items,users,Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login(request):

    if request.method == 'POST' :
        #print('hello_login')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        print(email,password)
        if users.objects.filter(user_email = email).filter(user_pass=password) != None:
        
            #users.objects.filter(user_email = email).values('user_name')[0].get('user_name')

            request.session['id'] = email
            return redirect('home')   
    
        else:
            redirect('signup')
    return render(request,'login_user.html')

def signup(request):
    if request.method == 'POST':
       
        details = users()

        details.user_name= request.POST.get('name')
        details.user_phone = request.POST.get('p_number')
        details.user_email= request.POST.get('email')
        details.user_pass = request.POST.get('password')
        
        details.save()

        return redirect('login')

    return render(request,'signup.html')


def home(request):

    current_user = request.session['id']

    if request.method == 'POST' :
        item_name = request.POST.get('item_name')
        
        cart_item = Cart()

        print(item_name,current_user)
        cart_item.user_email = current_user
        cart_item.user_item = item_name

        cart_item.save()

        return redirect('home')
    

    items = Items.objects.all()
    return render(request,'user_home.html',{'items':items,'user_id':current_user})


def cart(request):

    current_user = request.session['id']

  
    quantity_arr = []
    items_arr = []
    price_arr = []
    item_total = []
    image = []
    total_item = 0
    Total_value = 0

    if request.method == 'POST' :
     

        new_item = request.POST.get('submit_item')
        print(new_item)
        
        quantity_new = request.POST.get('quantity_change')
        items = Items.objects.filter(name = new_item)
        print(quantity_new)

        quantity = int(quantity_new)

        # get index 

        #index = items_arr.index(str(new_item))

        change = Cart.objects.get(user_item = new_item)
        change.item_quantity = quantity
        change.save()

        for i in Cart.objects.filter(user_email = current_user).values('user_item'):
            item_name = i.get('user_item')
            items = Items.objects.filter(name = item_name)

            price = items.values('price')[0]
            price = price.get('price')

            quantity = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_quantity')[0].get('item_quantity')

           # print( Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_quantity')[0].get('item_quantity'))
            total_item = (quantity * price) 

            quantity_arr.append(quantity)
            price_arr.append(price)
            items_arr.append(item_name)
            item_total.append(total_item)
            image.append(items.values('image')[0].get('image'))
            #print(items.values('image')[0].get('image'))
            collected = zip(items_arr,price_arr,item_total,image,quantity_arr)
            
            Total_value += total_item


        
        return render(request,'cart.html',{'products':collected,'Total':Total_value,'quantity_new':quantity}) 

    



    for i in Cart.objects.filter(user_email = current_user).values('user_item'):
        item_name = i.get('user_item')
        items = Items.objects.filter(name = item_name)

        price = items.values('price')[0]
        price = price.get('price')

        quantity = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_quantity')[0].get('item_quantity')

        total_item = (quantity * price) 

        quantity_arr.append(quantity)
        price_arr.append(price)
        items_arr.append(item_name)
        item_total.append(total_item)
        image.append(items.values('image')[0].get('image'))
        #print(items.values('image')[0].get('image'))
        collected = zip(items_arr,price_arr,item_total,image,quantity_arr)
        
        Total_value += total_item


        
    return render(request,'cart.html',{'products':collected,'Total':Total_value,'quantity_new':quantity})




def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')