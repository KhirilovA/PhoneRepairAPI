from django.contrib import admin

from .models import (Request,
                     Invoice)


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_model', 'status')


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('request', )
