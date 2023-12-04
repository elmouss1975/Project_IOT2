from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
from .models import Dht11

admin.site.register(Dht11)
