from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245680',
        'name': 'Rajendra Rifqi Baskara',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)