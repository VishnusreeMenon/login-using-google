from django import forms
from django.contrib.auth.models import User
from .models import Profile,Trigger
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

roles = [
    ('doctor','Doctor'),
    ('patient','Patient')
    
]

intrests = [
    ('overcome depression','Overcome Depression'),
    ('reduce anxiety','Reduce Anxiety'),
    ('overcome social anxiety','Overcome social anxiety'),
    ('sleep better','Sleep Better'),
    ('reduce stress','Reduce stress'),
    ('increase productivity','Increase Productivity'),
    
]

# class ExtendedUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=50)
    
#     class Meta:
#         model = User
#         fields = ('username','email','first_name','last_name')
        
#     def save(self,commit = True):
#         user = super().save(commit=False)
        
#         user.email = self.cleaned_data['email']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
        
#         if commit:
#             user.save()
            
#         return user
    
# class ProfileForm(forms.ModelForm):
#     role = forms.CharField(label="Select your current role:",widget=forms.Select(choices=roles))
#     intrest = forms.CharField(label="Select your intrest:",widget=forms.Select(choices=intrests))
#     class Meta:
#         model = Profile
#         fields = ('company','role','intrest')

class UserForm(forms.ModelForm): 
    
    email = forms.CharField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs= {'class' : 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs= {'class' : 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs= {'class' : 'form-control'}))
    
    
    class Meta():
        model = User       
        fields = ('email','username','first_name','last_name')


class ProfileForm(forms.ModelForm):
    role = forms.CharField(label="Select your current role:",widget=forms.Select(choices=roles))
    company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    intrest = forms.CharField(label="Select your intrest:",widget=forms.Select(choices=intrests))
    class Meta():
        model = Profile       
        fields = ('role','company','intrest')
        # fields = '__all__'


class TriggerForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=User.objects.all())
    assignment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta():
        model = Trigger
        fields = ('patient','assignment')