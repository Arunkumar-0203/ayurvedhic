from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class users(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=100,null=True)
    Address = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=100,null=True)
    id_proof= models.ImageField('images/',null=True)
    photo= models.ImageField('images/',null=True)
    place = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=100,null=True)
    Address = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=100,null=True)
    id_proof= models.ImageField('images/',null=True)
    photo= models.ImageField('images/',null=True)
    place = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=100,null=True)
    Address = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=100,null=True)
    id_proof= models.ImageField('images/',null=True)
    photo= models.ImageField('images/',null=True)
    place = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class pharmacy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=100,null=True)
    Address = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    id_proof= models.ImageField('images/',null=True)
    photo= models.ImageField('images/',null=True)
    place = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class medicine(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    med_name= models.CharField(max_length=100,null=True)
    med_price = models.IntegerField(null=True)
    photo= models.ImageField('images/',null=True)
    quantity = models.IntegerField(null=True)
    description = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class booking(models.Model):
    user = models.ForeignKey(users,on_delete=models.CASCADE,null=True)
    doctor_id = models.ForeignKey(doctor,on_delete=models.CASCADE,null=True)
    booking_date = models.DateField(max_length=100,null=True)
    time = models.CharField(max_length=100,null=True)
    description =  models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=100,null=True)

class prescription(models.Model):
    Booking = models.ForeignKey(booking,on_delete=models.CASCADE,null=True)
    symptoms = models.CharField(max_length=100,null=True)
    test  =models.CharField(max_length=100,null=True)
    advice =models.CharField(max_length=100,null=True)

    medicine_name1 = models.CharField(max_length=100,null=True)
    medicine1 = models.CharField(max_length=100,null=True)
    Quantity1 = models.IntegerField(null=True)
    time1 = models.CharField(max_length=100,null=True)
    food_time1 = models.CharField(max_length=100,null=True)

    medicine_name2 =models.CharField(max_length=100,null=True)
    medicine2 =models.CharField(max_length=100,null=True)
    Quantity2 = models.IntegerField(null=True)
    time2 = models.CharField(max_length=100,null=True)
    food_time2 = models.CharField(max_length=100,null=True)

    medicine_name3 =models.CharField(max_length=100,null=True)
    medicine3 =models.CharField(max_length=100,null=True)
    Quantity3 = models.IntegerField(null=True)
    time3 = models.CharField(max_length=100,null=True)
    food_time3 = models.CharField(max_length=100,null=True)

    medicine_name4 =models.CharField(max_length=100,null=True)
    medicine4 =models.CharField(max_length=100,null=True)
    Quantity4 = models.IntegerField(null=True)
    time4 = models.CharField(max_length=100,null=True)
    food_time4 = models.CharField(max_length=100,null=True)

    medicine_name5 =models.CharField(max_length=100,null=True)
    medicine5 =models.CharField(max_length=100,null=True)
    Quantity5 = models.IntegerField(null=True)
    time5 = models.CharField(max_length=100,null=True)
    food_time5 = models.CharField(max_length=100,null=True)

    medicine_name6 =models.CharField(max_length=100,null=True)
    medicine6 =models.CharField(max_length=100,null=True)
    Quantity6 = models.IntegerField(null=True)
    time6 = models.CharField(max_length=100,null=True)
    food_time6 = models.CharField(max_length=100,null=True)

    medicine_name7 =models.CharField(max_length=100,null=True)
    medicine7 =models.CharField(max_length=100,null=True)
    Quantity7 = models.IntegerField(null=True)
    time7 = models.CharField(max_length=100,null=True)
    food_time7 = models.CharField(max_length=100,null=True)

    medicine_name8 =models.CharField(max_length=100,null=True)
    medicine8 =models.CharField(max_length=100,null=True)
    Quantity8 = models.IntegerField(null=True)
    time8 = models.CharField(max_length=100,null=True)
    food_time8 = models.CharField(max_length=100,null=True)

    medicine_name9 =models.CharField(max_length=100,null=True)
    medicine9 =models.CharField(max_length=100,null=True)
    Quantity9 = models.IntegerField(null=True)
    time9 = models.CharField(max_length=100,null=True)
    food_time9 = models.CharField(max_length=100,null=True)

class prescriptionTopharmacy(models.Model):
     doctor_id = models.ForeignKey(doctor,on_delete=models.CASCADE,null=True)
     Booking = models.ForeignKey(booking,on_delete=models.CASCADE,null=True)
     PARMACY_id = models.ForeignKey(pharmacy,on_delete=models.CASCADE,null=True)
     status = models.CharField(max_length=100,null=True)



