from django import forms
from .models import Expense
from django.utils import timezone

class ExpenseForm(forms.ModelForm):
    # pub_date = forms.DateTimeField(widget=forms.SelectDateWidget(), initial=timezone.localtime(timezone.now()).today(), label='Paid date')
    pub_date = forms.DateTimeField(initial=timezone.localtime(timezone.now()), label='Paid date')
    class Meta:
        model = Expense
        fields = ('title', 'price', 'pub_date')
        