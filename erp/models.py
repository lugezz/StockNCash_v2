from datetime import datetime
from crum import get_current_user
from django.db import models
from django.forms.models import model_to_dict

from erp.choices import gender_choices
from snc.settings import MEDIA_URL, STATIC_URL
from user.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nombre")
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user_creation = user
        self.user_update = user
        return super().save(force_insert, force_update, using, update_fields)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nombre')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    image = models.ImageField(upload_to='product', null=True, blank=True, verbose_name='Imagen')
    price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, verbose_name='Precio de Venta')

    def __str__(self):
        return self.name.capitalize()

    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        item['image'] = self.get_image()
        item['price'] = format(self.price, '.2f')
        return item

    def get_image(self):
        if self.image:
            return f'{MEDIA_URL}{self.image}'
        else:
            return f'{STATIC_URL}img/empty.png'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_birthday = models.DateField(default="01/01/1990", verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return f'{self.names} {self.surnames}'

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {
            'id': self.gender,
            'name': self.get_gender_display()
            }
        item['date_birthday'] = self.date_birthday.strftime('%d/%m/%Y')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Sale(models.Model):
    # Agregar número de factura
    cli = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    date = models.DateTimeField(default=datetime.now, verbose_name='Fecha')
    subtotal = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.cli.names} ({self.id})'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    Quant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.prod.name} Quant: {self.cant} Date: {self.sale.date}'

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
