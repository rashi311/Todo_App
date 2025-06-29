from django.shortcuts import render,redirect
from .models import Task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.
'''
class  TaskListView(ListView):
    model=Task
    template_name='myapp/index.html'
    context_object_name='task_list'
'''

class TaskDetailView(DetailView):
    model=Task
    template_name='myapp/detail.html'    
    context_object_name='task'

def index(request):
    task_list=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')

        task=Task(name=name,priority=priority,date=date)
        task.save()
        return redirect('/')
    

    return render(request,'myapp/index.html',{'task_list':task_list})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')



    return render(request,'myapp/delete.html',{'task':task})


def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'myapp/edit.html',{'form':form,'task':task})