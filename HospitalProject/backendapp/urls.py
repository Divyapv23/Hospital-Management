from django.urls import path
from backendapp import views

urlpatterns=[
    path('loginpage/',views.loginpage,name="loginpage"),
    path('indexpage/',views.indexpage,name="indexpage"),
    path('logindetails/',views.logindetails,name="logindetails"),
    path('deptpage/',views.deptpage,name="deptpage"),
    path('deptdetails/',views.deptdetails,name="deptdetails"),
    path('displaydeptpage/',views.displaydeptpage,name="displaydeptpage"),
    path('editdeptpage/<int:dataid>',views.editdeptpage,name="editdeptpage"),
    path('updatedeptpage/<int:dataid>',views.updatedeptpage,name="updatedeptpage"),
    path('deldeptpage/<int:dataid>',views.deldeptpage,name="deldeptpage"),
    path('doctorpage/',views.doctorpage,name="doctorpage"),
    path('docdetails/',views.docdetails,name="docdetails"),
    path('docdispage/',views.docdispage,name="docdispage"),
    path('doceditpage/<int:dataid>',views.doceditpage,name="doceditpage"),
    path('docupdatepage/<int:dataid>',views.docupdatepage,name="docupdatepage"),
    path('docdeletepage/<int:dataid>',views.docdeletepage,name="docdeletepage"),
    path('displayweblog/',views.displayweblog,name="displayweblog"),
    path('displaywebapp/',views.displaywebapp,name="displaywebapp")



]