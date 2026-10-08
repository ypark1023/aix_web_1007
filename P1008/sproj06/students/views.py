from django.shortcuts import render,redirect
from students.models import Stu

# 학생성적입력
def swrite(request):
    if request.method == 'GET':
        print('GET 페이지가 로딩됨')
        return render(request,'swrite.html')
    elif request.method == 'POST':
        print('POST 페이지가 로딩됨')
        name = (request.POST.get('name'))
        major = (request.POST.get('major'))
        grade = (request.POST.get('grade'))
        age = (request.POST.get('age'))
        gender = (request.POST.get('gender'))

        qs = Stu(name=name, major=major, grade=grade, age=age, gender=gender)
        qs.save()

        print(name,major,grade,age,gender)
        # return render(request,'swrite.html')
        return redirect('/')
    # elif request.method == 'PUT':
    #     pass
    # elif request.method == 'DELETE':
    #     pass

# 학생성적리스트
def slist(request):
    return render(request,'slist.html')