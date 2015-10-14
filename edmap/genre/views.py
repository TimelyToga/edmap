from django.shortcuts import render
from forms import GenreForm
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
    return render(request, 'view_genre.html', {'genre_name': genre_name})