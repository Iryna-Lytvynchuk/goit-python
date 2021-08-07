from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post, Income, Expenses, Category, ExpensesCategory
from .forms import IncomeForm, ExpensesForm
 
 
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class CategoryPageView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category_list'
    def get_queryset(self):
        return Category.objects.all()

class AboutPageView(TemplateView):
    template_name = 'about.html'


def index(request):
    incomeform = IncomeForm()
    if request.method == "POST":
        incomeform = IncomeForm(request.POST)
    return render(request, "index.html", {"form": incomeform})


def create(request):
    if request.method == "POST":
        new_income = Income()
        new_income.data_income = request.POST.get("data_income")
        new_income.amount = request.POST.get("amount")
        new_income.save()
    return HttpResponseRedirect("/")

def index_expenses(request):
    expensesform = ExpensesForm()
    if request.method == "POST":
        expensesform = ExpensesForm(request.POST)
    return render(request, "index_expenses.html", {"form": expensesform})


def create_expenses(request):
    if request.method == "POST":
        data_expenses = request.POST.get("data_expenses")
        amount = request.POST.get("amount")
        category = request.POST.getlist('category')
        project = Expenses.objects.get_or_create(data_expenses=data_expenses, amount=amount)

        for itm in category:
            ExpensesCategory.objects.get_or_create(expenses_id = project[0], category_id = str(itm))
    return HttpResponseRedirect("/")


    