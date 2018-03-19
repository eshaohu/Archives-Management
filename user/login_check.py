from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
# session登录认证
def login_required(fn):
    @wraps(fn)
    def wrapper(request, *args, **kwargs):
        if request.session.get('user') is None:
            if request.is_ajax():
                return JsonResponse({'code' : 403, 'text' : 'login required', 'result' : None, 'errors' : {}})
            else:
                return redirect('user:index')
        else:
            return fn(request, *args, **kwargs)
    return wrapper

class LoginRequiredMixin:
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.session.get('user') is None:
            if request.is_ajax():
                return JsonResponse({'code' : 403, 'text' : 'login required', 'result' : None, 'errors' : {}})
            else:
                return redirect('user:index')
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)