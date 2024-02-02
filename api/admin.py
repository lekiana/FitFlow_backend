from django.contrib import admin
from .models import *

admin.site.register(Currency)
admin.site.register(Company)
admin.site.register(Means)
admin.site.register(Budget)
admin.site.register(TransactionType)
admin.site.register(TransactionCategory)
admin.site.register(Transaction)
admin.site.register(BudgetEntry)
admin.site.register(StandingOrder)