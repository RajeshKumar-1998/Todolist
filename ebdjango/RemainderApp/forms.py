from django import forms

class Todoform(forms.Form):
    chars = forms.CharField(max_length=40,
                           widget= forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'Remainder@list' , 'aria-label' : 'Rem', 'aria-describedby' : 'add-btn' }))