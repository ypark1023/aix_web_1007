from django.shortcuts import render
from member.models import Member

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST' :
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        qs = Member.objects.filter(id=id,pw=pw).first()
        if qs :
            request.session['session_id'] = qs.id
            request.session['session_nickname'] = qs.nickname
            context = {'temp':1}
        else :
            context = {'temp':2}

        return render(request, 'login.html', context)
        

def logout(request):
    request.session.clear()
    context = {'temp':2}
    return render(request, 'index.html', context)

def step01(request):
    return render(request, 'step01.html')

def step02(request):
    return render(request, 'step02.html')

def step03(request):
    return render(request, 'step03.html')

def step04(request):
    return render(request, 'step04.html')