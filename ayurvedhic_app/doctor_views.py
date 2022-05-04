from django.shortcuts import render
from django.views.generic import TemplateView

from ayurvedhic_app.models import medicine, doctor, pharmacy, booking, prescription, prescriptionTopharmacy


class index_view(TemplateView):
    template_name = 'doctor/doctor_index.html'

class view_users(TemplateView):
    template_name = 'doctor/view_user.html'
    def get_context_data(self, **kwargs):
        context = super(view_users,self).get_context_data(**kwargs)
        DOCTOR = doctor.objects.get(user_id= self.request.user.id)
        BOOKING = booking.objects.filter(doctor_id__category=DOCTOR.category,status='consulted')
        context['BOOKING']=BOOKING
        Pharmacy=pharmacy.objects.all()
        context['Pharmacy']=Pharmacy
        return context
    def post(self,request,*args,**kwargs):
        DOCTOR = doctor.objects.get(user_id= self.request.user.id)
        BOOKING = booking.objects.filter(doctor_id__category=DOCTOR.category,status='sent to pharmacy')
        Pharmacys=pharmacy.objects.all()
        id = request.POST['id']
        print(id)
        Pharmacy =request.POST['pharmacy']

        if Pharmacy=='null':
            return render(request, 'doctor/doctor_index.html',{'messages':'select any pharmacy'})
        else:
            print(Pharmacy)
            PHARMACY= prescriptionTopharmacy()
            PHARMACY.doctor_id_id=DOCTOR.id
            PHARMACY.PARMACY_id_id= Pharmacy
            PHARMACY.Booking_id= id
            PHARMACY.status = "sent to pharmacy"
            BOOKINGs = booking.objects.get(id=id)
            BOOKINGs.status = 'sent to pharmacy'
            BOOKINGs.save()
            PHARMACY.save()
            return render(request, 'doctor/view_user.html',{'BOOKING':BOOKING,'Pharmacy':Pharmacys})



class view_medicine(TemplateView):
    template_name = 'doctor/view_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(view_medicine,self).get_context_data(**kwargs)
        Medicine=medicine.objects.all()
        Doctor=doctor.objects.filter(status='accepted')
        context['Doctor']=Doctor
        context['Medicine']=Medicine
        return context

class view_pharmacy(TemplateView):
    template_name = 'doctor/view_pharmacy.html'
    def get_context_data(self, **kwargs):
        context = super(view_pharmacy,self).get_context_data(**kwargs)
        Pharmacy=pharmacy.objects.all()
        Doctor=doctor.objects.filter(status='accepted')
        context['Doctor']=Doctor
        context['Pharmacy']=Pharmacy
        return context

class view_booking(TemplateView):
    template_name = 'doctor/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(view_booking,self).get_context_data(**kwargs)
        DOCTOR = doctor.objects.get(user_id= self.request.user.id)
        BOOKING = booking.objects.filter(doctor_id__category=DOCTOR.category,status='booking confirm')
        context['BOOKING']=BOOKING
        return context

class view_prescription(TemplateView):
    template_name = 'doctor/doctor_prescription.html'
    def get_context_data(self, **kwargs):
        context = super(view_prescription,self).get_context_data(**kwargs)
        Medicine=medicine.objects.all()
        id =self.request.GET['id']
        context['Medicine']=Medicine
        context['id']=id
        return context

    def post(self,request,*args,**kwargs):
        id =request.POST['id']

        Symptoms = request.POST['Symptoms']
        print(Symptoms)
        Tests = request.POST['Tests']
        print(Tests)
        advice = request.POST['advice']
        print(advice)
        med1 = request.POST['med1']
        print(med1)
        if med1=='null':
            MED1='0'
        else:
            MED1= medicine.objects.get(id=med1)

        time1 = request.POST['time1']
        print(time1)
        food1 = request.POST['food1']
        print(food1,"11111111111")
        quantity1 = request.POST['Quantity1']
        print(quantity1)

        med2 = request.POST['med2']
        print(med2)
        if med2 == 'null':
            MED2='0'
        else:
            MED2= medicine.objects.get(id=med2)
        time2 = request.POST['time2']
        print(time2)
        food2 = request.POST['food2']
        print(food2)
        quantity2 = request.POST['Quantity2']
        print(quantity2)

        med3 = request.POST['med3']

        print("5555555555555555555555555555555555555555",med3)
        if med3=='null':
            MED3='0'
        else:
            MED3= medicine.objects.get(id=med3)
        time3 = request.POST['time3']
        print(time3)
        food3 = request.POST['food3']
        print(food3)
        quantity3 = request.POST['Quantity3']
        print(quantity3)

        med4 = request.POST['med4']
        print(med4)
        if med4 =='null':
            MED4 ='0'
        else:
            MED4= medicine.objects.get(id=med4)
        time4 = request.POST['time4']
        print(time4)
        food4 = request.POST['food4']
        print(food4)
        quantity4 = request.POST['Quantity4']
        print(quantity4)

        med5 = request.POST['med5']
        print(med5)
        if med5 == 'null':
            MED5 = '0'
        else:
            MED5= medicine.objects.get(id=med5)
        time5 = request.POST['time5']
        print(time5)
        food5 = request.POST['food5']
        print(food5)
        quantity5 = request.POST['Quantity5']
        print(quantity5)

        med6 = request.POST['med6']
        print(med6)

        if med6 == 'null':
            MED6='0'
        else:
            MED6= medicine.objects.get(id=med6)
        time6 = request.POST['time6']
        print(time6)
        food6 = request.POST['food6']
        print(food6)
        quantity6 = request.POST['Quantity6']
        print(quantity6)

        med7= request.POST['med7']
        print(med7)
        if med7=='null':
            MED7 = '0'
        else:
            MED7= medicine.objects.get(id=med7)
        time7 = request.POST['time7']
        print(time7)
        food7 = request.POST['food7']
        print(food7)
        quantity7 = request.POST['Quantity7']
        print(quantity7)


        med8 = request.POST['med8']
        print(med8)
        if med8 =='null':
            MED8='0'
        else:
            MED8= medicine.objects.get(id=med8)
        time8 = request.POST['time8']
        print(time8)
        food8 = request.POST['food8']
        print(food8)
        quantity8 = request.POST['Quantity8']
        print(quantity8)

        med9 = request.POST['med9']
        print(med9)
        if med9 == 'null':
            MED9='0'
        else:
            MED9= medicine.objects.get(id=med9)
        time9 = request.POST['time9']
        print(time9)
        food9 = request.POST['food9']
        print(food9)
        quantity9 = request.POST['Quantity9']
        print(quantity9)

        Prescription =prescription()
        Prescription.Booking_id = id
        Prescription.symptoms = Symptoms
        Prescription.test = Tests
        Prescription.advice = advice

        Prescription.medicine_name1= med1
        if quantity1=='':
            Prescription.Quantity1= 0
        else:
            Prescription.Quantity1= quantity1
        Prescription.time1= time1
        Prescription.food_time1= food1
        if MED1=='0':
            Prescription.medicine1= '0'
        else:
            Prescription.medicine1 = MED1.med_name

        Prescription.medicine_name2= med2
        if quantity2=='':
            Prescription.Quantity2= 0
        else:
            Prescription.Quantity2= quantity2
        Prescription.time2= time2
        Prescription.food_time2= food2

        if MED2=='0':
            Prescription.medicine3= '0'
        else:
            Prescription.medicine3 = MED2.med_name

        Prescription.medicine_name3= med3
        if quantity3=='':
            Prescription.Quantity3= 0
        else:
            Prescription.Quantity3= quantity3
        Prescription.time3= time3
        Prescription.food_time3= food3
        if MED3=='0':
            Prescription.medicine3= '0'
        else:
            Prescription.medicine3 = MED3.med_name



        Prescription.medicine_name4= med4
        if quantity4=='':
            Prescription.Quantity4= 0
        else:
            Prescription.Quantity4= quantity4
        Prescription.time4= time4
        Prescription.food_time4= food4
        if MED4=='0':
            Prescription.medicine4= '0'
        else:
            Prescription.medicine4 = MED4.med_name



        Prescription.medicine_name5= med5
        if quantity5=='':
            Prescription.Quantity5= 0
        else:
            Prescription.Quantity5= quantity5
        Prescription.time5= time5
        Prescription.food_time5= food5
        if MED5=='0':
            Prescription.medicine5= '0'
        else:
            Prescription.medicine5 = MED5.med_name




        Prescription.medicine_name6= med6
        if quantity6=='':
            Prescription.Quantity6= 0
        else:
            Prescription.Quantity6= quantity6
        Prescription.time6= time6
        Prescription.food_time6= food6
        if MED6=='0':
            Prescription.medicine6= '0'
        else:
            Prescription.medicine6 = MED6.med_name



        Prescription.medicine_name7= med7
        if quantity7=='':
            Prescription.Quantity7= 0
        else:
            Prescription.Quantity7= quantity7
        Prescription.time7= time7
        Prescription.food_time7= food7
        if MED7=='0':
            Prescription.medicine7= '0'
        else:
            Prescription.medicine7 = MED7.med_name

        Prescription.medicine_name8= med8
        if quantity8=='':
            Prescription.Quantity8= 0
        else:
            Prescription.Quantity8= quantity8
        Prescription.time8= time8
        Prescription.food_time8= food8
        if MED8=='0':
            Prescription.medicine8= '0'
        else:
            Prescription.medicine8 = MED8.med_name

        Prescription.medicine_name9= med9
        if quantity9=='':
            Prescription.Quantity9= 0
        else:
            Prescription.Quantity9= quantity9
        Prescription.time9= time9
        Prescription.food_time9= food9
        if MED9=='0':
            Prescription.medicine9= '0'
        else:
            Prescription.medicine9 = MED9.med_name

        Booking =booking.objects.get(id=id)
        Booking.status='consulted'
        Booking.save()
        Prescription.save()
        return render(request, 'doctor/doctor_index.html',{'messages':'prescription Sent successfully'})


class view_consulted_users_list(TemplateView):
    template_name = 'doctor/user_consulted_prescription_list.html'
    def get_context_data(self, **kwargs):
        context = super(view_consulted_users_list,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        BOOKING = booking.objects.get(id=id,status='consulted')
        Prescription = prescription.objects.get(Booking_id = BOOKING.id)
        context['Prescription']=Prescription

        return context

class prescription_sended_list(TemplateView):
    template_name = 'doctor/prescription_sended_list.html'
    def get_context_data(self, **kwargs):
        context = super(prescription_sended_list,self).get_context_data(**kwargs)
        DOCTOR = doctor.objects.get(user_id= self.request.user.id)
        BOOKING =prescriptionTopharmacy.objects.filter(doctor_id__category=DOCTOR.category,status='sent to pharmacy')
        context['BOOKING'] =BOOKING
        return context

class view_consulted_users_list_send_parmacy(TemplateView):
    template_name = 'doctor/user_consulted_prescription_list.html'
    def get_context_data(self, **kwargs):
        context = super(view_consulted_users_list_send_parmacy,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        BOOKING = booking.objects.get(id=id,status='sent to pharmacy')
        Prescription = prescription.objects.get(Booking_id = BOOKING.id)
        context['Prescription']=Prescription
        return context