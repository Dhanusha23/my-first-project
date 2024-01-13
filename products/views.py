from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from decimal import Decimal, InvalidOperation  # Import Decimal to handle currency calculations
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Cart
from .models import Cart, Product,Kids,Women,Men,Unisex

# Create your views here.
def home(request):
    #products=Product.objects.all()
    return render(request,'home.html')#,{'products':products})

#def Home(request):
    return HttpResponse('<h1>ABOUT PAGE</h1>')

def Kid(request):
    kids=Kids.objects.all()
    return render(request,'kids.html',{'kids':kids})

def Woman(request):
    women = Women.objects.all()
    return render(request, 'women.html', {'women': women})

def Man(request):
    men = Men.objects.all()
    return render(request, 'men.html', {'men': men})

def uni(request):
    unisex = Unisex.objects.all()
    return render(request, 'unisex.html', {'unisex': unisex})
'''
def cart(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})
'''
@login_required
def cart(request):
    # Filter cart items for the current user
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})


@csrf_exempt
@login_required # Ensure the user is logged in to add items to the cart
def save_to_cart(request):
    if request.method == 'POST':
        user=request.user  # Get the logged-in user
        cname = request.POST.get('cname')
        cprice = request.POST.get('cprice')
        cimage = request.POST.get('cimage')

        # Save the data to the Cart model
        cart = Cart.objects.create(user=user,cname=cname, cprice=cprice, cimage=cimage)
        cart.save()

        # Return a success response
        return JsonResponse({'success': 'Cart item saved successfully.'})

    
    # Print the request method to verify the method
    print('Request Method:', request.method)


    # Return an error response for invalid request method
    return JsonResponse({'error': 'Invalid request method.'})


@csrf_exempt
@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('itemId')
        cart_item = get_object_or_404(Cart, id=item_id)
        cart_item.delete()
        return JsonResponse({'success': 'Item removed from cart successfully.'})

    return JsonResponse({'error': 'Invalid request method.'})


@csrf_exempt
@login_required
def cart_total(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)

        total_price = Decimal(0)  # Initialize as a Decimal
        for item in cart_items:
            item_price = Decimal(item.cprice)  # Convert item.cprice to Decimal
            total_price += item_price

        print('Total Price:', total_price)  # Debug line

        return JsonResponse({'total_price': total_price})

    return JsonResponse({'error': 'Invalid request method.'})

