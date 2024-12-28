from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name='auth/login.html'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name="task_list"
    template_name="app/home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['task_list']=context['task_list'].filter(user=self.request.user)
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name="task"
    template_name="app/task.html"

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    template_name="app/task_form.html"
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    success_url=reverse_lazy("tasks")
    template_name="app/task_delete.html"