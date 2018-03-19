import datetime
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, ListView
from .login_check import login_required, LoginRequiredMixin


from .models import User, Record, Memo
# Create your views here.



def login(request):
    name = request.POST.get('username')
    password = request.POST.get('userpassword')
    user = User.login(name, password)

    if user:
        location = '/static/user_profile_picture/' + user.profile_picture
        request.session['user'] = {'name': user.name, 'id': user.id, 'nickname': user.nickname, 'location': location}
        return redirect('user:users')
    else:
        context = {}
        context['name'] = name
        context['error'] = '用户名或密码错误'
        return render(request, 'user/login.html', context)

@login_required
def edit(request):
    return render(request, 'user/edit.html')

@login_required
def modify(request):
    id = request.POST.get('id', -1)
    nickname = request.POST.get('usernickname', '')
    profileimage = request.FILES['userprofileimage']


    User.objects.filter(id=id).update(nickname=nickname, profile_picture=str(profileimage))
    handle_upload_file(profileimage, str(profileimage))

    return redirect("user:users")


def handle_upload_file(file, filename):
    path = '/root/Archive_Management/static/user_profile_picture/'
    with open(path+filename,'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

# calendar
@login_required
def calendar(request):
    uid = request.session['user'].get('id', -1)
    date = datetime.datetime.now()

    context = {'memos': Memo.objects.filter(user_id=uid), 'time': date.strftime('%Y-%m-%d')}
    return render(request, 'user/calendar.html', context)


class MemoAddView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        uid = request.POST.get('user_id', -1)
        title = request.POST.get('title', '')
        startday = request.POST.get('startday', '')
        endday = request.POST.get('endday', '')

        Memo.objects.create(user_id=uid, title=title, startday=startday, endday=endday)

        return JsonResponse({'code': 200, 'text': 'success', 'result': None, 'errors':{}})

class MemoEditView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('memo_id', -1)
        title = request.POST.get('memo_title', '')


        Memo.objects.filter(id=id).update(title=title)

        return JsonResponse({'code': 200, 'text': 'success', 'result': None, 'errors':{}})


class MemoDelView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('memo_id', -1)

        Memo.objects.filter(id=id).delete()

        return JsonResponse({'code': 200, 'text': 'success', 'result': None, 'errors':{}})


def logout(request):
    request.session.flush()

    return redirect('user:index')