from django.contrib import admin
from main.models import EncryptedPackage, SimplifiedPackage

# Register your models here.
admin.site.register(EncryptedPackage)
admin.site.register(SimplifiedPackage)