from django.contrib import admin
from django.contrib.auth.models import User
from fabrica_needs.models import Entry, Outflow, Product, Wallet

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('amount', 'donor')
    search_fields = ('amount','donor')
    list_filter = ('donor',)
    ordering = ('donor',)

@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ('amount',)
    search_fields = ('amount',)
    list_filter = ('amount',)
    ordering = ('amount',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'amount')
    search_fields = ('name', 'amount')
    list_filter = ('name', 'amount')
    ordering = ('name', 'amount')

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('balance',)
    search_fields = ('balance',)
    list_filter = ('balance',)
    ordering = ('balance',)