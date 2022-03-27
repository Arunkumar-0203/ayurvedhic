from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from ayurvedhic_app.models import doctor, booking, staff


class index_view(TemplateView):
    template_name = 'staff/staff_index.html'
    def get_context_data(self, **kwargs):
        context = super(index_view,self).get_context_data(**kwargs)
        Doctor=doctor.objects.filter(status='accepted')
        context['Doctor']=Doctor
        return context

class view_doctor(TemplateView):
    template_name = 'staff/view_doctors.html'
    def get_context_data(self, **kwargs):
        context = super(view_doctor,self).get_context_data(**kwargs)
        Doctor=doctor.objects.filter(status='accepted')
        context['Doctor']=Doctor
        return context

class view_booking(TemplateView):
    template_name = 'staff/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(view_booking,self).get_context_data(**kwargs)
        STAFF =staff.objects.get(user_id=self.request.user.id)
        Booking=booking.objects.filter(status='booked',doctor_id__category=STAFF.category)
        context['Booking']=Booking
        return context

class accepted_appointments(TemplateView):
    template_name = 'staff/accepted_appointments.html'
    def get_context_data(self, **kwargs):
        context = super(accepted_appointments,self).get_context_data(**kwargs)
        STAFF =staff.objects.get(user_id=self.request.user.id)
        BOOKING=booking.objects.filter(doctor_id__category=STAFF.category,status='booking confirm')
        context['BOOKING']=BOOKING
        return context


class confirm_booking(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        STAFF =staff.objects.get(user_id=self.request.user.id)
        BOOKING=booking.objects.get(doctor_id__category=STAFF.category,status='booked',id=id)
        BOOKING.status = 'booking confirm'
        BOOKING.save()
        return render(request, 'staff/staff_index.html',{'messages':'Booking confirm successfully'})