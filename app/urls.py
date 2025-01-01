from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,RegisterPageView
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('register/',RegisterPageView.as_view(),name='register'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page="login"),name='logout'),

    path("",TaskList.as_view(),name="tasks"),
    path("<int:pk>/",TaskDetail.as_view(),name="task_detail"),
    path("creator/",TaskCreate.as_view(),name="task_create"),
    path("edit/<int:pk>/",TaskUpdate.as_view(),name="task_update"),
    path("delete/<int:pk>",TaskDelete.as_view(),name="task_delete")
]