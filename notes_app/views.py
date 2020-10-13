from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from .models import Note
from .forms import NoteForm

## show all available notes
def all_notes(request):
    #html = "<html> <body> <h1>Welcome In Django with Hasan Alkaf </h1> </body> </html>"
    #return HttpResponse(html)
    #render(request, '<h1>Welcome In Django with Hasan Alkaf </h1>', {})
    all_notes = Note.objects.all()

    context ={
        'all_notes' : all_notes
    }

    return render(request, 'all_notes.html', context)

## show one note
def detail(request, slug):
    note = Note.objects.get(slug=slug)
    context = {
    'note' : note
    }
    return render(request, 'note_detail.html' , context)

## add note
def note_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/notes')
    else:
        form = NoteForm()

    context = {
        'form' : form
    }
    return render(request, 'add.html', context)

def note_edit(request, slug):
    note = get_object_or_404(Note, slug=slug)
    print(note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance = note)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/notes')
    else:
        form = NoteForm(instance = note)

    context = {
        'form' : form
    }
    return render(request, 'create.html', context)
