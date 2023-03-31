from django.http import HttpResponse
from django.shortcuts import redirect

def unauthUser(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    
    return wrapper_func
 
def allowed_user(allowed_roles=[]):
   def decorater(view_func):
        def wrapperr_func(request, *args,**kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args,**kwargs)
            else:
                return HttpResponse("You are not authorized!")
        return wrapperr_func
   return decorater

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
