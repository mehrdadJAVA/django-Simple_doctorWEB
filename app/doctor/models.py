from django.db import models
from jalali_date import datetime2jalali



class Doctor_model(models.Model):
    name = models.CharField(max_length=100,null=False)
    lastName = models.CharField(max_length=100, null=False)
    
    one1 = 1
    tow2 = 2 
    status2 = ((one1,'پوست و مو'),(tow2,'داخلی'))       
    Specialty = models.IntegerField(choices=status2)
    Data_time_Doctor_come = models.DateTimeField()
    Data_time_Doctor_come1 = models.DateTimeField()
    Data_time_Doctor_come2 = models.DateTimeField()
    
    price1 = 1
    price2 = 2
    price3 = 3
    price4 = 4
    doctor_price_status = ((price1,'4000000'),(price2,'5000000'),(price3,'6000000'),(price4,'سه 7000000'))
    visit_price =  models.IntegerField(choices=doctor_price_status)
    doctor_img = models.ImageField(upload_to='media/')
    
    def _Data_time_Doctor_come(self):
        return datetime2jalali(self.Data_time_Doctor_come.date())
    def _Data_time_Doctor_come1(self):
        return datetime2jalali(self.Data_time_Doctor_come1.date())
    def _Data_time_Doctor_come2(self):
        return datetime2jalali(self.Data_time_Doctor_come2.date())
    
    
    
    @property
    def _Data_time_Doctor_come(self):
        return datetime2jalali(self.Data_time_Doctor_come)
    @property
    def _Data_time_Doctor_come1(self):
        return datetime2jalali(self.Data_time_Doctor_come1)
    @property
    def _Data_time_Doctor_come2(self):
        return datetime2jalali(self.Data_time_Doctor_come2)
    
    def __str__(self) :
        return self.lastName


class Nurse_Model (models.Model):
    nurse_Nmae = models.CharField(max_length=100)
    nurse_Lastname = models.CharField(max_length=1000)
    natinalCode = models.CharField(max_length=100)
    nurse_img = models.ImageField(upload_to='media/')
    
    def __str__(self) :
        return self.nurse_Lastname




class Visit_model(models.Model):
    name = models.CharField(max_length=100,null=False)
    lastName = models.CharField(max_length=100,null=False)
    natinal_code = models.CharField(max_length=100,null=False)
    age = models.IntegerField()
    phone_num = models.CharField(max_length=100)
    mirid = models.BooleanField()
    doctor_choses =  models.ForeignKey(Doctor_model, on_delete=models.SET_NULL, null=True)
    
      
    one = 1
    tow = 2
    there = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight= 8 
    nin = 9
    ten = 10
    eleven = 11 
    towvelv = 12 
    thrertiin = 13 
    foutteen = 14
    fiftin = 15
    sixtiin = 16
    seventeen = 17
    eighteen = 18
    ninteen = 19
    toventy = 20
    towntyone = 21
    doctor_status = ((one,'08:00'),(tow,'09:00'),(there,'10:00'),(four,'11:00'),(five,'12:00'),
              (six,'13:00'),(seven,'14:00'),(eight,'15:00'),(nin,'16:00'),(ten,'17:00'),(eleven,'18:00')
              ,(towvelv,'19:00'),(thrertiin,'20:00'),(foutteen,'21:00'))
    
    doctor_time = models.IntegerField(choices=doctor_status)
    Date_Time = models.DateTimeField()
    
    def Date_Time1(self):
        return datetime2jalali(self.Date_Time)
    
    @property
    def Date_Time1(self):
        return datetime2jalali(self.Date_Time)
    
    
    def __str__(self):
        return self.natinal_code
    

    