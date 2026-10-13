from django.shortcuts import render,redirect
from students.models import Students

# 학생정보 삭제
def sdelete(request, no):
    Students.objects.get(no=no).delete()
    return redirect('/students/slist/')

# 학생정보 수정
def supdate(request, no):
    if request.method == 'GET' :
        qs = Students.objects.get(no=no)
        context = {'stu':qs}
        return render(request, 'supdate.html', context)
    elif request.method == 'POST' :
        qs = Students.objects.get(no=no)
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        # 수정된 데이터 반영
        qs.name = name
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.hobby = hobby
        qs.save()
        return redirect('students:slist')


# 학생정보 상세보기
def sview(request, no):
    qs = Students.objects.get(no=no)
    context = {'stu':qs}
    return render(request, 'sview.html', context)


# 학생정보목록
def slist(request):
    # 딕셔너리 형태로 데이터를 전달
    qs = Students.objects.all().order_by('-no')
    # qs = Students.objects.get(name='홍길동')
    # qs = Students.objects.filter(name__contains='s')
    # qs = Students.objects.filter(name__endswith='s')
    # qs = Students.objects.filter(grade__gte=3)
    context = {'list':qs}
    return render(request,'slist.html', context)


# 학생정보입력 FORM으로 전달
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
        Students(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby).save()
        # Students.objects.create(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby)        
        print(name,major,grade,age,gender,hobby)

        return redirect('/')

# # 학생정보입력 URL Path로 전달
# def swrite2(request,name):
#     print(f'값 전달: {name}')
#     return redirect('/')


# # 학생정보입력 Parameter로 전달
# def swrite3(request):
#     name = request.GET.get('name')
#     age = request.GET.get('age')
#     print(f'파라미터 전달: {name}, {age}')
#     return redirect('/')

