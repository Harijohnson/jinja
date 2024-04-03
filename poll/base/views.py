from django.shortcuts import render

# Create your views here.
def HomePage(request):
    # context = {'data':'hari'}
    return render(request ,'html/index.html', context={})