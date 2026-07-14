from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html', {
        'name': 'Your Name',
        'title': 'Portfolio Developer',
        'bio': 'I build modern web applications and enjoy creating thoughtful digital experiences.',
        'skills': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
    })
