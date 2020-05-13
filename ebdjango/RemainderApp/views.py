from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

from .forms import Todoform
from .models import Todorem

def index(request):
    todo = Todorem.objects.order_by('id')
    myform =Todoform()
    contexts = {'todo' : todo , 'myform' : myform}
    return render(request,'index.html',contexts)

@require_POST
def addrem(request):
    mform = Todoform(request.POST)

    if mform.is_valid():
        news = Todorem(list=request.POST['chars'])
        news.save()
        return redirect('index')

def completeTodo(request,todo_id):
    todo = Todorem.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deletecompleted(request):
    Todoobj = Todorem.objects.filter(complete__exact = True)
    Todoobj.delete()
    return redirect('index')
def delall(request):
    Todorem.objects.all().delete()
    return redirect('index')







