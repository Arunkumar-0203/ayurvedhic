from django.urls import path

from ayurvedhic_app.user_views import index_view, view_doctors, view_appoiments, user_booking, user_view_booking


urlpatterns = [

    path('',index_view.as_view()),
    path('view_doctors',view_doctors.as_view()),
    path('view_appoiments',view_appoiments.as_view()),
    path('user_booking',user_booking.as_view()),
    path('user_view_booking',user_view_booking.as_view()),

]

def urls():
    return urlpatterns, 'user', 'user'