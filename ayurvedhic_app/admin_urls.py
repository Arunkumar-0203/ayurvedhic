from django.urls import path

from ayurvedhic_app.admin_views import index_view, doctors_index_view, doctor_registration_list, doctor_accepted_list, \
    doctor_rejected_list, doctor_rejected, doctor_accepted, doctor_rejected_list_accepted, view_staff_index, \
    staff_registration_list, staff_accepted_list, staff_rejected_list, staff_accepted, staff_rejected, \
    staff_rejected_list_accepted, view_user_index, user_registration_list, user_accepted_list, user_rejected_list, \
    user_accepted, user_rejected, user_rejected_list_accepted, view_medicine_index, view_available_medicine_list, \
    medicine_status, request_medicine, view_feedback, view_complaint, view_Pharmacy_index, Pharmacy_registration_list, \
    Pharmacy_accepted_list, Pharmacy_rejected_list, Pharmacy_accepted, Pharmacy_rejected, \
    Pharmacy_rejected_list_accepted

urlpatterns=[
    path('',index_view.as_view()),
    path('doctors_index_view',doctors_index_view.as_view()),
    path('doctor_registration_list',doctor_registration_list.as_view()),
    path('doctor_accepted_list',doctor_accepted_list.as_view()),
    path('doctor_rejected_list',doctor_rejected_list.as_view()),
    path('doctor_accepted',doctor_accepted.as_view()),
    path('doctor_rejected',doctor_rejected.as_view()),
    path('doctor_rejected_list_accepted',doctor_rejected_list_accepted.as_view()),

    path('view_staff_index',view_staff_index.as_view()),
    path('staff_registration_list',staff_registration_list.as_view()),
    path('staff_accepted_list',staff_accepted_list.as_view()),
    path('staff_rejected_list',staff_rejected_list.as_view()),
    path('staff_accepted',staff_accepted.as_view()),
    path('staff_rejected',staff_rejected.as_view()),
    path('staff_rejected_list_accepted',staff_rejected_list_accepted.as_view()),

    path('view_user_index',view_user_index.as_view()),
    path('user_registration_list',user_registration_list.as_view()),
    path('user_accepted_list',user_accepted_list.as_view()),
    path('user_rejected_list',user_rejected_list.as_view()),
    path('user_accepted',user_accepted.as_view()),
    path('user_rejected',user_rejected.as_view()),
    path('user_rejected_list_accepted',user_rejected_list_accepted.as_view()),

    path('view_medicine_index',view_medicine_index.as_view()),
    path('view_available_medicine_list',view_available_medicine_list.as_view()),
    path('medicine_status',medicine_status.as_view()),
    path('request_medicine',request_medicine.as_view()),

    path('view_feedback',view_feedback.as_view()),
    path('view_complaint',view_complaint.as_view()),

    path('view_Pharmacy_index',view_Pharmacy_index.as_view()),
    path('Pharmacy_registration_list',Pharmacy_registration_list.as_view()),
    path('Pharmacy_accepted_list',Pharmacy_accepted_list.as_view()),
    path('Pharmacy_rejected_list',Pharmacy_rejected_list.as_view()),
    path('Pharmacy_accepted',Pharmacy_accepted.as_view()),
    path('Pharmacy_rejected',Pharmacy_rejected.as_view()),
    path('Pharmacy_rejected_list_accepted',Pharmacy_rejected_list_accepted.as_view()),
]
def urls():
    return urlpatterns, 'admin', 'admin'