from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Note


def all_notes(request):
    #html = "<html> <body> <h1>Welcome In Django with Hasan Alkaf </h1> </body> </html>"
    #return HttpResponse(html)
    #render(request, '<h1>Welcome In Django with Hasan Alkaf </h1>', {})
    all_notes = Note.objects.all()

    context ={
        'all_notes' : all_notes
    }

    return render(request, 'all_notes.html', context)

def detail(request, slug):
    note = Note.objects.get(slug=slug)
    context = {
    'note' : note
    }
    return render(request, 'note_detail.html' , context)
