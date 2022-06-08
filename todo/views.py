from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404

from todo.models import Todo

# Create your views here.
def home(request):

    obj = Todo.objects.all()

    ctx = {'title':obj,}
    return render(request, "todo/home.html" , ctx)

def addtodo(request):

    new = Todo(title = request.POST['title'])

    new.save()
   
    return HttpResponseRedirect('/home/')
        


def deletetodo(request, iteam_id):

    iteam = Todo.objects.get(id=iteam_id)
    iteam.delete()
    return HttpResponseRedirect('/home/')