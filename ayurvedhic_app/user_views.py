from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from ayurvedhic_app.models import doctor, booking, users, FEEDBACK, COMPLAINTS, pharmacy, give_medicine


class index_view(TemplateView):
    template_name = 'user/user_index.html'
    def get_context_data(self, **kwargs):
          context = super(index_view,self).get_context_data(**kwargs)
          Doctor=doctor.objects.filter(status='accepted')
          context['Doctor']=Doctor
          return context

class view_doctors(TemplateView):
    template_name = 'user/view_doctors.html'
    def post(self,request,*args,**kwargs):
        Category = request.POST['category']
        if Category == 'Toxicology':
            Doctors = doctor.objects.filter(category='Toxicology',status='accepted')
            return render(request, 'user/view_doctors.html',{'Doctor':Doctors})
        elif Category == 'Sexologist':
            Doctors = doctor.objects.filter(category='Sexologist',status='accepted')
            return render(request, 'user/view_doctors.html',{'Doctor':Doctors})
        elif Category == 'Accupressure':
            Doctors = doctor.objects.filter(category='Accupressure',status='accepted')
            return render(request, 'user/view_doctors.html',{'Doctor':Doctors})
        elif Category == 'Gynaecologist':
            Doctors = doctor.objects.filter(category='Gynaecologist',status='accepted')
            return render(request, 'user/view_doctors.html',{'Doctor':Doctors})
        elif Category == 'Naturopathy':
            Doctors = doctor.objects.filter(category='Naturopathy',status='accepted')
            return render(request, 'user/view_doctors.html',{'Doctor':Doctors})
        elif Category == 'General Medicine':
            Doctors = doctor.objects.filter(category='General Medicine',status='accepted')
            return render(request, 'user/view_doctors.html',{'Doctor':Doctors})
        else:
            return render(request, 'user/view_doctors.html',{'message':'no doctors available'})

class view_appoiments(TemplateView):
    template_name = 'user/user_appoiments.html'
    def get_context_data(self, **kwargs):
        context = super(view_appoiments,self).get_context_data(**kwargs)
        Doctor=doctor.objects.filter(status='accepted')
        context['Doctor']=Doctor
        return context

class user_booking(TemplateView):
    template_name = 'user/user_booking_form.html'
    def get_context_data(self, **kwargs):
        context = super(user_booking,self).get_context_data(**kwargs)
        id=self.request.GET['id']
        result=doctor.objects.get(id=id)
        context['result']=result.user.first_name
        context['designation']=result.category
        context['id']=result.id
        return context
    def post(self,request,*args,**kwargs):

        USER =users.objects.get(user_id=self.request.user.id)
        id=request.POST['id']
        date =request.POST['date']
        Time=request.POST['time']
        Description =request.POST['description']
        Booking =booking()
        Booking.booking_date = date
        Booking.user_id=USER.id
        Booking.doctor_id_id = id
        Booking.time=Time
        Booking.description = Description
        Booking.status= 'booked'
        Booking.save()
        return render(request, 'user/user_booking_form.html',{'messages':'Booking successfully'})

class user_view_booking(TemplateView):
    template_name = 'user/user_view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(user_view_booking,self).get_context_data(**kwargs)
        USER = users.objects.get(user_id=self.request.user.id)
        BOOKING=booking.objects.filter(user_id=USER.id)
        context['BOOKING']=BOOKING
        return context

class feedback(TemplateView):
    template_name = 'user/feedback.html'
    def get_context_data(self, **kwargs):
        context = super(feedback,self).get_context_data(**kwargs)
        USER = users.objects.get(user_id=self.request.user.id)
        feeds = FEEDBACK.objects.filter(USER_id=USER.id)
        context['feeds']=feeds
        return context

    def post(self,request,*args,**kwargs):
        feed = request.POST['feed_back']
        user = User.objects.get(id=self.request.user.id)
        USERS = users.objects.get(user_id=user.id)
        feeds = FEEDBACK()
        feeds.USER_id = USERS.id
        feeds.feedback = feed
        feeds.save()
        return redirect(request.META['HTTP_REFERER'])

class complaint(TemplateView):
    template_name = 'user/complaint.html'
    def get_context_data(self, **kwargs):
        context = super(complaint,self).get_context_data(**kwargs)
        USER = users.objects.get(user_id=self.request.user.id)
        complaintss = COMPLAINTS.objects.filter(USER_id=USER.id)
        context['complaintss']=complaintss
        return context

    def post(self,request,*args,**kwargs):
        complaintss = request.POST['complaint']
        user = User.objects.get(id=self.request.user.id)
        USERS = users.objects.get(user_id=user.id)
        complaint = COMPLAINTS()
        complaint.USER_id = USERS.id
        complaint.complaints = complaintss
        complaint.save()
        return redirect(request.META['HTTP_REFERER'])

class delete_feedback(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        FEEDBACK.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class delete_complaint(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        COMPLAINTS.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])


class prescription_status(TemplateView):
    template_name = 'user/view_prescription_status.html'
    def get_context_data(self,**kwargs):
       context = super(prescription_status,self).get_context_data(**kwargs)
       USER=users.objects.get(user_id=self.request.user.id)
       give_medicines =give_medicine.objects.filter(Booking__user_id = USER.id)
       # print(give_medicines.available_status1)
       context['Prescription']=give_medicines
       return context

class view_prescription(TemplateView):
    template_name = 'user/view_prescription.html'
    def get_context_data(self, **kwargs):
        context = super(view_prescription,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        BOOKING = booking.objects.get(id=id,status='sent to pharmacy')
        Prescription = give_medicine.objects.get(Booking_id = BOOKING.id)
        context['Prescription']=Prescription
        return context
