
from django.contrib import admin
from .models import UserProfile, Wallet, Transaction

admin.site.register(UserProfile)
admin.site.register(Wallet)
admin.site.register(Transaction)
