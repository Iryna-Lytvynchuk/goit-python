from django.contrib import admin
 
from .models import Post, Income, Expenses, Category
 
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Income)
admin.site.register(Expenses)