from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.utils import UnicodeUsernameValidator
from app.models import CustomUser,room_model

class signupForm(UserCreationForm):
    password2 = forms.CharField(label='confirm login password',widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username','email']
        labels = {'email':'EMAIL','username':'USERNAME '}
        error_messages = {'username':{'required':'name is necessary'},
                          'email':{'required':'email is necessary'}}

room_name = UnicodeUsernameValidator()

class room_form(forms.ModelForm):
    error_messages = {
        "room_space": ("please enter full name"),
    }
    class Meta:
        model = room_model
        fields = ('room',)
        labels = {'room':'Create Room'}
        
        
    # def clean(self):
    #     cleaned_data = super().clean()
    #     val_room = self.cleaned_data['room']
    #     print('it validate......')
    #     if val_room == 'box':
    #         raise forms.ValidationError('please enter big room name')
        



        # it use when we validate as specific field 
    def clean_room(self):
        val_room=self.cleaned_data['room']
        for room in val_room:
            print('room words',room)
            if room == " ":
                raise forms.ValidationError(
                    self.error_messages['room_space'],)
                

        return val_room 


