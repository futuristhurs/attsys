from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Import for login requirement (optional)
from .models import WorkLog
from .forms import WorkLogForm  # Assuming you have a WorkLogForm defined

@login_required(login_url='login')  # Adjust as needed for authentication
def work_log(request):
    """
    View function to handle work log entries.
    """
    current_user = request.user  # Get the current user (if using authentication)

    if request.method == 'POST':
        form = WorkLogForm(request.POST)
        if form.is_valid():
            work_log = form.save(commit=False)  # Don't save right away

            # Assign the work log to the current user (if applicable)
            if current_user.is_authenticated:
                work_log.intern = current_user.intern  # Assuming linked through Intern model

            work_log.save()
            return redirect('work_log_list')  # Redirect to work log list view after successful save
    else:
        form = WorkLogForm()

    context = {'form': form}
    return render(request, 'work_log/work_log_form.html', context)

@login_required(login_url='login')  # Adjust as needed for authentication
def work_log_list(request):
    """
    View function to list all work log entries for an intern (if applicable) or all entries (for admin).
    """
    current_user = request.user

    if current_user.is_authenticated:
        work_logs = WorkLog.objects.filter(intern=current_user.intern)  # Filter by intern if logged in
    else:
        work_logs = WorkLog.objects.all()  # Show all entries for admin/unauthenticated users (optional)

    context = {'work_logs': work_logs}
    return render(request, 'work_log/work_log_list.html', context)
