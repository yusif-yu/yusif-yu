from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    info = data.objects.all()
    paginate = Paginator(data.objects.all(), 2)
    page = request.GET.get('page')
    info = paginate.get_page(page)
    context = {'info':info}
    return render(request,'index/home.html',context)