from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from account.forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group


class index(TemplateView):
    template_name = 'index.html'
    title = 'Домашняя страница'

class register(TemplateView):
    template_name = 'registration/register.html'
    form = None

    def get(self,request,*args,**kwargs):
        self.form = UserRegistrationForm
        return super(register,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(register,self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self,request,*args,**kwargs):
        self.form=UserRegistrationForm(request.POST)
        if self.form.is_valid(): #Если все поля заполнены правильно, то регистрируем пользователя и сразу же авторизовываем его
            new_user = self.form.save(commit=False)
            new_user.set_password(self.form.cleaned_data['password'])
            new_user.save()
            new_user.groups.add(Group.objects.get(name='simple_user')) #Добавление в группу обычных пользователей
            if new_user is not None:
                if new_user.is_active:
                    login(request, new_user)
            return redirect('index')

        return super(register,self).get(request,*args,**kwargs)


