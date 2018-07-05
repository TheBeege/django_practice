from django.contrib import admin

# Register your models here.
from .models import Document, User

admin.site.register(Document)
admin.site.register(User)
