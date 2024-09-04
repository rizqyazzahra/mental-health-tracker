from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306244936',
        'name': 'Rizqya Az Zahra Putri',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)