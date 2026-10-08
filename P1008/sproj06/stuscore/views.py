from django.shortcuts import render,redirect
from students.models import Stu

# Create your views here.
def score_write(request):
    if request.method == 'GET':
        print('GET 페이지가 로딩됨')
        return render(request,'swrite.html')
    elif request.method == 'POST':
        print('POST 페이지가 로딩됨')

        # qs = Stu(name=name, major=major, grade=grade, age=age, gender=gender)
        # qs.save()

    return render(request, 'score_write.html')
