from django.urls import path

from ayurvedhic_app.staff_views import index_view, view_doctor, view_booking, accepted_appointments, confirm_booking

urlpatterns = [
    path('',index_view.as_view()),
    path('view_doctor',view_doctor.as_view()),
    path('view_booking',view_booking.as_view()),
    path('accepted_appointments',accepted_appointments.as_view()),
    path('confirm_booking',confirm_booking.as_view())
]
def urls():
    return urlpatterns, 'staff', 'staff'