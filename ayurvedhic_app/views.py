from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from  django.contrib.auth.models import auth,User
# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth import login

from ayurvedhic_app.models import UserType, users, doctor, pharmacy, staff


class index_view(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(index_view,self).get_context_data(**kwargs)
        doctors = doctor.objects.all()
        context['doctors']=doctors
        return context




class docters_view(TemplateView):
    template_name = 'doctors.html'
    def get_context_data(self, **kwargs):
        context = super(docters_view,self).get_context_data(**kwargs)
        doctors = doctor.objects.all()
        context['doctors']=doctors
        return context

class registration_view(TemplateView):
    template_name="registration.html"

class user_registration_view(TemplateView):
    template_name="user_ragistration.html"
    def post(self,request,*arg,**kwargs):
        name=request.POST['name']
        print(name)
        email=request.POST['email']
        print(email)
        Place=request.POST['place']
        print(Place)
        District=request.POST['district']
        print(District)
        age=request.POST['age']
        print(age)
        dateofbirth=request.POST['Dob']
        print(dateofbirth)
        Phone=request.POST['phone']
        print(Phone)
        proof= request.FILES['document']
        f = FileSystemStorage()
        PROOF = f.save(proof.name, proof)
        image= request.FILES['photo']
        F = FileSystemStorage()
        IMAGES = F.save(image.name, image)
        ADRESS=request.POST['address']
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        try:
            user = User.objects.create_user(first_name = name,email=email,password=password,username=username,last_name=0)
            table_user= users()
            table_user.user_id =user.id
            table_user.place = Place
            table_user.age = age
            table_user.dob = dateofbirth
            table_user.id_proof = PROOF
            table_user.photo = IMAGES
            table_user.contact   = Phone
            table_user.email       = email
            table_user.Address   = ADRESS
            table_user.status   = "registered"
            table_user.district      =District
            usertype = UserType()
            usertype.user = user
            usertype.type = 'user'
            usertype.save()
            table_user.save()
            return render(request,'index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})

class doctor_registration_view(TemplateView):
    template_name="doctor_registration.html"
    def post(self,request,*arg,**kwargs):
        name=request.POST['name']
        print(name)
        email=request.POST['email']
        print(email)
        Place=request.POST['place']
        print(Place)
        District=request.POST['district']
        print(District)
        age=request.POST['age']
        print(age)
        dateofbirth=request.POST['Dob']
        print(dateofbirth)
        Phone=request.POST['phone']
        print(Phone)
        proof= request.FILES['document']
        f = FileSystemStorage()
        PROOF = f.save(proof.name, proof)
        image= request.FILES['photo']
        F = FileSystemStorage()
        IMAGES = F.save(image.name, image)
        ADRESS=request.POST['address']
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        Category = request.POST['category']
        try:
            user = User.objects.create_user(first_name = name,email=email,password=password,username=username,last_name=0)
            table_doctor= doctor()
            table_doctor.user_id =user.id
            table_doctor.place = Place
            table_doctor.age = age
            table_doctor.dob = dateofbirth
            table_doctor.id_proof = PROOF
            table_doctor.photo = IMAGES
            table_doctor.contact   = Phone
            table_doctor.email       = email
            table_doctor.Address   = ADRESS
            table_doctor.status   = "registered"
            table_doctor.district      =District
            table_doctor.category= Category
            usertype = UserType()
            usertype.user = user
            usertype.type = 'doctor'
            usertype.save()
            table_doctor.save()
            return render(request,'index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})

class pharmacy_registration_view(TemplateView):
    template_name="pharmacy_registration.html"
    def post(self,request,*arg,**kwargs):
        name=request.POST['name']
        print(name)
        email=request.POST['email']
        print(email)
        Place=request.POST['place']
        print(Place)
        District=request.POST['district']
        print(District)
        Phone=request.POST['phone']
        print(Phone)
        proof= request.FILES['document']
        f = FileSystemStorage()
        PROOF = f.save(proof.name, proof)
        image= request.FILES['photo']
        F = FileSystemStorage()
        IMAGES = F.save(image.name, image)
        ADRESS=request.POST['address']
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        try:
            user = User.objects.create_user(first_name = name,email=email,password=password,username=username,last_name=0)
            table_pharmacy= pharmacy()
            table_pharmacy.user_id =user.id
            table_pharmacy.place = Place
            table_pharmacy.id_proof = PROOF
            table_pharmacy.photo = IMAGES
            table_pharmacy.contact   = Phone
            table_pharmacy.email       = email
            table_pharmacy.Address   = ADRESS
            table_pharmacy.status   = "registered"
            table_pharmacy.district      =District
            usertype = UserType()
            usertype.user = user
            usertype.type = 'pharmacy'
            usertype.save()
            table_pharmacy.save()
            return render(request,'index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})

class staff_registration_view(TemplateView):
    template_name="staff_registration.html"
    def post(self,request,*arg,**kwargs):
        name=request.POST['name']
        print(name)
        email=request.POST['email']
        Category =request.POST['category']
        print(email)
        Place=request.POST['place']
        print(Place)
        District=request.POST['district']
        print(District)
        age=request.POST['age']
        print(age)
        dateofbirth=request.POST['Dob']
        print(dateofbirth)
        Phone=request.POST['phone']
        print(Phone)
        proof= request.FILES['document']
        f = FileSystemStorage()
        PROOF = f.save(proof.name, proof)
        image= request.FILES['photo']
        F = FileSystemStorage()
        IMAGES = F.save(image.name, image)
        ADRESS=request.POST['address']
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        try:
            user = User.objects.create_user(first_name = name,email=email,password=password,username=username,last_name=0)
            table_staff= staff()
            table_staff.user_id =user.id
            table_staff.place = Place
            table_staff.age = age
            table_staff.dob = dateofbirth
            table_staff.id_proof = PROOF
            table_staff.photo = IMAGES
            table_staff.contact   = Phone
            table_staff.email       = email
            table_staff.Address   = ADRESS
            table_staff.status   = "registered"
            table_staff.category = Category
            table_staff.district      =District
            usertype = UserType()
            usertype.user = user
            usertype.type = 'staff'
            usertype.save()
            table_staff.save()
            return render(request,'index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})

class login_view(TemplateView):
    template_name="login.html"
    def post(self,request,*args,**kwargs):
        username=request.POST['username']
        print(username)
        password =request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not  None:
            login(request,user)
            if user.last_name=='1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type=="pharmacy":
                    return redirect('/Pharmacy')
                elif UserType.objects.get(user_id=user.id).type == "doctor":
                    return redirect('/doctor')
                elif UserType.objects.get(user_id=user.id).type == "staff":
                    return redirect('/staff')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                else:
                    return render(request,'login.html',{'message':" User Account Not Authenticated"})

            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})

class about_view(TemplateView):
    template_name = 'about.html'

class gallery_view(TemplateView):
    template_name = 'gallery.html'
