from django.shortcuts import render, HttpResponseRedirect
from .form import StudentRegistration
from .models import User


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            fm = StudentRegistration()


    else:
        fm= StudentRegistration()

    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})


# delete function
def delete_data(request,id):
 if request.method == 'POST':
     pi = User.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect('/')