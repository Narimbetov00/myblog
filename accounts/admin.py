from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustemUserCreationForm,CustemUserChangeForm
from .models import CustomUser
# Register your models here.


class CustemUserAdmin(UserAdmin):
    add_form = CustemUserCreationForm
    form = CustemUserChangeForm
    model = CustomUser
    list_display = ['email','username','first_name','last_name','age','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
        )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('age',)}),
    )

admin.site.register(CustomUser,CustemUserAdmin)