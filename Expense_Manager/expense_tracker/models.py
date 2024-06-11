from django.db import models


class Register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    username = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    passwd = models.CharField(max_length=40)
    phone = models.IntegerField(default=0)
    dob = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)

    def __str__(self):
        return self.fname


class Myexpense(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=70)
    category = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    update_date = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Mybudget(models.Model):
    username = models.CharField(max_length=70)
    category = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    remain_amount = models.CharField(max_length=200, default="1000")

    def __str__(self):
        return self.category


class Notification(models.Model):
    username = models.CharField(max_length=70)
    date = models.CharField(max_length=200)
    notify = models.CharField(max_length=400)

    def __str__(self):
        return self.notify
