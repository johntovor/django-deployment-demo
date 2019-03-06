from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'text': 'hello world', 'number': 900}
    return render(request, 'template_app/index.html', context)

def other(request):
    return render(request, 'template_app/other.html')

def relative_url_templates(request):
    return render(request, 'template_app/relative_url_templates.html')
