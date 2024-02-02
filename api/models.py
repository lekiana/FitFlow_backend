from django.db import models
from django.contrib.auth.models import User, Permission, Group
from rest_framework.authtoken.models import Token

transaction_type = [("I", "Income"), ("E", "Expense"), ("T", "Transaction")]


class Currency(models.Model):
    currency = models.CharField(max_length=3, unique=True, null=False)

    def __str__(self):
        return self.currency


class Company(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, unique=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class Means(models.Model):
    name = models.CharField(max_length=50, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False) #źle
    
    def __str__(self):
        return self.name


class Budget(models.Model):
    name = models.CharField(max_length=50, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    
    def __str__(self):
        return self.name


class TransactionType(models.Model):
    name = models.CharField(max_length=1, choices=transaction_type, null=False, unique=True)

    def __str__(self):
        return self.name


class TransactionCategory(models.Model):
    name = models.CharField(max_length=50, null=False)
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    value = models.IntegerField(null=False)
    title = models.CharField(max_length=50, null=False)
    date = models.DateField(null=False)
    means = models.ForeignKey(Means, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(TransactionCategory, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.title
    
class StandingOrder(models.Model):
    value = models.IntegerField(null=False)
    title = models.CharField(max_length=50, null=False)
    due_date = models.DateField(null=False)
    interval = models.IntegerField(null=False)
    means = models.ForeignKey(Means, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(TransactionCategory, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.title


class BudgetEntry(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(TransactionCategory, on_delete=models.PROTECT, null=False)
    value = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.budget} - {self.category}"
    