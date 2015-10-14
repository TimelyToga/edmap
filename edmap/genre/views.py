from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'create_genre.html', {})

def view_genre(request, genre_name):
    return render(request, 'view_genre.html', {'genre_name': genre_name})