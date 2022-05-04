from django.urls import path

from ayurvedhic_app.Pharmacy_view import index_view, add_medicine, Remove_Medicine, Medicine_status, view_Doctors, \
    view_Booking, view_feedback,view_consulted_users_list_send_parmacy, delete_feedback, prescription_status, \
    view_prescription

urlpatterns= [
    path('',index_view.as_view()),
    path('add_medicine',add_medicine.as_view()),
    path('Remove_Medicine',Remove_Medicine.as_view()),
    path('Medicine_status',Medicine_status.as_view()),
    path('view_Doctors',view_Doctors.as_view()),
    path('view_Booking',view_Booking.as_view()),
    path('view_feedback',view_feedback.as_view()),
    path('view_consulted_users_list_send_parmacy',view_consulted_users_list_send_parmacy.as_view()),
    path('delete_feedback',delete_feedback.as_view()),
    path('prescription_status',prescription_status.as_view()),
    path('view_prescription',view_prescription.as_view()),




]
def urls():
    return urlpatterns, 'Pharmacy', 'Pharmacy'