from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import ProductForm
from .models import Product

# CRUD = Create, Read, Update, Delete

# Home view
@login_required
def home_view(request):
    return render(
        request, 
        "invApp/home.html",
        )
    
# Create View
@login_required
def product_create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("invApp:product_list")
    
    context = {
        "form": form,
        }
    
    return render(
        request, 
        "invApp/product_form.html",
        context,
        )
    
# Read View
@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(
        request,
        "invApp/product_list.html",
        {"products": products},
    )
    
# Update View
@login_required
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("invApp:product_list")
    
    context = {
        "form": form,
    }
    
    return render(
        request, 
        "invApp/product_form.html",
        context,
        )

# Delete View
@login_required
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("invApp:product_list")
    
    context = {
        "product": product,
    }
    
    return render(
        request, 
        "invApp/product_confirm_delete.html",
        context,
        )