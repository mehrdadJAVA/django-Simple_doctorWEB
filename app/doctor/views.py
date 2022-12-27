from django.shortcuts import render
from django.db.models import Q
from .models import *
from .forms import *
from jalali_date import datetime2jalali
import datetime
from django.contrib import messages


def Home_View(request):
    List =[]
    form = Search_Form()
    if request.method == 'POST':
        form = Search_Form(request.POST)
        if form.is_valid():
            for i in form:
                List.append(i.data)
                print(List)
                try :
                    Doctor_model_Data = Doctor_model.objects.get(lastName = str(i.data))  
                    print('77777777777777777777777777')
        
                     
                    
                    Price = ''
                    Specialty = ''
                    if  Doctor_model_Data.visit_price == 1:
                        Price = '4000000'
                    if  Doctor_model_Data.visit_price == 2:
                        Price = '5000000'
                    if  Doctor_model_Data.visit_price == 3:
                        Price = '6000000'
                    if  Doctor_model_Data.visit_price == 4:
                        Price = '7000000'
                        
                    if Doctor_model_Data.Specialty == 1:
                        Specialty = 'پوست مو'
                    if Doctor_model_Data.Specialty == 2:
                        Specialty = 'داخلی'
                    
                    
                    Doctor_model_Data.doctor_img
                    c1 = str(Doctor_model_Data.Data_time_Doctor_come)
                    c2 = str(Doctor_model_Data.Data_time_Doctor_come1)
                    c3 = str(Doctor_model_Data.Data_time_Doctor_come2)
                    come1 =c1[0:10]  
                    come2 = c2[0:10]
                    come3 = c3[0:10]
                    con ={'form':form,'name':Doctor_model_Data.name,'lastname':Doctor_model_Data.lastName,
                                              'Specialty':Specialty,'come1':come1,
                                              'come3':come3,'come2':come2,
                                              'price':Price,'doctor_img':Doctor_model_Data.doctor_img}
                    print(i.data)
                    return render(request,'doctor/search.html',con )
                except:
                    messages.success(request,(' tjikl;gr '))
                    return render(request,'doctor/index.html',{'form':form})

            else:
                messages.success(request,('پیدا نشد'))

                return render(request,'doctor/index.html',{'form':form})
                

    return render(request,'doctor/index.html',{'form':form})


# ----- وزیت کاربر ------- #
def Visit_View(request):
    today = datetime.datetime.now()
    today_now = datetime2jalali(today)
    List = []
    Counter = 0
    Time_Visit = 'n' 
    form = Visit_form()
    if request.method == 'POST':
        form = Visit_form(request.POST)
        if form.is_valid():
            for i in form:
                List.append(i.data)
            print(List )
            # Check_1 = Visit_model.objects.filter(doctor_time = List[7],
            #                                      Date_Time =List[8],doctor_choses_id = List[6])     
            Check_1 = Visit_model.objects.all()
            print(List[6],List[7],List[8])
            if Check_1 is not None:
                for j in Check_1:
                    year = datetime2jalali(j.Date_Time)
                    f = str(year)
                    data = f[0:10]
                    Dt=j.doctor_time 
                    Dc= j.doctor_choses
                    DRt = Doctor_model.objects.get(id = List[6])
                    print(int(List[6])==int(DRt.id))
                    if data == str(List[8]):
                        if int(Dt) == int(List[7]):
                            if  int(DRt.id) == int(List[6]):
                                Counter = Counter + 1
                                print(Counter)
                                if Counter == 3 :   
                                    return render(request ,'doctor/error.html',{})
                
                else:
                    
                    Doctor_model_ = Doctor_model.objects.get(id =List[6])                    
                    if Doctor_model_:
                        User_date = str(List[8])
                        
                        Date_1=str(Doctor_model_.Data_time_Doctor_come.date())
                        Date_2=str(Doctor_model_.Data_time_Doctor_come1.date())
                        Date_3=str(Doctor_model_.Data_time_Doctor_come2.date())
                        print(Date_2,Date_1,Date_3)
                        if Date_1 == User_date:
                            form.save()
                            name = List[0]
                            Lastname = List[1]
                            natinal_code = List[2]
                            doctor_name = Doctor_model.objects.get(id = List[6])
                            Time_come = int(List[7])

                            Tm_8 = '8:00'
                            Tm_9 = '9:00'
                            Tm_10 = '10:00'
                            Tm_11 = '11:00'
                            Tm_12 = '12:00'
                            Tm_13 = '13:00'
                            Tm_14 = '14:00'
                            Tm_15 = '15:00' 
                            Tm_16 = '16:00'
                            Tm_17 = '17:00'
                            Tm_18 = '18:00' 
                            Tm_19 = '19:00' 
                            Tm_20 = '20:00' 
                            Tm_21 = '21:00'
                            
                            if Time_come == 1:
                                Time_Visit = Tm_8
                            if Time_come == 2:
                                Time_Visit = Tm_9
                            if Time_come == 3:
                                Time_Visit = Tm_10
                            if Time_come == 4:
                                Time_Visit = Tm_11
                            if Time_come == 5:
                                Time_Visit = Tm_12
                            if Time_come == 6:
                                Time_Visit = Tm_13
                            if Time_come == 7:
                                Time_Visit = Tm_14
                            if Time_come == 8:
                                Time_Visit = Tm_15   
                            if Time_come == 9:
                                Time_Visit = Tm_16
                            if Time_come == 10:
                                Time_Visit = Tm_17
                            if Time_come == 11:
                                Time_Visit = Tm_18
                            if Time_come == 12:
                                Time_Visit = Tm_19    
                            if Time_come == 13:
                                Time_Visit = Tm_20
                            if Time_come == 14:
                                Time_Visit = Tm_21
                            
                            Price = ''
                            if  doctor_name.visit_price == 1:
                                 Price = '4000000'
                            if  doctor_name.visit_price == 2:
                                Price = '5000000'
                            if  doctor_name.visit_price == 3:
                                Price = '6000000'
                            if  doctor_name.visit_price == 4:
                                Price = '7000000'
                                                      
                            
                            print('Data is saved . . . ')
                            return render(request,'doctor/visit_OK.html',{'date_now':today_now.date(),'price':Price,'time':Time_Visit,'day':Date_1,'doctor_name':doctor_name.lastName,'name':name,'lastname':Lastname,'natinal_code':natinal_code})
                        
                        
                        
                        if Date_2 == User_date:
                            form.save()
                            name = List[0]
                            Lastname = List[1]
                            natinal_code = List[2]
                            doctor_name = Doctor_model.objects.get(id = List[6])
                            Time_come = int(List[7])
   
                                
                            
                            Tm_8 = '8:00'
                            Tm_9 = '9:00'
                            Tm_10 = '10:00'
                            Tm_11 = '11:00'
                            Tm_12 = '12:00'
                            Tm_13 = '13:00'
                            Tm_14 = '14:00'
                            Tm_15 = '15:00' 
                            Tm_16 = '16:00'
                            Tm_17 = '17:00'
                            Tm_18 = '18:00' 
                            Tm_19 = '19:00' 
                            Tm_20 = '20:00' 
                            Tm_21 = '21:00'
                            
                            if Time_come == 1:
                                Time_Visit = Tm_8
                            if Time_come == 2:
                                Time_Visit = Tm_9
                            if Time_come == 3:
                                Time_Visit = Tm_10
                            if Time_come == 4:
                                Time_Visit = Tm_11
                            if Time_come == 5:
                                Time_Visit = Tm_12
                            if Time_come == 6:
                                Time_Visit = Tm_13
                            if Time_come == 7:
                                Time_Visit = Tm_14
                            if Time_come == 8:
                                Time_Visit = Tm_15   
                            if Time_come == 9:
                                Time_Visit = Tm_16
                            if Time_come == 10:
                                Time_Visit = Tm_17
                            if Time_come == 11:
                                Time_Visit = Tm_18
                            if Time_come == 12:
                                Time_Visit = Tm_19    
                            if Time_come == 13:
                                Time_Visit = Tm_20
                            if Time_come == 14:
                                Time_Visit = Tm_21
                            
                            
                            Price = ''
                            if  doctor_name.visit_price == 1:
                                 Price = '4000000'
                            if  doctor_name.visit_price == 2:
                                Price = '5000000'
                            if  doctor_name.visit_price == 3:
                                Price = '6000000'
                            if  doctor_name.visit_price == 4:
                                Price = '7000000'
                                                      
                            
                            print('Data is saved . . . ')
                            return render(request,'doctor/visit_OK.html',{'date_now':today_now.date(),'price':Price,'time':Time_Visit,'day':Date_2,'doctor_name':doctor_name.lastName,'name':name,'lastname':Lastname,'natinal_code':natinal_code})
                        
                        
                        
                        if Date_3 == User_date:
                            form.save()
                            name = List[0]
                            Lastname = List[1]
                            natinal_code = List[2]
                            doctor_name = Doctor_model.objects.get(id = List[6])
                            Time_come = int(List[7])
                            
                            
                            Tm_8 = '8:00'
                            Tm_9 = '9:00'
                            Tm_10 = '10:00'
                            Tm_11 = '11:00'
                            Tm_12 = '12:00'
                            Tm_13 = '13:00'
                            Tm_14 = '14:00'
                            Tm_15 = '15:00' 
                            Tm_16 = '16:00'
                            Tm_17 = '17:00'
                            Tm_18 = '18:00' 
                            Tm_19 = '19:00' 
                            Tm_20 = '20:00' 
                            Tm_21 = '21:00'
                            
                            if Time_come == 1:
                                Time_Visit = Tm_8
                            if Time_come == 2:
                                Time_Visit = Tm_9
                            if Time_come == 3:
                                Time_Visit = Tm_10
                            if Time_come == 4:
                                Time_Visit = Tm_11
                            if Time_come == 5:
                                Time_Visit = Tm_12
                            if Time_come == 6:
                                Time_Visit = Tm_13
                            if Time_come == 7:
                                Time_Visit = Tm_14
                            if Time_come == 8:
                                Time_Visit = Tm_15   
                            if Time_come == 9:
                                Time_Visit = Tm_16
                            if Time_come == 10:
                                Time_Visit = Tm_17
                            if Time_come == 11:
                                Time_Visit = Tm_18
                            if Time_come == 12:
                                Time_Visit = Tm_19    
                            if Time_come == 13:
                                Time_Visit = Tm_20
                            if Time_come == 14:
                                Time_Visit = Tm_21
                            
                            Price = ''
                            if  doctor_name.visit_price == 1:
                                 Price = '4000000'
                            if  doctor_name.visit_price == 2:
                                Price = '5000000'
                            if  doctor_name.visit_price == 3:
                                Price = '6000000'
                            if  doctor_name.visit_price == 4:
                                Price = '7000000'
                                                      
                            
                            
                            print('Data is saved . . . ')
                            return render(request,'doctor/visit_OK.html',{'date_now':today_now.date(),'price':Price,'time':Time_Visit,'day':Date_3,'doctor_name':doctor_name.lastName,'name':name,'lastname':Lastname,'natinal_code':natinal_code})
                            
                       
                                
                        else:
                            Doctor_model_Data = Doctor_model.objects.get(id =List[6]) 
                            Price = ''
                            Specialty = ''
                            if  Doctor_model_Data.visit_price == 1:
                                Price = '4000000'
                            if  Doctor_model_Data.visit_price == 2:
                                Price = '5000000'
                            if  Doctor_model_Data.visit_price == 3:
                                Price = '6000000'
                            if  Doctor_model_Data.visit_price == 4:
                                Price = '7000000'
                                
                            if Doctor_model_Data.Specialty == 1:
                                Specialty = 'پوست مو'
                            if Doctor_model_Data.Specialty == 2:
                                Specialty = 'داخلی'
                            
                            
                            Doctor_model_Data.doctor_img
                            c1 = str(Doctor_model_Data.Data_time_Doctor_come)
                            c2 = str(Doctor_model_Data.Data_time_Doctor_come1)
                            c3 = str(Doctor_model_Data.Data_time_Doctor_come2)
                            come1 =c1[0:10]  
                            come2 = c2[0:10]
                            come3 = c3[0:10]
                            con ={'name':Doctor_model_Data.name,'lastname':Doctor_model_Data.lastName,
                                  'Specialty':Specialty,'come1':come1,
                                  'come3':come3,'come2':come2,
                                  'price':Price,'doctor_img':Doctor_model_Data.doctor_img}
                            
                            return render(request , 'doctor/visit_oder.html',con)         
            else:
                form.save()
    return render(request,'doctor/visit.html',{'form':form})





# ------ مشخصات دکتر ----- #
def Doctor_Del_View(request):
    Doctor = Doctor_model.objects.all()
    
    come1 =''
    come2 =''
    come3 ='' 
    c1 = ''
    c2 = ''
    c3 = ''
    Price = ''
    for i in Doctor:
        c1 = str(i.Data_time_Doctor_come)
        c2 = str(i.Data_time_Doctor_come1)
        c3 = str(i.Data_time_Doctor_come2)
        come1 =c1[0:10]  
        come2 = c2[0:10]
        come3 = c3[0:10]
        Specialty = ''
                              
        if  i.visit_price == 1:
            Price = '4000000'
        if  i.visit_price == 2:
            Price = '5000000'
        if  i.visit_price == 3:
            Price = '6000000'
        if  i.visit_price == 4:
            Price = '7000000'
        if i.Specialty == 1:
            Specialty = 'پوست مو'
        if i.Specialty == 2:
            Specialty = 'داخلی'
            
    con = {'doctor':Doctor,'come1':come1,'come2':come2,'come3':come3,'price':Price,'Specialty':Specialty}
    return render(request,'doctor/doctor_details.html',con)




def Doctor_SRECH_View(request):
    
    form = Search_Form()
    if request.method == 'POST':
        form = Search_Form(request.POST)
        if form.is_valid():
            for i in form:
                
                Doctor_model_Data = Doctor_model.objects.get(lastName = str(i.data)) 
                Price = ''
                Specialty = ''
                if  Doctor_model_Data.visit_price == 1:
                    Price = '4000000'
                if  Doctor_model_Data.visit_price == 2:
                    Price = '5000000'
                if  Doctor_model_Data.visit_price == 3:
                    Price = '6000000'
                if  Doctor_model_Data.visit_price == 4:
                    Price = '7000000'
                    
                if Doctor_model_Data.Specialty == 1:
                    Specialty = 'پوست مو'
                if Doctor_model_Data.Specialty == 2:
                    Specialty = 'داخلی'
                
                
                Doctor_model_Data.doctor_img
                c1 = str(Doctor_model_Data.Data_time_Doctor_come)
                c2 = str(Doctor_model_Data.Data_time_Doctor_come1)
                c3 = str(Doctor_model_Data.Data_time_Doctor_come2)
                come1 =c1[0:10]  
                come2 = c2[0:10]
                come3 = c3[0:10]
    con ={'form':form,'name':Doctor_model_Data.name,'lastname':Doctor_model_Data.lastName,
                                              'Specialty':Specialty,'come1':come1,
                                              'come3':come3,'come2':come2,
                                              'price':Price,'doctor_img':Doctor_model_Data.doctor_img}
    return render(request,'doctor/search.html',con)
            