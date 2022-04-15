from django import forms
from .models import ExchangeRate

class ExchangeRateForm(forms.ModelForm):
    """Form definition for ExchangeRate."""

    class Meta:
        """Meta definition for ExchangeRateform."""

        model = ExchangeRate
        fields = '__all__'
        exclude = ('date',)
        widgets ={
            'sale_price': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                }
            ),
            'purchase_price': forms.TextInput(attrs={
                'class': 'form-control',
                'type':'text',
            }),
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type':'date'
                }
            )
        }

    #Validate that the values to update are float
    def clean_sale_price(self):
        sale_price = self.cleaned_data.get('sale_price')
        try:
            float(sale_price)
        except:
            self.add_error('sale_price','Debe ingresar un valor numerico')
        return sale_price
    
    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get('purchase_price')
        try:
            float(purchase_price)
        except:
            self.add_error('purchase_price','Debe ingresar un valor numerico')  
        return purchase_price