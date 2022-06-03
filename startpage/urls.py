
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('submitt_form',views.submitt_form, name='submitt_form'),
    path('main',views.main),
    path('login_submit',views.login_submitt),
    path('logout',views.logout),
    path('contact',views.contact_form),
    path('sellerreg',views.sellerreg),
    path('shops',views.shops),
    path('prac',views.prac)
]
