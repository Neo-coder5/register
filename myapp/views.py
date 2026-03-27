from django.shortcuts import render, redirect
from .models import Person

def main(request):
    if request.method == "POST":
        model = Person()
        model.first_name = request.POST.get('first_name','')
        model.last_name = request.POST.get('last_name','')
        model.company = request.POST.get('company','')
        model.email = request.POST.get('email','')
        model.phone = request.POST.get('area_code','') + request.POST.get('phone','')
        model.course_type = request.POST.get('course_type','')
        model.subject = request.POST.get('subject','')
        model.exist = request.POST.get('exist','')
        model.save()

        return redirect('persons')

    return render(request,'index.html')


def persons(request):
    query = Person.objects.all()
    return render(request,'list.html', {'persons': query})