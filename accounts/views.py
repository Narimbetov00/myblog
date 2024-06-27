from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustemUserCreationForm
# Create your views here.

# from django.urls import reverse_lazy tiykargi waziypasi bul orinlangannan son url pathdi ozgertipqoyadi 


class SignUpView(CreateView):
    form_class = CustemUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# template_name = 'registration/signup.html' qaysi fileda islew kerek ekenligin bildiredi