from django.http import HttpResponse
from .tasks import download_a_cat

def home(request):
    download_a_cat()
    return HttpResponse('<h1>Cat loading..</h1>')