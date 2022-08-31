from django.contrib import admin
from app_gen.models import Person
# Create your models here.

@admin.register(Person)
class ShowId(admin.ModelAdmin):
    list_display = ('id', 'name','username','email','password','role' )
