from django.forms import ModelForm,ModelMultipleChoiceField,CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from .models import *


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email','college','city']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['room_id','host', 'created']

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['topic','year','month','day']

        