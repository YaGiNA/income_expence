from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from .models import Expense
from .form import ExpenseForm
from django.utils import timezone


def index(request):
    today = timezone.now()
    expenses = Expense.objects.all()
    total_price = sum(expense.price for expense in expenses)
    form = ExpenseForm(request.POST or None)
    context = {
        'now': today,
        'expenses' : expenses,
        'form': form,
        'total_price': total_price,
    }
    if form.is_valid():
        form.save()
        return redirect('expense:index')
    return render(request, 'expense/index.html', context)

def detail(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    return render(request, 'expense/detail.html', {'expense': expense})