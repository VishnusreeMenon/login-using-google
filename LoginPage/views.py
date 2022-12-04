from django.shortcuts import redirect, render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .forms import ProfileForm ,UserForm,TriggerForm
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,Trigger
from .serializer import ProfileSerializer
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def update_profile(request):
    # try:
    #     profile = request.user.profile
    #     # print("cccccs")
    # except Profile.DoesNotExist:
    #     profile = Profile(user=request.user)
    #     print(profile.user) 
        
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # print("Done, form saved")
            messages.success(request, ('Your profile was successfully updated!'))
            role = profile_form.cleaned_data.get("role")
            print(role)
            if role == 'doctor':
                return redirect('/doctor')
            else:
                return redirect('/patient')
            
            # return redirect('settings:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        
    return render(request, 'LoginPage/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })    

    
class Login(TemplateView):
    template_name = 'LoginPage/login.html'
    
    
class RegistrationApi(APIView):
    
    def post(self, request):
        try:
            data = request.data
            serializer = ProfileSerializer(data = data)
            
            if serializer.is_valid():
                # print(serializer.user)    
                serializer.save()
                
                return Response(
                    {
                        'status':200,
                        'message':'Profile registered',
                        'data':serializer.data
                    }
                )
                
            return Response({
                'status':400,
                'message':"There was some error",
                'data' : serializer.errors
            })
            
        except Exception as e:
            print("error viwes-",e)
            
            
            
class TriggerFill(SuccessMessageMixin,CreateView):
    # model = Trigger
    form_class = TriggerForm
    template_name = 'LoginPage/doctor.html'
    context_object_name = "trigger_form"
    success_url = '/doctor'
    

class ViewAssignments(ListView):
    model = Trigger
    template_name = 'LoginPage/patient.html'
    paginate_by: 10
    context_object_name = "assignments"
    def get_queryset(self):
        return Trigger.objects.filter(patient=self.request.user)
            
# class Registration(CreateView):
#     # model = ProfileForm
#     form_class = ProfileForm    
#     template_name = 'LoginPage/registration.html'
#     context_object_name = 'form'
    
    
# @login_required
# def update_profile(request):
    
#     try:
#         profile = request.user.profile
#         # print("cccccs")
#     except Profile.DoesNotExist:
#         profile = Profile(user=request.user)
#         print(profile.user)
        
        
#     if request.method == 'POST':
#         form = ExtendedUserForm(request.POST)
#         profile_form = ProfileForm(request.POST,instance=profile)
#         print(profile_form)
#         if form.is_valid() and profile_form.is_valid():
#             # user = form.save()
            
#             profile = profile_form.save(commit=False)
#             # profile.user = user
#             # print(profile.user_id)
#             profile.save()
                
#     else:
#         form = ExtendedUserForm()
#         profile_form = ProfileForm()
        
#     context = {'form':form,'profile_form':profile_form}
#     return render(request,'LoginPage/registration.html',context)