from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello welcome to Bishal's first django project.")