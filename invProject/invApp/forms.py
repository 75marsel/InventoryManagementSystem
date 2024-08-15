from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            "product_id": "Product ID",
            "product_name": "Product Name",
            "serial_number": "Serial Number",
            "price": "Price",
            "quantity": "Quantity",
            "supplier": "Supplier",  
            "delivered_date": "Delivered Date",
            "product_image": "Product Image",
        }
        widgets ={
            "product_id": forms.NumberInput(
                attrs={
                    "placeholder": "e.g 1",
                    "class": "form-control",
                }),
            "product_name": forms.TextInput(
                attrs={
                    "placeholder": "Shirt",
                    "class": "form-control",
                }),
            "serial_number": forms.TextInput(
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
            "delivered_date": forms.DateTimeInput(
                attrs={
                    "placeholder": "Delivered Date",
                    "class": "form-control",
                    "type": "datetime-local",
            }),
            'product_image': forms.ClearableFileInput(
                attrs={
                "class": "form-control",
                'accept': 'image/*'
            }),
        }