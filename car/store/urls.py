from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('company',views.company, name="company"),
    path('company/<str:slug>',views.companyview, name="companyview"),
    path('company/<str:comp_slug>/<str:prod_slug>',views.productview, name="productview"),

    path('searchcar/',views.searchcar),
    
    path('signup',views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
    path('signout',views.signout, name="signout"),

  

]