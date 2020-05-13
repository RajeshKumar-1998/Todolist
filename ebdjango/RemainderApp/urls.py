from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('add',views.addrem,name ='add'),
    path('del',views.deletecompleted,name ='del'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('delall',views.delall,name ='delall')
]