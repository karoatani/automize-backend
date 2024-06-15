from django.contrib import admin
from .models import Person, Debt, Account
# Register your models here.


admin.site.register(Person)
admin.site.register(Debt)
admin.site.register(Account)