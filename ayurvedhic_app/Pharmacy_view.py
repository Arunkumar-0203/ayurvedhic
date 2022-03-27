from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from ayurvedhic_app.models import medicine, doctor, prescriptionTopharmacy, pharmacy, booking, prescription


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

class view_consulted_users_list_send_parmacy(TemplateView):
    template_name = 'pharmacy/user_consulted_prescription_list.html'
    def get_context_data(self, **kwargs):
        context = super(view_consulted_users_list_send_parmacy,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        BOOKING = booking.objects.get(id=id,status='sent to pharmacy')
        Prescription = prescription.objects.get(Booking_id = BOOKING.id)
        context['Prescription']=Prescription
        return context