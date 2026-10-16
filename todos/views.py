from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')
    
    tasks = Task.objects.all()
    return render(request, 'todos/todo_list.html', {'tasks': tasks})

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('task_list')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')