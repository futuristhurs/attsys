from django.shortcuts import render, redirect
from .forms import TaskForm  # Import the TaskForm
from .models import Task

# Create your views here.
def createTask(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to a page displaying the list of tasks
    else:
        form = TaskForm()

    
    context = {'form': form}
    return render(request, 'task/create_task.html', context)
        

