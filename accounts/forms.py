from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
  

#User jaratiw bolimi  
class CustemUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name','email','age',)

class CustemUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','age',)