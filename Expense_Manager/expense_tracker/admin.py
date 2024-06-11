from django.contrib import admin

from .models import Register, Myexpense, Mybudget, Notification

admin.site.register(Register)
admin.site.register(Myexpense)
admin.site.register(Mybudget)
admin.site.register(Notification)


