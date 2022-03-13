from django.contrib import admin

# Register your models here.
from food.models import Services
from food.models import Checkout

admin.site.register(Services)



admin.site.register(Checkout)