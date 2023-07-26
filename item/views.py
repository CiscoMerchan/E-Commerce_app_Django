from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import NewItemForm, EditItemForm
# Create your views here.

#broswer button
def items(request):
    #in /item/ search bar the 'query' will be fetch by the search bar and will be pass through the http request 
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all() 
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    #query filter to fetch the items either by name or description. "__icontains" = if contains.
    if query:
        items = items.filter(Q(name__icontains=query) | Q (description__icontains=query))

    return render(request, 'item/items.html',{
        'items': items,
        'query': query,
        'category_id': int(category_id),
        'categories':categories
    })


# get item detail through the id (pk = primary key) from the url. 'Item' from the item .models 
def detail(request, pk): 
    item = get_object_or_404(Item, pk=pk)
    #to render below the item all the items of the category. if column 'is_sold' False don't show the item. The 
    # ".exclude" does not rende the item that is all ready display  
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':

        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:    
        form = NewItemForm()
    
    return render(request, 'item/form.html', {
        'form':form,
        'title': 'New item', 
    })

# user edit item by the created user
@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user )
    
    if request.method == 'POST':

        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:    
        form = EditItemForm(instance=item) #By setting instance=item, the EditItemForm instance will be 
                                           # populated with the values of the item object that is passed to it.
                                           # This allows the form to display the existing values for the item instance,
                                           # which can be edited and updated using the form.
    
    return render(request, 'item/form.html', {
        'form':form,
        'title': 'Edit item', 
    })

# user delete item by the created user
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user )
    item.delete()
    
    return redirect('dashboard:index')


