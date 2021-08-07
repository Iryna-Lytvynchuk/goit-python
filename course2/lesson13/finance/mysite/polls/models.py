from django.db import models
from django.db.models.deletion import CASCADE
 
 
class Post(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text[:50]

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"

class Income(models.Model):
    data_income = models.DateField()
    amount = models.IntegerField()

class Expenses(models.Model):
    data_expenses = models.DateField()
    amount = models.IntegerField()
    category = models.ManyToManyField(Category)

class ExpensesCategory(models.Model):
    expenses_id = models.ForeignKey(Expenses, on_delete = models.CASCADE)
    category_id = models.CharField(Category, max_length=50)