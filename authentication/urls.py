from django.urls import path
from .import views

urlpatterns=[

    path('account/',views.account,name='account'),
   # path('login',views.loginview,name="login"),
    path('account/login/',views.loginview,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('account/sign_up/',views.sign_up,name="signup"),
    path('reset',views.Resethome,name='reset'),
    path('passwordreset',views.resetpassword,name="passwordreset")
]