from . import models
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name','email','subject','message']
        

class QuoteForm(ModelForm):
    class Meta:
        model = models.Quote
        fields = ['name','email','phone','message','departure_city','delivery_city', 'weighht','dimension']
        