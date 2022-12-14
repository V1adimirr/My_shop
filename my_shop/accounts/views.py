from django.shortcuts import redirect
from django.contrib.auth import login
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User

from accounts.forms import MyUserCreationForm


class UserRegisterView(CreateView):
    model = User
    template_name = 'user_add.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url

