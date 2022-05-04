from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

from ayurvedhic_app.models import medicine, doctor, prescriptionTopharmacy, pharmacy, booking, prescription, \
    give_medicine, users, FEEDBACK


class index_view(TemplateView):
    template_name = 'pharmacy/pharmacy_index.html'


class Medicine(object):
    pass


class add_medicine(TemplateView):
    template_name = 'pharmacy/add_medicine.html'
    def post(self,request,*args,**kwargs):
        name=request.POST['name']
        price =request.POST['price']
        image= request.FILES['photo']
        F = FileSystemStorage()
        IMAGES = F.save(image.name, image)
        quantity = request.POST['quantity']
        description = request.POST['description']
        Medicine = medicine()
        Medicine.user_id=self.request.user.id
        Medicine.med_name =name
        Medicine.med_price = price
        Medicine.photo = IMAGES
        Medicine.quantity =quantity
        Medicine.description = description
        Medicine.status = 'active'
        Medicine.save()
        return  redirect(request.META['HTTP_REFERER'])

    def get_context_data(self, **kwargs):
        context = super(add_medicine,self).get_context_data(**kwargs)
        Medicine=medicine.objects.filter(user_id=self.request.user.id)
        context['Medicine']=Medicine
        return context

class Remove_Medicine(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        medicine.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class Medicine_status(TemplateView):
      template_name = 'pharmacy/view_medicine.html'
      def get_context_data(self, **kwargs):
          context = super(Medicine_status,self).get_context_data(**kwargs)
          Medicine=medicine.objects.filter(user_id=self.request.user.id)
          context['Medicine']=Medicine
          return context

class view_Doctors(TemplateView):
    template_name = 'pharmacy/view_doctors.html'
    def get_context_data(self, **kwargs):
          context = super(view_Doctors,self).get_context_data(**kwargs)
          Doctor=doctor.objects.filter(status='accepted')
          context['Doctor']=Doctor
          return context

class view_Booking(TemplateView):
    template_name = 'pharmacy/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(view_Booking,self).get_context_data(**kwargs)
        Pharmacy = pharmacy.objects.get(user_id= self.request.user.id)
        BOOKING = prescriptionTopharmacy.objects.filter(PARMACY_id_id=Pharmacy.id,status='sent to pharmacy')
        context['BOOKING']=BOOKING
        return context

class view_feedback(TemplateView):
    template_name = 'pharmacy/view_feedback.html'
    def get_context_data(self, **kwargs):
        context = super(view_feedback,self).get_context_data(**kwargs)
        pharmacys = pharmacy.objects.get(user_id=self.request.user.id)
        feeds = FEEDBACK.objects.filter(USER_id=pharmacys.id)
        context['feeds']=feeds
        return context

    def post(self,request,*args,**kwargs):
        feed = request.POST['feed_back']
        user = User.objects.get(id=self.request.user.id)
        pharmacys = pharmacy.objects.get(user_id=user.id)
        feeds = FEEDBACK()
        feeds.USER_id = pharmacys.id
        feeds.feedback = feed
        feeds.save()
        return redirect(request.META['HTTP_REFERER'])

class delete_feedback(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        FEEDBACK.objects.filter(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class view_consulted_users_list_send_parmacy(TemplateView):
    template_name = 'pharmacy/user_consulted_prescription_list.html'
    def get_context_data(self, **kwargs):
        context = super(view_consulted_users_list_send_parmacy,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        BOOKING = booking.objects.get(id=id,status='sent to pharmacy')
        Prescription = prescription.objects.get(Booking_id = BOOKING.id,status='not provide medicine')
        context['Prescription']=Prescription
        return context

    def post(self,request,*args,**kwargs):

        id = request.POST['id']
        TOTAL1=1
        TOTAL2= 2
        TOTAL3=3
        TOTAL4=4
        TOTAL5=5
        TOTAL6=6
        TOTAL7=7
        TOTAL8=8
        TOTAL9=9
        Prescription = prescription.objects.get(id = id)
        SYMPTOM =request.POST['Symptom']
        test = request.POST['Tests']
        Advice =request.POST['advice']

        medicine1 =request.POST['medicine1']
        if medicine1=='null':
            MED1='0'
        else:
            MED1= medicine.objects.get(id=medicine1)
        Quantity1 =request.POST['Quantity1']
        time1 = request.POST['time1']
        food_time1 = request.POST['food_time2']



        medicine2 =request.POST['medicine2']
        if medicine2=='null':
            MED2='0'
        else:
            MED2= medicine.objects.get(id=medicine2)
        Quantity2 =request.POST['Quantity2']
        time2 = request.POST['time2']
        food_time2 = request.POST['food_time2']

        medicine3 =request.POST['medicine3']
        if medicine3=='null':
            MED3='0'
        else:
            MED3= medicine.objects.get(id=medicine3)
        Quantity3 =request.POST['Quantity3']
        time3 = request.POST['time3']
        food_time3 = request.POST['food_time3']


        medicine4 =request.POST['medicine4']
        if medicine4=='null':
            MED4='0'
        else:
            MED4= medicine.objects.get(id=medicine4)
        Quantity4 =request.POST['Quantity4']
        time4 = request.POST['time4']
        food_time4 = request.POST['food_time4']


        medicine5 =request.POST['medicine5']
        if medicine5=='null':
            MED5='0'
        else:
            MED5= medicine.objects.get(id=medicine5)
        Quantity5 =request.POST['Quantity5']
        time5 = request.POST['time5']
        food_time5 = request.POST['food_time5']

        medicine6 =request.POST['medicine6']
        if medicine6=='null':
            MED6='0'
        else:
            MED6= medicine.objects.get(id=medicine6)
        Quantity6 =request.POST['Quantity6']
        time6 = request.POST['time6']
        food_time6 = request.POST['food_time6']


        medicine7 =request.POST['medicine7']
        if medicine7=='null':
            MED7='0'
        else:
            MED7= medicine.objects.get(id=medicine7)
        Quantity7 =request.POST['Quantity7']
        time7 = request.POST['time7']
        food_time7 = request.POST['food_time7']

        medicine8 =request.POST['medicine8']
        if medicine8=='null':
            MED8='0'
        else:
            MED8= medicine.objects.get(id=medicine8)
        Quantity8 =request.POST['Quantity8']
        time8 = request.POST['time8']
        food_time8 = request.POST['food_time8']

        medicine9 =request.POST['medicine9']
        if medicine9=='null':
            MED9='0'
        else:
            MED9= medicine.objects.get(id=medicine9)
        Quantity9 =request.POST['Quantity9']
        time9 = request.POST['time9']
        food_time9 = request.POST['food_time9']



        Give_medicine =give_medicine()
        Give_medicine.Booking_id = Prescription.Booking_id
        Give_medicine.symptoms = SYMPTOM
        Give_medicine.test = test
        Give_medicine.advice = Advice



        if medicine1=="null":
             Give_medicine.medicine_name1= "0"
             Give_medicine.available_status1="not selected"
        else:
            if Quantity1=='':
               Give_medicine.Quantity1= 0
            else:
                Give_medicine.Quantity1= Quantity1
                MEDICINE =medicine.objects.get(id=medicine1)
                print(MEDICINE)
                Give_medicine.total1=int(Quantity1)* int(MEDICINE.med_price)
                TOTAL1 = Give_medicine.total1
                MEDICINE.quantity=int(MEDICINE.quantity) - int(Quantity1)
                print(MEDICINE.quantity,"1111111111111111111111111111111111111111111111111")
                # MEDICINE.save()
                Give_medicine.medicine_name1= medicine1
                if MEDICINE.quantity<=0:
                    Give_medicine.available_status1="out of stock"
                else:
                    MEDICINE.save()
                    Give_medicine.available_status1="available"

                Give_medicine.time1= time1
                Give_medicine.food_time1= food_time1
        if MED1=='0':
            Give_medicine.medicine1= '0'
        else:
            Give_medicine.medicine1 = MED1.med_name




        if medicine2=="null" :
             Give_medicine.medicine_name2= "0"
             Give_medicine.available_status2="not selected"
        else:
            if Quantity2=='':
               Give_medicine.Quantity2= 0
            else:
                Give_medicine.Quantity2= Quantity2
                MEDICINE =medicine.objects.get(id=medicine2)
                print(MEDICINE)
                Give_medicine.total2=int(Quantity2)* int(MEDICINE.med_price)
                TOTAL2 = Give_medicine.total2
                MEDICINE.quantity=int(MEDICINE.quantity) - int(Quantity2)
                print(MEDICINE.quantity,"1111111111111111111111111111111111111111111111111")
                # MEDICINE.save()
                Give_medicine.medicine_name2= medicine2
                if MEDICINE.quantity<=0:
                    Give_medicine.available_status2="out of stock"
                else:
                    MEDICINE.save()
                    Give_medicine.available_status2="available"

                Give_medicine.time2= time2
                Give_medicine.food_time2= food_time2
        if MED2=='0':
            Give_medicine.medicine2= '0'
        else:
            Give_medicine.medicine2 = MED2.med_name




        if medicine3=="null" :
             Give_medicine.medicine_name3= "0"
             Give_medicine.available_status3="not selected"
        else:
            if Quantity3=='':
               Give_medicine.Quantity3= 0
            else:
                Give_medicine.Quantity3= Quantity3
                MEDICINE =medicine.objects.get(id=medicine3)
                print(MEDICINE)
                Give_medicine.total3=int(Quantity3)* int(MEDICINE.med_price)
                TOTAL3 = Give_medicine.total3
                MEDICINE.quantity=int(MEDICINE.quantity) - int(Quantity3)
                # MEDICINE.save()
                Give_medicine.medicine_name3= medicine3
                print(MEDICINE.quantity,"1111111111111111111111111111111111111111111111111")
                if MEDICINE.quantity<=0:
                    Give_medicine.available_status3="out of stock"
                else:
                    MEDICINE.save()
                    Give_medicine.available_status3="available"
                Give_medicine.time3= time3
                Give_medicine.food_time3= food_time3
        if MED3=='0':
            Give_medicine.medicine3= '0'
        else:
            Give_medicine.medicine3 = MED3.med_name



        if medicine4=="null":
             Give_medicine.medicine_name4= "0"
             Give_medicine.available_status4="not selected"
        else:
            if Quantity4=='':
               Give_medicine.Quantity4= 0
            else:
                Give_medicine.Quantity4= Quantity4
                MEDICINE =medicine.objects.get(id=medicine4)
                print(MEDICINE)
                Give_medicine.total4=int(Quantity4)* int(MEDICINE.med_price)
                TOTAL4 = Give_medicine.total4
                MEDICINE.quantity=int(MEDICINE.quantity) - int(Quantity4)
                # MEDICINE.save()
                Give_medicine.medicine_name4= medicine4
                if MEDICINE.quantity<=0:
                    Give_medicine.available_status4="out of stock"
                else:
                    MEDICINE.save()
                    Give_medicine.available_status4="available"
                Give_medicine.time4= time4
                Give_medicine.food_time4= food_time4
        if MED4=='0':
            Give_medicine.medicine4= '0'
        else:
            Give_medicine.medicine4 = MED4.med_name



        if medicine5=="null":
             Give_medicine.medicine_name5= "0"
             Give_medicine.available_status5="not selected"
        else:
            if Quantity5=='':
               Give_medicine.Quantity5= 0
            else:
                Give_medicine.Quantity5= Quantity5
                MEDICINE =medicine.objects.get(id=medicine5)
                print(MEDICINE)
                Give_medicine.total5=int(Quantity5)* int(MEDICINE.med_price)
                TOTAL5 = Give_medicine.total5
                MEDICINE.quantity=int(MEDICINE.quantity) - int(Quantity5)
                # MEDICINE.save()
                Give_medicine.medicine_name5= medicine5
                if MEDICINE.quantity<=0:
                    Give_medicine.available_status5="out of stock"
                else:
                    MEDICINE.save()
                    Give_medicine.available_status5="available"
                Give_medicine.time5= time5
                Give_medicine.food_time1= food_time5
        if MED5=='0':
            Give_medicine.medicine5= '0'
        else:
            Give_medicine.medicine5 = MED5.med_name




        if medicine6=="null"  :
             Give_medicine.medicine_name6= "0"
             Give_medicine.available_status6="not selected"
        else:
            if Quantity6=='':
               Give_medicine.Quantity6= 0
            else:
                Give_medicine.Quantity6= Quantity6
                MEDICINE =medicine.objects.get(id=medicine6)
                print(MEDICINE)
                Give_medicine.total6=int(Quantity6)* int(MEDICINE.med_price)
                TOTAL6 = Give_medicine.total6
                MEDICINE.quantity=int(MEDICINE.quantity) - int(Quantity6)
                # MEDICINE.save()
                Give_medicine.medicine_name6= medicine6
                if MEDICINE.quantity<=0:
                    Give_medicine.available_status6="out of stock"
                else:
                    MEDICINE.save()
                    Give_medicine.available_status6="available"
                Give_medicine.time6= time6
                Give_medicine.food_time6= food_time6
        if MED6=='0':
            Give_medicine.medicine6= '0'
        else:
            Give_medicine.medicine6 = MED6.med_name



        if medicine7=='null':
             Give_medicine.medicine_name7= "0"
             Give_medicine.available_status7="not selected"
        else:
            if Quantity7=='':
               Give_medicine.Quantity7= 0
            else:
                Give_medicine.Quantity1= Quantity7
                MEDICINE =medicine.objects.get(id=medicine7)
                print(MEDICINE)
                Give_medicine.total7=int(Quantity7)* int(MEDICINE.med_price)
                TOTAL7 = Give_medicine.total7
                MEDICINE.quantity=int(MEDICINE.quantity) - int(Quantity7)
                # MEDICINE.save()
                Give_medicine.medicine_name7= medicine7
                if MEDICINE.quantity<=0:
                    Give_medicine.available_status7="out of stock"
                else:
                    MEDICINE.save()
                    Give_medicine.available_status7="available"
                Give_medicine.time7= time7
                Give_medicine.food_time7= food_time7
        if MED7=='0':
            Give_medicine.medicine7= '0'
        else:
            Give_medicine.medicine7 = MED7.med_name



        if medicine8=='null' :
             Give_medicine.medicine_name8= "0"
             Give_medicine.available_status8="not selected"
        else:
            if Quantity8=='':
               Give_medicine.Quantity8= 0
            else:
                Give_medicine.Quantity8= Quantity8
                MEDICINE =medicine.objects.get(id=medicine8)
                print(MEDICINE)
                Give_medicine.total8=int(Quantity8)* int(MEDICINE.med_price)
                TOTAL8 = Give_medicine.total8
                MEDICINE.quantity=int(MEDICINE.quantity) - int(Quantity8)
                # MEDICINE.save()
                Give_medicine.medicine_name8= medicine8
                if MEDICINE.quantity<=0:
                    Give_medicine.available_status8="out of stock"
                else:
                    MEDICINE.save()
                    Give_medicine.available_status8="available"
                Give_medicine.time8= time8
                Give_medicine.food_time8= food_time8
        if MED8=='0':
            Give_medicine.medicine8= '0'
        else:
            Give_medicine.medicine8 = MED8.med_name



        if medicine9=='null' :
             Give_medicine.medicine_name9= "0"
             Give_medicine.available_status9="not selected"
        else:
            if Quantity9=='':
               Give_medicine.Quantity9= 0
            else:
                Give_medicine.Quantity9= Quantity9
                MEDICINE =medicine.objects.get(id=medicine9)
                print(MEDICINE)
                Give_medicine.total9=int(Quantity1)* int(MEDICINE.med_price)
                TOTAL9 = Give_medicine.total9
                MEDICINE.quantity=int(MEDICINE.quantity) - int(Quantity9)
                if MEDICINE.quantity<=0:
                    Give_medicine.available_status9="out of stock"
                else:
                    MEDICINE.save()
                    Give_medicine.available_status9="available"
                Give_medicine.medicine_name9= medicine9
                # if MD.quantity<=int(MEDICINE.quantity):
                #     Give_medicine.available_status9="not available"
                # else:

                Give_medicine.time9= time9
                Give_medicine.food_time9= food_time9
        if MED9=='0':
            Give_medicine.medicine9= '0'
        else:
            Give_medicine.medicine9 = MED9.med_name

        Give_medicine.Total = int(TOTAL1)+int(TOTAL2)+int(TOTAL3)+int(TOTAL4)+int(TOTAL5)+int(TOTAL6)+int(TOTAL7)+int(TOTAL8)+int(TOTAL9)
        Booking =prescriptionTopharmacy.objects.get(Booking_id=Prescription.Booking_id)
        Booking.status='medicine give successfully'
        Prescription.status='provide medicine'
        Booking.save()
        Give_medicine.PARMACY_id=Booking.PARMACY_id.id
        Give_medicine.save()

        return render(request, 'pharmacy/pharmacy_index.html',{'messages':"medicine given successfully"})


class prescription_status(TemplateView):
    template_name = 'pharmacy/view_prescription_status.html'
    def get_context_data(self,**kwargs):
       context = super(prescription_status,self).get_context_data(**kwargs)
       pharmacys=pharmacy.objects.get(user_id=self.request.user.id)
       give_medicines =give_medicine.objects.filter(PARMACY_id=pharmacys.id)
       # print(give_medicines.available_status1)
       context['Prescription']=give_medicines
       return context

class view_prescription(TemplateView):
    template_name = 'pharmacy/view_prescription.html'
    def get_context_data(self, **kwargs):
        context = super(view_prescription,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        BOOKING = booking.objects.get(id=id,status='sent to pharmacy')
        Prescription = give_medicine.objects.get(Booking_id = BOOKING.id)
        context['Prescription']=Prescription
        return context



