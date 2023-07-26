from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse

# Create your views here.

#import images with the Categories from the DB 
from item.models import Category, Item

from .forms import SignUpForm

#index page
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]  #fetch tyhe items from the Item TABLE. the .filte 
                                                        #(column "is_sold") if == False wont show the Item. "[0:6]" = get from 0 to 6 items 
    categories = Category.objects.all() # all the Category
    
    return render(request, 'core/index.html', {
        'categories': categories,
                  'items': items,
    })

#contact page
def contact(request):
    return render(request, 'core/contact.html')


#signup form
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

#logout
def logout_user(request):
    logout(request)
    return redirect(reverse('core:index'))