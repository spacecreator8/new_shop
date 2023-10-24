from django.contrib import admin
from demo.models import *


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)

