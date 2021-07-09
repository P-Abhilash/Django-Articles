from django.shortcuts import render
import requests
API_KEY = '6e74986113f945c79f538ce657601f88'

# Create your views here.


def home(request):
    category = request.GET.get('category')

    query = request.GET.get('q', None)

    if query:
        url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif query == '':
        url = f'https://newsapi.org/v2/everything?q=news&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    articles = articles[:12]

    context = {
        'articles': articles
    }

    return render(request, 'home.html', context)
