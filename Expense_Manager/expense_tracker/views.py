from datetime import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Register, Myexpense, Mybudget, Notification
from django.contrib.auth import authenticate, login, logout


# from rest_framework.authtoken.admin import User


def home(request):
    return render(request, 'welcome.html')


def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        passwd = request.POST['password']
        phone = request.POST['phone']
        dob = request.POST['dob']
        gender = request.POST['gender']

        user = User.objects.create_user(username, email, passwd)
        user.save()
        reg = Register(fname=fname, lname=lname, username=username, email=email, passwd=passwd, phone=phone, dob=dob,
                       gender=gender)
        reg.save()
        return redirect('/expense/tracker')
    return render(request, 'register.html')


def login_check(request):
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST['password']
        us = authenticate(username=username, password=passwd)
        if us is not None:
            login(request, us)
            messages.success(request, "Successfully logged in")
            return redirect('/expense/tracker/')

        else:
            messages.error(request, "Wrong password or user_id")
            return redirect('/expense/login_check/')

    return render(request, 'login.html')


def tracker(request):
    username = request.user.username
    myexp = Myexpense.objects.filter(username=username)
    mybudg = Mybudget.objects.filter(username=username)
    length = len(myexp)
    cur_exp = 0
    tot_budg = 0
    for bud in mybudg:
        tot_budg += int(bud.amount)

    for exp in myexp:
        cur_exp += int(exp.amount)
    percent = 0
    if cur_exp < tot_budg:
        percent = (cur_exp / tot_budg) * 100
    else:
        percent = 100
    notify = Notification.objects.filter(username=username)
    notification = []
    for noty in notify:
        d = {'username': noty.username, 'date': noty.date, 'notify': noty.notify}
        notification.append(d)
    if len(notification)>4:
        notification = notification[:4]

    myexp_list = []
    if length > 6:
        for exp in myexp:
            d = {'category': exp.category, 'date': exp.date, 'desc': exp.desc, 'amount': exp.amount,
                 'update_date': exp.update_date}
            myexp_list.append(d)
        myexp_list = myexp_list[-6:]
        myexp_list = myexp_list[::-1]
    else:
        for exp in myexp:
            d = {'category': exp.category, 'date': exp.date, 'desc': exp.desc, 'amount': exp.amount,
                 'update_date': exp.update_date}
            myexp_list.append(d)
        myexp_list = myexp_list[::-1]

    return render(request, 'tracker.html', {'myexp_list': myexp_list, 'percent': percent, 'notification':notification})


def transaction(request):
    username = request.user.username
    myexp = Myexpense.objects.filter(username=username)

    return render(request, 'transaction.html', {'myexp': myexp})


def budget(request):
    if request.method == "POST":
        username = request.user.username
        category = request.POST.get('cat', '')
        amount = request.POST.get('amount', '')
        remain_amount = amount
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        date = dt_string
        mybudget = Mybudget(username=username, category=category, date=date, amount=amount, remain_amount=remain_amount)
        mybudget.save()

    username = request.user.username
    budget = Mybudget.objects.filter(username=username)

    return render(request, 'budget.html', {'budget': budget})


def new_expense(request):
    if request.method == "POST":
        username = request.user.username
        category = request.POST.get('cat', '')
        date_of_expense = request.POST.get('date')
        desc = request.POST.get('desc', '')
        amount = request.POST.get('expense')
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        updated_at = dt_string
        finance = Myexpense(username=username, category=category, date=date_of_expense, desc=desc, amount=amount,
                            update_date=updated_at)

        finance.save()
        notify = Notification(username=username, date=dt_string, notify="Expense Addedd!!!")
        notify.save()
        return redirect('/expense/transaction/')


def expense_chart(request):
    category = ['Health', 'Electronics', 'Travel', 'Education', 'Others']
    username = request.user.username
    dict_myexp = {}

    for cat in category:
        myexp = Myexpense.objects.filter(username=username, category=cat)
        am = 0
        for exp in myexp:
            am += int(exp.amount)
        dict_myexp[cat] = am

    return render(request, 'expense_chart.html', context={'dict_myexp': dict_myexp})


def ex_tracker(request):
    return render(request, 'ex_tracker.html')


def edit_expense(request, myid):
    if request.method == "POST":
        username = request.user.username
        finance = Myexpense.objects.get(id=myid)
        # finance.name = request.POST.get('name' + str(myid), '')
        finance.desc = request.POST.get('desc' + str(myid), '')
        finance.category = request.POST.get('cat' + str(myid))
        finance.date = request.POST.get('date' + str(myid))
        finance.amount = request.POST.get('expense' + str(myid))
        finance.username = request.user.username
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        finance.update_date = dt_string
        finance.save()
        notify = Notification(username=username, date=dt_string, notify="Expense Edited!!!")
        notify.save()
        return redirect('/expense/transaction')


def delete_expense(request, myid):
    if request.method == "POST":
        username = request.user.username
        finance = Myexpense.objects.get(id=myid)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        finance.delete()
        notify = Notification(username=username, date=dt_string, notify="Expense Deleted!!!")
        notify.save()
        return redirect('/expense/transaction')
