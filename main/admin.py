from django.contrib import admin
from .models import Goals, CompletedGoals, CanseledGoals

# Register your models here.

admin.site.register(Goals)
admin.site.register(CompletedGoals)
admin.site.register(CanseledGoals)