from datetime import datetime

from django.forms import DateInput, ModelForm, Select, Textarea, TextInput

from erp.models import Category, Client, Product, Sale


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        exclude = ['user_creation', 'user_update']
        fields = '__all__'
        # exclude = ... si necesitara excluir campos

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': "Ingrese el nombre de categoría"
                }
            ),

            'desc': Textarea(
                attrs={
                    'placeholder': "Ingrese la descipción del nombre de categoría",
                    'rows': 3,
                    'cols': 3
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 5:
    #         raise forms.ValidationError('Validacion xxx')
    #         #self.add_error('name', 'Le faltan caracteres')
    #     return cleaned


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dni',
                }
            ),
            'date_birthday': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'gender': Select()
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        block_attr = {
            'readonly': True,
            'class': 'form-control',
        }

        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['autofocus'] = True

        self.fields['subtotal'].widget.attrs = block_attr
        self.fields['total'].widget.attrs = block_attr

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 100%'
                }
            ),
            'date': DateInput(
                format=("%d/%m/%Y"),
                attrs={
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'id': 'datepicker',
                }
            )
        }
