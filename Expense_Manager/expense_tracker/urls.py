from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('register/', views.register, name="register"),
    path('tracker/', views.tracker, name="tracker"),
    path('login_check/', views.login_check, name="login_check"),
    path('transaction/', views.transaction, name="transaction"),
    path('budget/', views.budget, name="budget"),
    path('new_expense/', views.new_expense, name="new_expense"),
    path('expense_chart/', views.expense_chart, name="expense_chart"),
    path('ex_tracker/', views.ex_tracker, name="ex_tracker"),
    path('ex_tracker/', views.ex_tracker, name="ex_tracker"),
    path('edit_expense/<int:myid>', views.edit_expense, name="edit_expense"),
    path('delete_expense/<int:myid>', views.delete_expense, name="delete_expense"),

]