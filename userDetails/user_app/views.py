from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basicApp/index.html')
def relative(request):
    return render(request,'basicApp/relative_url_template.html')
def other(request):
    return render(request,'basicApp/other.html')
def basic(request):
    return render(request,'basicApp/basic.html')
