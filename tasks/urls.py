from django.urls import path
from .views import TaskView,TasksView,CategoryDetail
urlpatterns =[

    path('categories', CategoryDetail.as_view(), name='category-detail'),

    path('tasks', TasksView.as_view(), name="book-list-create"),

    path('tasks/<int:pk>', TaskView.as_view(), name="book-detail"),
]