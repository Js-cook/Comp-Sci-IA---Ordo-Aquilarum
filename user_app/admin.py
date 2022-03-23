from django.contrib import admin
from .models import Question, CustomUser

# Register your models here.
admin.site.register(Question)
admin.site.register(CustomUser)