from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from .models import *



class Visit_form(forms.ModelForm):
    class Meta:
        model = Visit_model
        fields = ['name', 'lastName','natinal_code','age','phone_num','mirid','doctor_choses','doctor_time','Date_Time']
        
        # this function for jalali-date shamsi year...
    def __init__(self, *args, **kwargs):
        super(Visit_form, self).__init__(*args, **kwargs)
        self.fields['Date_Time'] = JalaliDateField(label=('تاریخ'), 
            widget=AdminJalaliDateWidget 
        )
        
        
        

class Search_Form(forms.ModelForm):
        class Meta:
            model = Doctor_model
            fields = ['name']
        