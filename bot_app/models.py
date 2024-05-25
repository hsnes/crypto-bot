# bot_app/models.py
from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet

class UserProfile(models.Model):
    user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    private_key = models.BinaryField()

    def save(self, *args, **kwargs):
        # Encrypt the private key before saving
        fernet = Fernet(settings.CRYPTO_KEY)
        self.private_key = fernet.encrypt(self.private_key)
        super().save(*args, **kwargs)

    def get_private_key(self):
        # Decrypt the private key when accessing it
        fernet = Fernet(settings.CRYPTO_KEY)
        return fernet.decrypt(self.private_key)

class Wallet(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    currency = models.CharField(max_length=10)
    balance = models.DecimalField(max_digits=20, decimal_places=8)

class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=4, choices=[('buy', 'Buy'), ('sell', 'Sell')])
    currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField(auto_now_add=True)
