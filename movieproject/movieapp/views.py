from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movieform
from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'mov':movie})

def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('movie_name',)
        desc = request.POST.get('movie_desc',)
        year = request.POST.get('movie_year',)
        img = request.FILES['movie_img']
        movie = Movie(movie_name=name,movie_desc=desc,movie_year=year,movie_img=img)
        movie.save()
    return render(request,'add.html')

def update(request,mov_id):
    movie = Movie.objects.get(id=mov_id)
    forms = Movieform(request.POST or None,request.FILES,instance=movie)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'form':forms,'movie':movie})

def Delete(request,id):
    if request.method == "POST":
        film = Movie.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request,'delete.html')

