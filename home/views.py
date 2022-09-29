

from django.shortcuts import render, HttpResponseRedirect, redirect
from home.models import Task
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(Tasktitle = title, Taskdesc = desc)
        ins.save()
        
    return render(request, 'index.html')

def about(request):

    alltasks = Task.objects.all()
    print(alltasks)
   

    return render(request, 'about.html', {'context' : alltasks})


def Update(request, id=None):
    
    if request.method == "POST":
        
        title = request.POST['title']
        
        desc = request.POST['desc']
        Task.objects.filter(pk=id).update(Tasktitle = title , Taskdesc = desc)
        
        return redirect('about')
        #return render(request, 'about.html')
        
    return render(request, 'Update_Task.html',{'id':id})



def Data_D(request, id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        pi.delete()
        return redirect('about')