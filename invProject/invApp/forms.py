from django import forms
from .models import Product

class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            "product_id": "Product ID",
            "name": "Name",
            "sku": "SKU",
            "price": "Price",
            "quantity": "Quantity",
            "supplier": "Supplier",  
        }
        widhets ={
            "product_id": forms.NumberInput(
                attrs={
                    "placeholder": "e.g 1",
                    "class": "form-control",
                }),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Shirt",
                    "class": "form-control",
                }),
            "sku": forms.TextInput(
                attrs={
                    "placeholder": "Serial Number",
                    "class": "form-control",
                }),
            "price": forms.NumberInput(
                attrs={
                    "placeholder": "19.99",
                    "class": "form-control",
                }),
            "quantity": forms.NumberInput(
                attrs={
                    "placeholder": "10",
                    "class": "form-control",
                }),
            "supplier": forms.TextInput(
                attrs={
                    "placeholder": "ABC Company",
                    "class": "form-control",
                }),
        }