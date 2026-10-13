from django.shortcuts import render, redirect
from students.models import Student

def sview(request, no):
    qs = Student.objects.get(no=no)
    context = {'stu':qs}
    return render(request, 'sview.html', context)

def slist(request):
    qs = Student.objects.all().order_by('-no')
    context = {'list':qs}
    return render(request,'slist.html', context)

def swrite(request):
    if request.method == 'GET':
        return render(request,'swrite.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        Student(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby).save()
        print(name,major,grade,age,gender,hobby)
        return redirect('/')

