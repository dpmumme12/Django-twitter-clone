from django.contrib import admin
from .models import User, profile, post

# Register your models here.

admin.site.register(User)
admin.site.register(profile)
admin.site.register(post)