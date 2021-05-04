from django import forms
from .models import Empleados, Compras, Productos, Ventas, Infoventas


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='email', widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget = forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            }



class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['nombre','apellidos','puesto','telefono','direccion']
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'puesto': 'Puesto',
            'telefono': 'Telefono',
            'direccion': 'Direccion',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'puesto': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
        }

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['cantidad','subtotal','descripcion','productos_id']
        labels = {
            'cantidad': 'Cantidad',
            'subtotal': 'Subtotal',
            'descripcion': 'Descripcion',
            'productos_id': 'Productos ID',
        }

        widgets = {
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'subtotal': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'productos_id': forms.Select(attrs={'class':'form-control'}),
        }

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['producto','descripcion','preciocompra','precioventa','existencia']

        labels = {
            'producto': 'Producto',
            'descripcion': 'Descripcion',
            'preciocompra': 'Precio De Compra',
            'precioventa': 'Precio De Venta',
            'existencia': 'Existencia',
        }

        widgets = {
            'producto': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'preciocompra': forms.NumberInput(attrs={'class':'form-control'}),
            'precioventa': forms.NumberInput(attrs={'class':'form-control'}),
            'existencia': forms.NumberInput(attrs={'class':'form-control'}),
        }




class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['total','fecha','nit','nombre','direccion','empleados_id']

        labels = {
                'total': 'Total',
                'fecha': 'Fecha',
                'nit': 'NIT',
                'nombre': 'Nombre',
                'direccion': 'Direccion',
                'empleados_id': 'Empleado',

            }

        widgets = {
            'total': forms.NumberInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'nit': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'empleados_id': forms.Select(attrs={'class':'form-control'}),

        }


class InfoventasForm(forms.ModelForm):
    class Meta:
        model = Infoventas
        fields =  ['cantidad','subtotal','productos_id','ventas_id']

        labels = {
                'cantidad': 'Cantidad',
                'subtotal': 'SubTotal',
                'productos_id': 'Producto',
                'ventas_id': 'Venta',

            }

        widgets = {
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
            'subtotal': forms.NumberInput(attrs={'class':'form-control'}),
            'productos_id': forms.Select(attrs={'class':'form-control'}),
            'ventas_id': forms.Select(attrs={'class':'form-control'}),
        }
