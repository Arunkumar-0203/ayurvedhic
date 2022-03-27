from django.urls import path

from ayurvedhic_app.doctor_views import index_view, view_users, view_medicine, view_pharmacy, view_booking, \
    view_prescription, view_consulted_users_list, prescription_sended_list, view_consulted_users_list_send_parmacy

urlpatterns=[
    path('',index_view.as_view()),
    path('view_users',view_users.as_view()),
    path('view_medicine',view_medicine.as_view()),
    path('view_pharmacy',view_pharmacy.as_view()),
    path('view_booking',view_booking.as_view()),
    path('view_prescription',view_prescription.as_view()),
    path('view_consulted_users_list',view_consulted_users_list.as_view()),
    path('prescription_sended_list',prescription_sended_list.as_view()),
    path('view_consulted_users_list_send_parmacy',view_consulted_users_list_send_parmacy.as_view())
]
def urls():
    return urlpatterns, 'doctor', 'doctor'