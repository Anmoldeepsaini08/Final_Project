from django.shortcuts import redirect, render
from administrator.models import Items,users,Cart,Address,Orders,Wishlist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
from django.conf import settings

def login(request):

    if request.method == 'POST' :
        #print('hello_login')
        email = request.POST.get('email')
        password = request.POST.get('pass')
       # print(email,password)
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

        if 'like-button' in request.POST:
            item_name = request.POST.get('like-button')

            wish = Wishlist()

            #print(current_user,item_name)
            wish.user_email  = current_user
            wish.user_item = item_name
            wish.save()

     

        else:

            item_name = request.POST.get('item_name')
            
            cart_item = Cart()

        # print(item_name,current_user)
            cart_item.user_email = current_user
            cart_item.user_item = item_name

            cart_item.save()

        return redirect('home')
    

    items = Items.objects.all()
    items = items[:4]

    items_2 = Items.objects.all()
    items_2 = items_2

    return render(request,'user_home.html',{'items':items,'user_id':current_user,'items_2':items_2})

def mens(request):

    current_user = request.session['id']

    if request.method == 'POST' :

        if 'like-button' in request.POST:
            item_name = request.POST.get('like-button')

            wish = Wishlist()

            #print(current_user,item_name)
            wish.user_email  = current_user
            wish.user_item = item_name
            wish.save()

     

        else:

            item_name = request.POST.get('item_name')
            
            cart_item = Cart()

        # print(item_name,current_user)
            cart_item.user_email = current_user
            cart_item.user_item = item_name

            cart_item.save()

        return redirect('mens')

    items = Items.objects.all()
    items = items


    return render(request,'mens.html',{'items':items,'user_id':current_user})


def women(request):

    current_user = request.session['id']

    if request.method == 'POST' :

        if 'like-button' in request.POST:
            item_name = request.POST.get('like-button')

            wish = Wishlist()

            #print(current_user,item_name)
            wish.user_email  = current_user
            wish.user_item = item_name
            wish.save()

     

        else:

            item_name = request.POST.get('item_name')
            
            cart_item = Cart()

        # print(item_name,current_user)
            cart_item.user_email = current_user
            cart_item.user_item = item_name

            cart_item.save()

        return redirect('mens')

    items = Items.objects.all()
    items = items


    return render(request,'women.html',{'items':items,'user_id':current_user})

def cart(request):

    current_user = request.session['id']

    collected = ''
    quantity_arr = []
    items_arr = []
    price_arr = []
    item_total = []
    image = []
    total_item = 0
    Total_value = 0
    change_size = ''
    size_arr = []

    if request.method == 'POST' :
     
        if 'delete-button' in request.POST:
            delete_item = request.POST.get('delete-button')
            #print(delete_item)

            Cart.objects.filter(user_item = delete_item).delete()


            return redirect('cart')

        elif 'size-btn' in request.POST:

            size = request.POST.get('sizes') 
            new_item = request.POST.get('size-btn') 
            #print(size,new_item)

            change = Cart.objects.get(user_item = new_item)
        
            change.item_size = size
            change.save()

            for i in Cart.objects.filter(user_email = current_user).values('user_item'):
                item_name = i.get('user_item')
                items = Items.objects.filter(name = item_name)

                price = items.values('price')[0]
                price = price.get('price')

                quantity = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_quantity')[0].get('item_quantity')

                Size_items = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_size')[0].get('item_size')

                total_item = (quantity * price) 

                size_arr.append(Size_items)
                quantity_arr.append(quantity)
                price_arr.append(price)
                items_arr.append(item_name)
                item_total.append(total_item)
                image.append(items.values('image')[0].get('image'))
                #print(items.values('image')[0].get('image'))
                collected = zip(items_arr,price_arr,item_total,image,quantity_arr,size_arr)
                
                Total_value += total_item
            
                

        else:


            new_item = request.POST.get('submit_item')
            #print(new_item)
            
            quantity_new = request.POST.get('quantity_change')
            items = Items.objects.filter(name = new_item)
        # print(quantity_new)

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

                Size_items = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_size')[0].get('item_size')
                total_item = (quantity * price) 

                size_arr.append(Size_items)
                quantity_arr.append(quantity)
                price_arr.append(price)
                items_arr.append(item_name)
                item_total.append(total_item)
                image.append(items.values('image')[0].get('image'))
                #print(items.values('image')[0].get('image'))
                collected = zip(items_arr,price_arr,item_total,image,quantity_arr,size_arr)
                
                Total_value += total_item


        
        return render(request,'cart.html',{'products':collected,'Total':Total_value,'user_id':current_user}) 

    


    else:

        try:

            for i in Cart.objects.filter(user_email = current_user).values('user_item'):
                item_name = i.get('user_item')
                items = Items.objects.filter(name = item_name)

                price = items.values('price')[0]
                price = price.get('price')

                quantity = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_quantity')[0].get('item_quantity')

                total_item = (quantity * price) 

                Size_items = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_size')[0].get('item_size')
                size_arr.append(Size_items)
                quantity_arr.append(quantity)
                price_arr.append(price)
                items_arr.append(item_name)
                item_total.append(total_item)
                image.append(items.values('image')[0].get('image'))
                #print(items.values('image')[0].get('image'))
                collected = zip(items_arr,price_arr,item_total,image,quantity_arr,size_arr)
                
                Total_value += total_item

        except:
            return redirect('home')
        
        return render(request,'cart.html',{'products':collected,'Total':Total_value,'user_id':current_user})



def account(request):

    current_user = request.session['id']
   



    if request.method == 'POST' :
        address = request.POST.get('address')
        pin = request.POST.get('pin_code')
        
    

        details = Address()

        details.user_email= current_user
        details.user_address = address
        details.user_pincode= pin
        
        
        details.save()


        user_name = users.objects.filter(user_email = current_user).values('user_name')[0].get('user_name')

        phone = users.objects.filter(user_email = current_user).values('user_phone')[0].get('user_phone')
        
        address_user = Address.objects.filter(user_email = current_user).values('user_address')[0].get('user_address')
        pin_code = Address.objects.filter(user_email = current_user).values('user_pincode')[0].get('user_pincode')

        return render(request,'account.html',{'user_id':current_user,'user_name':user_name,'user_phone':phone,'address':address_user,'user_pincode':pin_code})

    else:
        user_name = users.objects.filter(user_email = current_user).values('user_name')[0].get('user_name')

        phone = users.objects.filter(user_email = current_user).values('user_phone')[0].get('user_phone')

   

        address_user = Address.objects.filter(user_email = current_user).values('user_address')[0].get('user_address')
        pin_code = Address.objects.filter(user_email = current_user).values('user_pincode')[0].get('user_pincode')

        return render(request,'account.html',{'user_id':current_user,'user_name':user_name,'user_phone':phone,'address':address_user,'user_pincode':pin_code})




def checkout(request):

    collected = ''
    quantity_arr = []
    items_arr = []
    price_arr = []
    item_total = []
    image = []
    total_item = 0
    Total_value = 0
    
    size_arr = []
    address = ''
    pincode = 0
    phone_number = 0

    name = ''

    current_user = request.session['id']
    if Address.objects.filter(user_email = current_user).values('user_address')[0].get('user_address') == '':
        redirect('account')

    else:

        try:
            # for address
            name = users.objects.filter(user_email = current_user).values('user_name')[0].get('user_name')
            address = Address.objects.filter(user_email = current_user).values('user_address')[0].get('user_address')
            pincode = Address.objects.filter(user_email = current_user).values('user_pincode')[0].get('user_pincode')
            phone_number = users.objects.filter(user_email = current_user).values('user_phone')[0].get('user_phone')

            # for items
            for i in Cart.objects.filter(user_email = current_user).values('user_item'):
                    item_name = i.get('user_item')
                    items = Items.objects.filter(name = item_name)

                    price = items.values('price')[0]
                    price = price.get('price')

                    quantity = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_quantity')[0].get('item_quantity')

                    total_item = (quantity * price) 

                    Size_items = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_size')[0].get('item_size')
                    size_arr.append(Size_items)
                    quantity_arr.append(quantity)
                    price_arr.append(price)
                    items_arr.append(item_name)
                    item_total.append(total_item)
                   
                    collected = zip(items_arr,size_arr,quantity_arr,price_arr)
                    
                    Total_value += total_item

        except:
            return redirect('home')
        
        

        #user_address = Address.objects.filter(user_email = current_user).values('user_address')[0].get('user_address')

        return render(request,'checkout.html',{'products':collected,'Total':Total_value,'user_id':current_user,'address_bill':address,'pin':pincode,'call':phone_number,'name':name})


def payment(request):


    current_user = request.session['id']
    Total_value = 0

    if request.method == 'POST':

        if 'payment_ok' in request.POST:
            #print('hello_world')

            # save purchase cart items in order and delete cart for particular user

            order = Orders()

            for i in Cart.objects.filter(user_email = current_user).values('user_item'):
                    item_name = i.get('user_item')
                    items = Items.objects.filter(name = item_name)

                    order.user_email = current_user
                    order.user_item = Cart.objects.filter(user_email = current_user).values('user_item')[0].get('user_item')
                    order.item_quantity = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_quantity')[0].get('item_quantity')

                    order.item_size = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_size')[0].get('item_size')
            
                    x = datetime.datetime.now()
                    date = x.strftime("%x")

                    order.date = date
                    order.user_total = Items.objects.filter(name = item_name).values('price')[0].get('price')


                    order.save()


            


            


            Cart.objects.filter(user_email = current_user).delete()


            return redirect('home')
        

    for i in Cart.objects.filter(user_email = current_user).values('user_item'):
        item_name = i.get('user_item')
        items = Items.objects.filter(name = item_name)

        price = items.values('price')[0]
        price = price.get('price')

        quantity = Cart.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_quantity')[0].get('item_quantity')

        total_item = (quantity * price) 

       
        Total_value += total_item



    return render(request,'payment.html',{'Total':Total_value})



def order(request):
    current_user = request.session['id']


    collected = ''
    quantity_arr = []
    items_arr = []
    price_arr = []
    
    date_arr = []
    size_arr = []

    for i in Orders.objects.filter(user_email = current_user).values('user_item'):
        item_name = i.get('user_item')
        
        quantity = Orders.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_quantity')[0].get('item_quantity')

        Size_items = Orders.objects.filter(user_email = current_user).filter(user_item = item_name).values('item_size')[0].get('item_size')
        
        order_date = Orders.objects.filter(user_email = current_user).filter(user_item = item_name).values('date')[0].get('date')
        price = Orders.objects.filter(user_email = current_user).filter(user_item = item_name).values('user_total')[0].get('user_total')

        price_arr.append(price)
        size_arr.append(Size_items)
        quantity_arr.append(quantity)
  
        items_arr.append(item_name)
        date_arr.append(order_date)
                    
        collected = zip(items_arr,date_arr,quantity_arr,size_arr,price_arr)

                    
                    
   #     print(order_date,item_name,price,quantity,Size_items)


    return render(request,'order.html',{'user_id':current_user,'products':collected})








def wishlist(request):

    
    current_user = request.session['id']

    collected = ''
    
    items_arr = []
    price_arr = []
    item_total = []
    image = []
    total_item = 0
  
#    print(Wishlist.objects.filter(user_email = current_user).values('user_item')[0].get('user_item'))



    if 'delete-button' in request.POST:
            
        delete_item = request.POST.get('delete-button')
            #print(delete_item)

        Wishlist.objects.filter(user_item = delete_item).delete()

        return redirect('wishlist')

            
    elif 'to_cart' in request.POST:
        item_name = request.POST.get('to_cart')
            
        cart_item = Cart()

        # print(item_name,current_user)
        cart_item.user_email = current_user
        cart_item.user_item = item_name

        cart_item.save()

    #    print(Wishlist.objects.filter(user_email = current_user).values('user_item'))
    for i in Wishlist.objects.filter(user_email = current_user).values('user_item'):
        item_name = i.get('user_item')
       # print(Items.objects.filter(name = item_name))
        if not Items.objects.filter(name = item_name):
            continue
        else:

            items = Items.objects.filter(name = item_name)
           # print(items)
            
            
            price = items.values('price')[0]
            price = price.get('price')

                
            price_arr.append(price)
            items_arr.append(item_name)
            item_total.append(total_item)
            image.append(items.values('image')[0].get('image'))
                        #print(items.values('image')[0].get('image'))
            collected = zip(image,items_arr,price_arr)
                        
           
       
        

        
        
    return render(request,'wishlist.html',{'wish':collected,'user_id':current_user}) 

    


                
    
def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')