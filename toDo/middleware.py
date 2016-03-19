from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import redirect
from re import compile


class LoginRequiredMiddleware:
    def process_request(self, request):
        if request.session.get('user_id', None) is None:
            if 'login' not in request.path and 'register' not in request.path:
                return redirect('login')
        return
