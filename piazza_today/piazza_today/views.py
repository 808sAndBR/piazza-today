from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'piazza_today/home_page.html', {})
