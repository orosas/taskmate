from django.shortcuts import render, redirect
from django.http import HttpResponse

from todolist_app.models import TaskList
from todolist_app.forms import TaskForm

from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

# Método principal. If guarda un nuevo task enviado desde el formulario de todolist.html
# else muestra todos los "tasks" guardados en la base de datos.
# en else, se incluye opción de paginación de Django para mostrar parte de los records
# de la base de datos.

@login_required
def todolist(request):

    if request.method == "POST":

        form = TaskForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request, ("New Task Added!"))
        return redirect('todolist')

    else:
        # all_tasks = TaskList.objects.all().order_by('id')
        all_tasks = TaskList.objects.filter(manage=request.user).order_by('id')

        paginator = Paginator(all_tasks, 6)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks': all_tasks})

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
        messages.success(request, ("Task: " + str(task.id) + " " + task.task + " Deleted!"))
    else:
        messages.error(request, ("Access Restricted. You Are Not Allowed To Delete This Task!"))

    return redirect('todolist', )


# Omar: Edita el nombre o texto de la tarea por hacer
@login_required
def edit_task(request, task_id):
    
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)

        form = TaskForm(request.POST or None, instance = task)
        
        if form.is_valid():
            form.save()

        messages.success(request, ("Task: " + str(task.id) + " " + task.task + " Edited!"))
        return redirect('todolist')

    else:
        task_object = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_object': task_object})


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
        messages.success(request, ("Task: " + str(task.id) + " " + task.task + " Completed!"))
    else:
        # messages.error(request, ("Access Restricted. You Are Not Allowed To Mark As Complete The Task: {}".format(task.task)))
        messages.error(request, ("Access Restricted. You Are Not Allowed To Mark As Complete The Task: "))

    return redirect('todolist')


@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False

    task.save()
    
    messages.success(request, ("Task: " + str(task.id) + " " + task.task + " Pending!"))
    return redirect('todolist')


def index(request):
    
    context = {
        'index_text': "Welcome Index Page."
    }

    return render(request, 'index.html', context)


def contact(request):
    
    context = {
        'contact_text': "Welcome Contact Page."
    }

    return render(request, 'contact.html', context)

def about(request):
    
    context = {
        'about_text': "Welcome About Page."
    }

    return render(request, 'about.html', context)