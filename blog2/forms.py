from django import forms
from .models import Post, Comments, SubscribeNewsletter, Profile, Adress, PostImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory, modelformset_factory


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date', 'user')
        
class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']
        
ImageFormSet = modelformset_factory(PostImage, form=PostImageForm, extra=4)
        
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text',]
        exclude = ('user', 'published_date', 'post', 'avatar')
        
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribeNewsletter
        fields = ['email',]
        
class UserRegister(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2',]
        

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','register_date',)
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
        
class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','telephone', 'country', 'city',]
        
class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['street', 'private_house_number', 'entrance_number', 'flat_num']

            
AdressFormSet = inlineformset_factory(Profile, Adress, form= AdressForm, extra=0, can_delete= True)

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

        
