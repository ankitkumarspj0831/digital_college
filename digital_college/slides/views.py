from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import assign
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from .forms import add_assign
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def download(request, id=None):
     print(id)
     instance = get_object_or_404(assign, id=id)
     file_path = str(instance.file)

     if os.path.exists(file_path):
         with open(file_path, 'rb') as fh:
             response = HttpResponse(fh.read(), content_type="application/pdf")
             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
             return response
     raise Http404

def addAssign(request):
    assign_files = assign.objects.all()
    form = add_assign(request.POST or None, request.FILES or None)
    if form.is_valid():
        newAssign = form.save(commit=False)
        newAssign.save()
        messages.success(request, "Successfully Uploaded")
    else:
        messages.error(request, "Not Uploaded")
    form_add = {
        "form" : form,
        "assign_files": assign_files,
    }
    return render(request,'faculty/faculty.html',form_add)

def delAssign(request,file_id):
    assign_files = assign.objects.get(pk=file_id).delete()
    return redirect ('/faculty/addAssign/')
