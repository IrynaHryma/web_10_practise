from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from .forms import RegisterForm

# Create your views here.
class RegisterView(View):
    form_class=RegisterForm
    template_name = "users/signup.html"

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})


    def post(self,request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f"{username}, your account is created")
            return redirect(to="users:login")
        
        return render(request,self.template_name,{'form':form})