from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
    #     'placeholder' : 'johnDoe'
    # })
    # )
    # gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES,widget=forms.Select(attrs={
    #     'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
    # })
    # )
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #     'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
    #     'placeholder' : 'johnDoe@gmail.com'
    # })
    # )
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
    #     'placeholder' : 'Password'
    # })
    # )
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
    #     'placeholder' : 'Confirm Password'
    # })
    # )

    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                         "class": "w-full px-4 py-2 border border-gray-300 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"    
                             }))


    gender = forms.ChoiceField(
        choices=CustomUser.GENDER_CHOICES,
        widget=forms.Select(attrs={
                        "class": "w-full px-4 py-2 border border-gray-300 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"
        })
    )
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            
           "password1",
           "password2",
           
        )

        widgets = { 
            "username": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            }), 
            
            # "password1": forms.PasswordInput(attrs={
            #     "class": "w-full px-4 py-2 border border-gray-300 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                
            # }),
          
            # "password2": forms.PasswordInput(attrs={
            #     "class": "w-full px-4 py-2 border border-gray-300 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            # }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-blue-500'
        })

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "gender",
            "is_staff",
        )