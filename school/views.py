from django.shortcuts import render
from school.models import Record
# Create your views here.

def index(request):
    records=Record.objects.all()
    return render(request,'index.html',{'records':records})
