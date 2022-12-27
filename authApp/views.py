from django.shortcuts import render,redirect
from .form import RegistrationForm,ServiceForm
from django.views import View
from .models import Service
from django.contrib.auth.models import User
# Create your views here.
default = {

}

class Registration(View):
    def get(self,request):
        default['form'] = RegistrationForm()
        return render(request,'index.html',default)
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request,'index.html',{'form':form})

class ServiceView(View):
    def get(self,request):
        default['form'] = ServiceForm()
        default['service'] = Service.objects.filter(user=request.user)
        return render(request,'service.html',default)
    def post(self,request):
        form = ServiceForm(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            rate = form.cleaned_data['rate']
            image = request.FILES['image']
            
            res = Service(user=user,name=name,rate=rate,image=image)
            res.save()
            return redirect('service')
        return redirect('service')
    
def deleteservice(request,pk):
    Service.objects.get(id=pk).delete()
    return redirect('service')

def deleteuser(request,pk):
    User.objects.get(id=pk).delete()
    return redirect('index')