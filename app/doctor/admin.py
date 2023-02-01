from django.contrib import admin
from .models import *

# this 3 class with admin dateils view

class doctor_admin(admin.ModelAdmin):
    list_display = ('name','lastName','visit_price')


class nurse_admin(admin.ModelAdmin):
    list_display = ('nurse_Nmae','nurse_Lastname','natinalCode')


class visit_admin(admin.ModelAdmin):
    list_display = ('lastName','natinal_code','phone_num','doctor_time','Date_Time')




admin.site.register(Doctor_model,doctor_admin)
admin.site.register(Nurse_Model,nurse_admin)
admin.site.register(Visit_model,visit_admin)


