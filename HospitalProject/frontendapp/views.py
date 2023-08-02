from django.shortcuts import render,redirect
from backendapp.models import departmentdb,doctordb
from frontendapp.models import MyModel,logindb

# Create your views here.

def homepage(request):
    return render(request,"home.html")

def webdeptpage(request):
    data=departmentdb.objects.all()
    return render(request,"webdept.html",{'data':data})

def webdocpage(request):
    data=doctordb.objects.all()
    return render(request,"webdoc.html",{'data':data})

def appoinmentpage(request):
    data=doctordb.objects.all()
    dept=departmentdb.objects.all()
    return render(request,"appoinment.html",{'data':data,'dept':dept})

def appdetails(request):
    if request.method=="POST":
        dp=request.POST.get('dept')
        dr=request.POST.get('doc')
        dt=request.POST.get('date')
        tm=request.POST.get('time')
        na=request.POST.get('name')
        ml=request.POST.get('mail')
        ph=request.POST.get('phone')
        pl=request.POST.get('place')
        appobj=MyModel(name=na,place=pl,date_field=dt,choose_doctor=dr,choose_department=dp,
                       phone_number=ph,email_id=ml,time_slot=tm)
        appobj.save()
        return redirect(appoinmentpage)


def weblogpage(request):
    return render(request,"weblogin.html")

def weblogdetails(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ml=request.POST.get('mail')
        ps=request.POST.get('pass')
        objlog=logindb(name=na,mail=ml,password=ps)
        objlog.save()
        return redirect(homepage)

def customerlogin(request):
    if request.method == "POST":
        email_r = request.POST.get('email')
        password_r = request.POST.get('pass')
        if logindb.objects.filter(mail=email_r, password=password_r).exists():
            request.session['username'] = email_r
            request.session['password'] = password_r
            return redirect(appoinmentpage)
        else:
            return redirect(weblogpage)
    return redirect(weblogpage)
