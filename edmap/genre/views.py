from django.shortcuts import render
from forms import GenreForm
from models import Genre
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def create(request):
    if request.POST:
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/genre/all')
    else:
        form = GenreForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'create_genre.html', args)

def view_genre(request, genre_name):
    try:
        genre = Genre.objects.get(key=genre_name)
    except Exception:
        return render(request, 'view_genre.html', {'genre': {"name": "NOT FOUND"}})

    return render(request, 'view_genre.html', {'genre': genre})


def all(request):
    return render(request, 'all.html', {'genres': Genre.objects.all()})