from django.db import models
from django.utils import timezone
from cryptography.fernet import Fernet
import base64

class License(models.Model):
    key = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    issue_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return f"{self.product_name} - {self.client_name}"

    def encrypt_key(self):
        """Encrypt the license key for secure storage."""
        cipher_key = Fernet(base64.urlsafe_b64encode(Fernet.generate_key()))
        return cipher_key.encrypt(self.key.encode()).decode('utf-8')

    def decrypt_key(self, encrypted_key):
        """Decrypt the license key."""
        cipher_key = Fernet(base64.urlsafe_b64encode(Fernet.generate_key()))
        return cipher_key.decrypt(encrypted_key.encode()).decode('utf-8')
