from django import forms
from .models import Expense
from django.utils import timezone

class ExpenseForm(forms.ModelForm):
    pub_date = forms.DateTimeField(widget=forms.SelectDateWidget(), initial=timezone.now().today(), label='Paid date')
    class Meta:
        model = Expense
        fields = ('title', 'price', 'pub_date')
        