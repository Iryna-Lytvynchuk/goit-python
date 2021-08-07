from django import forms


class IncomeForm(forms.Form):
    date_income = forms.DateField()
    amount = forms.IntegerField()

class ExpensesForm(forms.Form):
    date_expenses = forms.DateField()
    amount = forms.IntegerField()
    category = forms.MultipleChoiceField()