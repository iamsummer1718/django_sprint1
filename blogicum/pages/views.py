from django.shortcuts import render


def about(request):
    template: str = 'pages/about.html'
    return render(request, template)


def rules(request):
    template: str = 'pages/rules.html'
    return render(request, template)
