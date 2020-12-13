from django.shortcuts import render

from django.views.generic.edit import FormView

from .forms import UserRegisterForm

from .models import User

class UserRegisterView(FormView):
	template_name = 'users/register.html'
	form_class = UserRegisterForm
	success_url = '/'

	def form_valid(self, form):
		User.objects.create_user(
			form.cleaned_data['username'],
			form.cleaned_data['email'],
			form.cleaned_data['password1'],
			nombres = form.cleaned_data['nombres'],
			apellidos = form.cleaned_data['apellidos'],
			gener = form.cleaned_data['gener'],
		)

		return super(UserRegisterView, self).form_valid(form)