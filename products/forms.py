from django import forms
from .models import Product, Colour, Closure, Style, Grape
from .widgets import CustomClearableFileInput

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        colours = Colour.objects.all()
        closures = Closure.objects.all()
        styles = Style.objects.all()
        grapes = Grape.objects.all()
