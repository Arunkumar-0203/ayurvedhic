from django.urls import path

from ayurvedhic_app.user_views import index_view, view_doctors, view_appoiments, user_booking, user_view_booking, \
    feedback, complaint, delete_feedback, delete_complaint, prescription_status, view_prescription

urlpatterns = [

    path('',index_view.as_view()),
    path('view_doctors',view_doctors.as_view()),
    path('view_appoiments',view_appoiments.as_view()),
    path('user_booking',user_booking.as_view()),
    path('user_view_booking',user_view_booking.as_view()),
    path('feedback',feedback.as_view()),
    path('complaint',complaint.as_view()),
    path('delete_feedback',delete_feedback.as_view()),
    path('delete_complaint',delete_complaint.as_view()),
    path('prescription_status1',prescription_status.as_view()),
    path('view_prescription1',view_prescription.as_view()),

]

def urls():
    return urlpatterns, 'user', 'user'