from django.shortcuts import render
from member.models import Member


# Create your views here.
def login(request):
    if request.method == 'GET':
            context = {}
            if request.COOKIES.get('cookie_id'): #없을때 None
                context = {'cookie_id':request.COOKIES.get('cookie_id')}
            return render(request, 'login.html',context)
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')    
        idsave = request.POST.get('idsave','')
        # 회원확인 방법2
        qs = Member.objects.filter(id=id,pw=pw).first()
        if qs :
            request.session['session_id'] = qs.id
            request.session['session_nickname'] = qs.nickname
            context = {'temp':1}
        else:
            context = {'temp':0}

        print(f'로그인 정보: {id},{pw},{idsave} / 회원확인: {context}')

        response = render(request, 'login.html', context)

        if idsave != '' :
            response.set_cookie('cookie_id',id, max_age=60*60*24)
        else :
            response.delete_cookie('cookie_id')
        return response

    
        # 회원확인 방법1
        # try:
        #     qs = Member.objects.get(id=id, pw=pw)
        #     request.session['session_id'] = qs.id
        #     request.session['session_nickname'] = qs.nickname
        #     context = {'temp':1}
        #     print('로그인 되었습니다')
        # except Member.DoesNotExist:
        #     context = {'temp':0}
        #     print('아이디 또는 비밀번호가 일치하지 않습니다')

        # print(f'로그인 정보: {id},{pw},{idsave} / 회원확인: {context}')
        # return render(request, 'login.html', context)
            
# python -> html : context
# html -> form : 1.Form/2.Url Path/3.Parameter/4.Javascript(Ajax)
# Session은 서버 저장에 필요, session은 서버, 민감한 정보 vs cookie 로컬에 저장


def logout(request):
    request.session.clear()
    context = {'temp':2}
    return render(request, 'index.html', context)


def join(request):
    return render(request, 'step01.html')

def step02(request):
    return render(request, 'step02.html')

def step03(request):
    return render(request, 'step03.html')

def step04(request):
    return render(request, 'step04.html')