from django.http import HttpResponse
from django.shortcuts import redirect

def admin_only(view_func):
    def wrappers_func(request, *args,**kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Customer':
            return redirect('profilepage')
        elif group == 'admins':
            return view_func(request,*args,**kwargs)
        
    return wrappers_func
