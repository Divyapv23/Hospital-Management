from django.urls import path
from frontendapp import views


urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('webdeptpage/',views.webdeptpage,name="webdeptpage"),
    path('webdocpage/',views.webdocpage,name="webdocpage"),
    path('appoinmentpage/',views.appoinmentpage,name="appoinmentpage"),
    path('appdetails/',views.appdetails,name="appdetails"),
    path('weblogpage/',views.weblogpage,name="weblogpage"),
    path('weblogdetails/',views.weblogdetails,name="weblogdetails"),
    path('customerlogin/',views.customerlogin,name="customerlogin")

]