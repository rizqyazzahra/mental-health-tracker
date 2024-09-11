from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import MoodEntryForm
from main.models import MoodEntry
from django.shortcuts import render

# Create your views here.
def show_main(request):
    mood_entries = MoodEntry.objects.all()

    context = {
        'name': 'Rizqya Az Zahra Putri',
        'class': 'PBP F',
        'npm': '2306244936',
        'mood_entries': mood_entries
    }

    return render(request, "main.html", context)

def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)

def show_xml(request):
    data = MoodEntry.objects.all()

def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MoodEntry.objects.all()

def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")