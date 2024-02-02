from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Company, TransactionCategory, TransactionType

@receiver(post_save, sender=Company)
def add_default_categories(sender, instance, created, **kwargs):
    expense = TransactionType.objects.get(pk=2)
    if created:
        TransactionCategory.objects.create(name='Taxes and fees', company=instance, type=expense)
        TransactionCategory.objects.create(name='Salaries and wages', company=instance, type=expense)
        TransactionCategory.objects.create(name='Loans', company=instance, type=expense)
        TransactionCategory.objects.create(name='Materials', company=instance, type=expense)
        TransactionCategory.objects.create(name='Marketing expenses', company=instance, type=expense)
        TransactionCategory.objects.create(name='Administrative expenses', company=instance, type=expense)
