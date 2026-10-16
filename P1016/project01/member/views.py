from django.shortcuts import render,redirect
from member.models import Member


### 회원가입 ##############################
# def mupdate(request,id):
#     if request.method == 'GET':
#         print(f"확인 : {id}")
#         qs = Member.objects.get(id=id)
#         tel = qs.tel.split('-')
#         context = {'member':qs,'tel':tel}
#         return render(request, 'mupdate.html', context)
#     elif request.method == 'POST':
#         id = request.session.session_id
#         pw = request.POST.get('pw')
#         name = request.POST.get('name')
#         nickname = request.POST.get('nickname')
#         tel1 = request.POST.get('tel1')
#         tel2 = request.POST.get('tel2')
#         tel3 = request.POST.get('tel3')
#         tel = f'{tel1}-{tel2}-{tel3}'
#         gender = request.POST.get('gender')
#         hobby = request.POST.getlist('hobby')
#         qs = Member.objects.get(id=id)
#         qs.pw = pw
#         qs.name = name
#         qs.nickname = nickname
#         qs.tel = tel
#         qs.gender = gender
#         qs.hobby = hobby
#         qs.save()
#         # Member(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby).save()
#         # Member.objects.create(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)

#         # print(f'회원확인: {id},{pw},{name},{nickname},{tel},{gender},{hobby}')
#         return redirect('/')


def mupdate(request, id):
    if request.method == 'GET':
        print(f"확인 : {id}")
        qs = Member.objects.get(id=id)
        tel = qs.tel.split('-') if qs.tel and '-' in qs.tel else ['', '', '']
        context = {'member': qs, 'tel': tel}
        return render(request, 'mupdate.html', context)
        
    elif request.method == 'POST':
        # 1. URL 매개변수로 넘어온 id를 그대로 사용하거나 세션에서 가져올 경우 딕셔너리 방식으로 접근
        # id = request.session.get('session_id')  <- 세션 사용 시 올바른 문법
        
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        tel1 = request.POST.get('tel1')
        tel2 = request.POST.get('tel2')
        tel3 = request.POST.get('tel3')
        tel = f'{tel1}-{tel2}-{tel3}'
        gender = request.POST.get('gender')
        
        # 2. 리스트로 넘어오는 취미 데이터를 쉼표(,)로 연결된 문자열로 변환
        hobby_list = request.POST.getlist('hobby')
        hobby = ','.join(hobby_list)
        
        # 3. DB 업데이트 처리
        qs = Member.objects.get(id=id)
        qs.pw = pw
        qs.name = name
        qs.nickname = nickname
        qs.tel = tel
        qs.gender = gender
        qs.hobby = hobby
        qs.save()

        return redirect('/')

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

        # Member(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby).save()
        Member.objects.create(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)

        # print(f'회원확인: {id},{pw},{name},{nickname},{tel},{gender},{hobby}')
        return render(request,'mresult.html')


### 로그인 ##############################
def login(request):
    if request.method == 'GET' :
        cookie_id = request.COOKIES.get('cookie_id', '')
        context = {'cookie_id':cookie_id}
        return render (request, 'login.html', context)
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        rememberId = request.POST.get('rememberId')

        # DB 확인 / filter 검색 시 리스트로 넘어옴, 그중 first
        qs = Member.objects.filter(id=id,pw=pw).first()
        if qs :
            context = {'temp':1}
            request.session['session_id'] = id
            # request.session['session_id'] = qs.id (위와 동일)
            request.session['session_nickname'] = qs.nickname
        else :
            context = {'temp':0}

        # print(f'확인: {id},{pw},{rememberId}/{context}')

        response = render(request,'login.html', context)
        if rememberId:
            response.set_cookie('cookie_id',id,max_age=60*60*24)
        else : 
            response.delete_cookie('cookie_id')
        return response

        # return render(request,'login.html', context)

### 로그아웃 ##############################
def logout(request):
    request.session.clear()
    context = {'temp':2}
    return render(request,'login.html', context)
    