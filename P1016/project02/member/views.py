from django.shortcuts import render
from member.models import Member


### 회원가입 ##############################
def mwrite(request):

    if request.method == 'GET':
        return render(request,'mwrite.html')
    elif request.method == 'POST':

        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        tel1 = request.POST.get('tel1')
        tel2 = request.POST.get('tel2')
        tel3 = request.POST.get('tel3')
        tel = f'{tel1}-{tel2}-{tel3}'
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        Member.objects.create(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)
        return render(request,'mresult.html')



### 로그인 ##############################
def login(request):
    if request.method == 'GET' :
        cookie_id = request.COOKIES.get('cookie_id','')
        context = {'cookie_id':cookie_id}
        return render(request,'login.html',context)
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        rememberId = request.POST.get('rememberId')
        print(f'확인: {id},{pw},{rememberId}')

        qs = Member.objects.filter(id=id).first()
        if qs :
            context = {'temp':1}
            request.session['session_id'] = id
            request.session['session_nickname'] = qs.nickname 
        else : 
            context = {'temp':0}
        
        response = render(request,'login.html', context)
        if rememberId:
            response.set_cookie('cookie_id',id,max_age=60*60*24)
        else :
            response.delete_cookie('cookie_id')
        return response
    


### 로그아웃 ##############################
def logout(request):
    request.session.clear()
    context = {'temp':2}
    return render(request,'login.html', context)
    