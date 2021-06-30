# posts/urls.py
from django.urls import path
from .views import add_student, search_student, delete_student, update_student, index, all_students

urlpatterns = [
    path('', index, name='home'),
    path('list/', all_students, name='list'),
    path('create/', add_student, name='create'),
    path('read/', search_student, name='read'),
    path('delete/', delete_student, name='delete'),
    path('update/', update_student, name='update'),
]