from django.contrib import admin

# Register your models here.
from .models import Account,BookUpload, BookDisplay

admin.site.register(Account)
admin.site.register(BookUpload)
admin.site.register(BookDisplay)