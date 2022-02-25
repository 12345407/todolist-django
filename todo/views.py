from urllib import request
from django.shortcuts import render, redirect
from .models import todo

# Create your views here.

def index(request):
    todo1 = todo.objects.all()
    if request.method == 'POST':
        
        new_todo = todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')

    return render(request,'index.html', {'todos':todo1})

def delete(request, pk):
    todo1 = todo.objects.get(id = pk)
    todo1.delete()
    return redirect('/')
