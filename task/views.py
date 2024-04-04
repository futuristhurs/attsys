from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm  # Import the TaskForm
from .models import Task

# Create your views here.
@login_required
def createTask(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) #Don't save yet to assign creator
            task.creator = request.user
            task.save()
            return redirect('task_list')  # Redirect to a page displaying the list of tasks
    else:
        form = TaskForm()

    
    context = {'form': form}
    return render(request, 'task/create_task.html', context)
        

@login_required
def taskList(request):

    tasks = Task.objects.filter(creator=request.user)
    context = {'tasks': tasks}
    return render(request, 'task/task_list.html', context)

@login_required
def taskDetails(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task/task_details.html', context)

@login_required
def taskUpdate(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    context = {'form': form}
    return render(request, 'task/create_task.html', context)

@login_required
def taskDelete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':   
        task.delete()
        return redirect('task_list')
    context = {'task': task}
    return render(request, 'task/task_delete.html', context)