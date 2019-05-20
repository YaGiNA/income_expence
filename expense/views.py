from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Expense


def index(request):
    latest_expense_list = Expense.objects.order_by('-pub_date')[:5]
    context = {
        'latest_expense_list': latest_expense_list,
    }
    return render(request, 'expense/index.html', context)

def detail(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    return render(request, 'expense/detail.html', {'expense': expense})