from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

from ayurvedhic_app.models import doctor, staff, users, pharmacy, FEEDBACK, COMPLAINTS, medicine


class index_view(TemplateView):
    template_name = 'admin/admin_index.html'

class doctors_index_view(TemplateView):
    template_name = 'admin/view_doctors_index.html'
    def get_context_data(self, **kwargs):
        context = super(doctors_index_view,self).get_context_data(**kwargs)
        doctors = doctor.objects.all()
        context['doctors']=doctors
        return context



class doctor_registration_list(TemplateView):
    template_name = 'admin/doctor_registration_list.html'
    def get_context_data(self, **kwargs):
        context = super(doctor_registration_list,self).get_context_data(**kwargs)
        DOCTOR=doctor.objects.filter(status='registered')
        context['DOCTOR']=DOCTOR
        return context

class doctor_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        try:
            if  User.objects.get(id=id,last_name='1'):
                 return render(request,'admin/view_doctors_index.html',{'messages':'Already accepted '})
            else:
                user = User.objects.get(id=id,last_name='0')
                DOCTOR=doctor.objects.get(user_id=id,status='registered')
                DOCTOR.status='accepted'
                user.last_name="1"
                user.save()
                DOCTOR.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
                user = User.objects.get(id=id,last_name='0')
                DOCTOR=doctor.objects.get(user_id=id,status='registered')
                DOCTOR.status='accepted'
                user.last_name="1"
                user.save()
                DOCTOR.save()
                return redirect(request.META['HTTP_REFERER'])


class doctor_rejected(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        try:
            if  User.objects.get(id=id,last_name='0'):
                 return render(request,'admin/view_doctors_index.html',{'messages':'Already rejected '})
            else:
                user = User.objects.get(id=id,last_name='1')
                DOCTOR=doctor.objects.get(status='accepted',user_id=id)
                DOCTOR.status='rejected'
                user.last_name="0"
                DOCTOR.save()
                user.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
                user = User.objects.get(id=id,last_name='1')
                DOCTOR=doctor.objects.get(status='accepted',user_id=id)
                DOCTOR.status='rejected'
                user.last_name="0"
                DOCTOR.save()
                user.save()
                return redirect(request.META['HTTP_REFERER'])


class doctor_accepted_list(TemplateView):
    template_name = 'admin/doctor_accepted_list.html'
    def get_context_data(self, **kwargs):
        context = super(doctor_accepted_list,self).get_context_data(**kwargs)
        DOCTOR=doctor.objects.filter(status='accepted')
        context['DOCTOR']=DOCTOR
        return context


class doctor_rejected_list(TemplateView):
    template_name = 'admin/doctor_rejected_list.html'
    def get_context_data(self, **kwargs):
        context = super(doctor_rejected_list,self).get_context_data(**kwargs)
        DOCTOR=doctor.objects.filter(status='rejected')
        context['DOCTOR']=DOCTOR
        return context

class doctor_rejected_list_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        user = User.objects.get(id=id)
        DOCTOR=doctor.objects.get(user_id=id,status='rejected')
        DOCTOR.status='accepted'
        user.last_name="1"
        user.save()
        DOCTOR.save()
        return redirect(request.META['HTTP_REFERER'])


class view_staff_index(TemplateView):
    template_name = 'admin/view_staff_index.html'
    def get_context_data(self, **kwargs):
        context = super(view_staff_index,self).get_context_data(**kwargs)
        doctors = doctor.objects.all()
        context['doctors']=doctors
        return context


class staff_registration_list(TemplateView):
    template_name = 'admin/staff_registration_list.html'
    def get_context_data(self, **kwargs):
        context = super(staff_registration_list,self).get_context_data(**kwargs)
        Staff=staff.objects.filter(status='registered')
        context['Staff']=Staff
        return context

class staff_accepted_list(TemplateView):
    template_name = 'admin/staff_accepted_list.html'
    def get_context_data(self, **kwargs):
        context = super(staff_accepted_list,self).get_context_data(**kwargs)
        Staff=staff.objects.filter(status='accepted')
        context['Staff']=Staff
        return context


class staff_rejected_list(TemplateView):
    template_name = 'admin/staff_rejected_list.html'
    def get_context_data(self, **kwargs):
        context = super(staff_rejected_list,self).get_context_data(**kwargs)
        Staff=staff.objects.filter(status='rejected')
        context['Staff']=Staff
        return context


class staff_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        try:
            if  User.objects.get(id=id,last_name='1'):
                return render(request,'admin/view_staff_index.html',{'messages':'Already accepted '})
            else:
                user = User.objects.get(id=id,last_name='0')
                STAFF=staff.objects.get(user_id=id,status='registered')
                STAFF.status='accepted'
                user.last_name="1"
                user.save()
                STAFF.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
                user = User.objects.get(id=id,last_name='0')
                STAFF=staff.objects.get(user_id=id,status='registered')
                STAFF.status='accepted'
                user.last_name="1"
                user.save()
                STAFF.save()
                return redirect(request.META['HTTP_REFERER'])


class staff_rejected(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        try:
            if  User.objects.get(id=id,last_name='0'):
                 return render(request,'admin/view_staff_index.html',{'messages':'Already rejected '})
            else:
                user = User.objects.get(id=id,last_name='1')
                STAFF=staff.objects.get(status='accepted',user_id=id)
                STAFF.status='rejected'
                user.last_name="0"
                STAFF.save()
                user.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
                user = User.objects.get(id=id,last_name='1')
                STAFF=staff.objects.get(status='accepted',user_id=id)
                STAFF.status='rejected'
                user.last_name="0"
                STAFF.save()
                user.save()
                return redirect(request.META['HTTP_REFERER'])


class staff_rejected_list_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        user = User.objects.get(id=id)
        STAFF=staff.objects.get(user_id=id,status='rejected')
        STAFF.status='accepted'
        user.last_name="1"
        user.save()
        STAFF.save()
        return redirect(request.META['HTTP_REFERER'])



class view_user_index(TemplateView):
    template_name = 'admin/view_user_index.html'
    def get_context_data(self, **kwargs):
        context = super(view_user_index,self).get_context_data(**kwargs)
        doctors = doctor.objects.all()
        context['doctors']=doctors
        return context



class user_registration_list(TemplateView):
    template_name = 'admin/user_registration_list.html'
    def get_context_data(self, **kwargs):
        context = super(user_registration_list,self).get_context_data(**kwargs)
        USER=users.objects.filter(status='registered')
        context['USER']=USER
        return context

class user_accepted_list(TemplateView):
    template_name = 'admin/user_accepted_list.html'
    def get_context_data(self, **kwargs):
        context = super(user_accepted_list,self).get_context_data(**kwargs)
        USER=users.objects.filter(status='accepted')
        context['USER']=USER
        return context


class user_rejected_list(TemplateView):
    template_name = 'admin/user_rejected_list.html'
    def get_context_data(self, **kwargs):
        context = super(user_rejected_list,self).get_context_data(**kwargs)
        USER=users.objects.filter(status='rejected')
        context['USER']=USER
        return context

class user_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        try:
            if  User.objects.get(id=id,last_name='1'):
                return render(request,'admin/view_user_index.html',{'messages':'Already accepted'})
            else:
                user = User.objects.get(id=id,last_name='0')
                USER=users.objects.get(user_id=id,status='registered')
                USER.status='accepted'
                user.last_name="1"
                user.save()
                USER.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
                user = User.objects.get(id=id,last_name='0')
                USER=users.objects.get(user_id=id,status='registered')
                USER.status='accepted'
                user.last_name="1"
                user.save()
                USER.save()
                return redirect(request.META['HTTP_REFERER'])

class user_rejected(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        try:
            if  User.objects.get(id=id,last_name='0'):
                 return render(request,'admin/view_user_index.html',{'messages':'Already rejected'})
            else:
                user = User.objects.get(id=id,last_name='1')
                USER=users.objects.get(status='accepted',user_id=id)
                USER.status='rejected'
                user.last_name="0"
                USER.save()
                user.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
                user = User.objects.get(id=id,last_name='1')
                USER=users.objects.get(status='accepted',user_id=id)
                USER.status='rejected'
                user.last_name="0"
                USER.save()
                user.save()
                return redirect(request.META['HTTP_REFERER'])



class user_rejected_list_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        user = User.objects.get(id=id)
        USER=users.objects.get(user_id=id,status='rejected')
        USER.status='accepted'
        user.last_name="1"
        user.save()
        USER.save()
        return redirect(request.META['HTTP_REFERER'])

class view_medicine_index(TemplateView):
    template_name = 'admin/view_medicine_index.html'
    def get_context_data(self, **kwargs):
        context = super(view_medicine_index,self).get_context_data(**kwargs)
        doctors = doctor.objects.all()
        context['doctors']=doctors
        return context

class view_available_medicine_list(TemplateView):
    template_name = 'admin/view_available_medicine_list.html'
    def get_context_data(self, **kwargs):
        context = super(view_available_medicine_list,self).get_context_data(**kwargs)
        medicines = medicine.objects.filter(status='active')
        context['medicines']=medicines
        return context


class medicine_status(TemplateView):
    template_name = 'admin/medicine_status.html'
    def get_context_data(self, **kwargs):
        context = super(medicine_status,self).get_context_data(**kwargs)
        medicines = medicine.objects.all()
        context['medicines']=medicines
        return context

class request_medicine(TemplateView):
    template_name = 'admin/request_medicine.html'


class view_feedback(TemplateView):
    template_name = 'admin/view_feedback.html'
    def get_context_data(self, **kwargs):
        context = super(view_feedback,self).get_context_data(**kwargs)
        feeds = FEEDBACK.objects.all()
        context['feeds']=feeds
        return context

class view_complaint(TemplateView):
    template_name = 'admin/view_complaint.html'
    def get_context_data(self, **kwargs):
        context = super(view_complaint,self).get_context_data(**kwargs)
        complaint = COMPLAINTS.objects.all()
        context['complaint']=complaint
        return context


class view_Pharmacy_index(TemplateView):
    template_name = 'admin/view_pharmacy_index.html'
    def get_context_data(self, **kwargs):
        context = super(view_Pharmacy_index,self).get_context_data(**kwargs)
        doctors = doctor.objects.all()
        context['doctors']=doctors
        return context



class Pharmacy_registration_list(TemplateView):
    template_name = 'admin/Pharmacy_registration_list.html'
    def get_context_data(self, **kwargs):
        context = super(Pharmacy_registration_list,self).get_context_data(**kwargs)
        PARMACY=pharmacy.objects.filter(status='registered')
        context['PARMACY']=PARMACY
        return context

class Pharmacy_accepted_list(TemplateView):
    template_name = 'admin/Pharmacy_accepted_list.html'
    def get_context_data(self, **kwargs):
        context = super(Pharmacy_accepted_list,self).get_context_data(**kwargs)
        PARMACY=pharmacy.objects.filter(status='accepted')
        context['PARMACY']=PARMACY
        return context


class Pharmacy_rejected_list(TemplateView):
    template_name = 'admin/Pharmacy_rejected_list.html'
    def get_context_data(self, **kwargs):
        context = super(Pharmacy_rejected_list,self).get_context_data(**kwargs)
        PARMACY=pharmacy.objects.filter(status='rejected')
        context['PARMACY']=PARMACY
        return context

class Pharmacy_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        try:
            if  User.objects.get(id=id,last_name='1'):
                return render(request,'admin/view_pharmacy_index.html',{'messages':'Already accepted'})
            else:
                user = User.objects.get(id=id,last_name='0')
                PARMACY=pharmacy.objects.get(user_id=id,status='registered')
                PARMACY.status='accepted'
                user.last_name="1"
                user.save()
                PARMACY.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
                user = User.objects.get(id=id,last_name='0')
                PARMACY=pharmacy.objects.get(user_id=id,status='registered')
                PARMACY.status='accepted'
                user.last_name="1"
                user.save()
                PARMACY.save()
                return redirect(request.META['HTTP_REFERER'])


class Pharmacy_rejected(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        try:
            if  User.objects.get(id=id,last_name='0'):
                    return render(request,'admin/view_pharmacy_index.html',{'messages':'Already rejected'})
            else:
                user = User.objects.get(id=id,last_name='1')
                PARMACY=pharmacy.objects.get(status='accepted',user_id=id)
                PARMACY.status='rejected'
                user.last_name="0"
                PARMACY.save()
                user.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
                user = User.objects.get(id=id,last_name='1')
                PARMACY=pharmacy.objects.get(status='accepted',user_id=id)
                PARMACY.status='rejected'
                user.last_name="0"
                PARMACY.save()
                user.save()
                return redirect(request.META['HTTP_REFERER'])



class Pharmacy_rejected_list_accepted(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        user = User.objects.get(id=id)
        PARMACY=pharmacy.objects.get(user_id=id,status='rejected')
        PARMACY.status='accepted'
        user.last_name="1"
        user.save()
        PARMACY.save()
        return redirect(request.META['HTTP_REFERER'])