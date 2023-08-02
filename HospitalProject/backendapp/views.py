from django.shortcuts import render,redirect
from backendapp.models import adminlogin,departmentdb,doctordb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from frontendapp.models import logindb,MyModel

# Create your views here.

def loginpage(request):
    return render(request,"weblogin.html")

def indexpage(request):
    return render(request,"index.html")

def logindetails(request):
    if request.method=="POST":
        em=request.POST.get('email')
        ps=request.POST.get('pass')
        if adminlogin.objects.filter(Mail=em,Password=ps).exists():
            request.session['email']=em
            request.session['pass']=ps
            return redirect(indexpage)
        else:
            return redirect(loginpage)
    return redirect(loginpage)

def deptpage(request):
    return render(request,"department.html")

def deptdetails(request):
    if request.method=="POST":
        na=request.POST.get('Dname')
        im=request.FILES['Dimage']
        ds=request.POST.get('Ddescription')
        deptobj=departmentdb(Name=na,Image=im,Description=ds)
        deptobj.save()
        return redirect(deptpage)

def displaydeptpage(request):
    data=departmentdb.objects.all()
    return render(request,"deptdisplay.html",{'data':data})

def editdeptpage(request,dataid):
    data=departmentdb.objects.get(id=dataid)
    return render(request,"deptedit.html",{'data':data})

def updatedeptpage(request,dataid):
    if request.method=="POST":
        na = request.POST.get('Dname')
        ds = request.POST.get('Ddescription')
        try:
            img = request.FILES['Dimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = departmentdb.objects.get(id=dataid).Image
        departmentdb.objects.filter(id=dataid).update(Name=na, Image=file, Description=ds)
        return redirect(displaydeptpage)

def deldeptpage(request,dataid):
    data=departmentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydeptpage)


def doctorpage(request):
    data=departmentdb.objects.all()
    return render(request,"doctors.html",{'data':data})

def docdetails(request):
    if request.method=="POST":
        dnm=request.POST.get('Drname')
        ql=request.POST.get('qul')
        dim=request.FILES['Drimage']
        dpt=request.POST.get('Dept')
        drobj=doctordb(Drname=dnm,Qul=ql,Drimage=dim,Dept=dpt,)
        drobj.save()
        return redirect(doctorpage)

def docdispage(request):
    data=doctordb.objects.all()
    return render(request,"docdisplay.html",{'data':data})

def doceditpage(request,dataid):
    data=doctordb.objects.get(id=dataid)
    dept=departmentdb.objects.all()
    return render(request,"docedit.html",{'data':data,'dept':dept})

def docupdatepage(request,dataid):
    if request.method=="POST":
        dnm = request.POST.get('Drname')
        ql = request.POST.get('qul')
        dpt = request.POST.get('Dept')
        try:
            dim = request.FILES['Drimage']
            fs=FileSystemStorage()
            file=fs.save(dim.name,dim)
        except MultiValueDictKeyError:
            file=doctordb.objects.get(id=dataid).Drimage
        doctordb.objects.filter(id=dataid).update(Drname=dnm,Dept=dpt,Qul=ql,Drimage=file)
        return redirect(docdispage)


def docdeletepage(request,dataid):
    data=doctordb.objects.filter(id=dataid)
    data.delete()
    return redirect(docdispage)

def displayweblog(request):
    data=logindb.objects.all()
    return render(request,"displayuserlogin.html",{'data':data})

def displaywebapp(request):
    data=MyModel.objects.all()
    return render(request,"displayapp.html",{'data':data})