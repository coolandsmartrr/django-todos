from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request):
  if request.method == 'POST':
    if 'add_todo' in request.POST:
      form = TodoForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('todo_list')
    if 'delete_todo' in request.POST:
      todo_id = request.POST.get('todo_id')
      todo = get_object_or_404(Todo, id=todo_id)
      todo.delete()
      return redirect('todo_list')
  else:
    form = TodoForm()
  
  todos = Todo.objects.all()
  return render(request, 'todo_list.html', {'todos': todos, 'form': form})
