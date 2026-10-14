from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def login(request):

    if request.method == 'GET': 
        return render(request, 'login.html')

    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')

        try: 
            qs = Member.objects.get(id=id, pw=pw) #and를 의미
            request.session['session_id'] = qs.id
            request.session['session_nickname'] = qs.nickname
            print('로그인이 되었습니다')
            context = {'temp':1}
            return render(request,'login.html', context)
        except Member.DoesNotExist:
            print('ID 또는 PW가 일치하지 않습니다')
            return render(request,'login.html')


def logout(request):
    request.session.clear()
    context = {'temp':2}
    return render (request,'login.html', context)
    