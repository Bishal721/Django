from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello welcome to first django project.")