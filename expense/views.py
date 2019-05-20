from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from .models import Expense
from .form import ExpenseForm
from django.utils import timezone


def index(request):
    today = str(timezone.now()).split('-')
    expenses = Expense.objects.all()
    form = ExpenseForm(request.POST or None)
    context = {
        'year' : today[0],
        'month' : today[1],
        'expenses' : expenses,
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect('expense:index')
    return render(request, 'expense/index.html', context)

def detail(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    return render(request, 'expense/detail.html', {'expense': expense})