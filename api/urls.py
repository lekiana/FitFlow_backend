from django.urls import include, path
from .views.budget_entry_views import *
from .views.budget_views import *
from .views.company_views import *
from .views.group_views import *
from .views.means_views import *
from .views.transaction_category_views import *
from .views.user_views import *
from .views.transaction_views import *
from .views.app_views import *
from .views.standing_order_views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'currency', CurrencyViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'means', MeansViewSet)
router.register(r'budget', BudgetViewSet)
router.register(r'transactiontype', TransactionTypeViewSet)
router.register(r'transactioncategory', TransactionCategoryViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'budgetentry', BudgetEntryViewSet)
router.register(r'standingorder', StandingOrderViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

    # transactions_views #
    path('company_transactions', get_company_transactions),
    path('add_transaction', add_transaction),
    path('delete_transaction', delete_transaction),
    path('get_category_transactions', get_category_transactions),
    path('get_sum', get_sum),
    path('get_available_means', get_available_means),

    # users_views #
    path('company_users', get_company_users),
    path('authenticate_user', authenticate_user),
    path('create_user', create_user),
    path('delete_user', delete_user),

    # company_views #
    path('create_company', create_company),
    
    # group_views #
    path('create_group', create_group),

    # budget_entry_views #
    path('company_budget', get_budget_entries),
    path('add_budget_entry', add_budget_entry),
    path('delete_budget_entry', delete_budget_entry),
    path('get_planned_profit', get_planned_profit),

    # transaction_category_views #
    path('transactions_categories', get_transactions_categories),
    path('get_type_categories', get_type_categories),
    path('add_category', add_category),

    # means_views #
    path('company_means', get_company_means),
    path('add_account', add_account),

    # budget_views #
    path('company_budgets', get_company_budgets),
    path('add_budget', add_budget),

    # standing_order_views #
    path('get_standing_orders', get_standing_orders),
    path('get_standing_orders_sum', get_standing_orders_sum),
    path('update_standing_order', update_standing_order),
    path('delete_standing_order', delete_standing_order),
    path('add_standing_order', add_standind_order),
]