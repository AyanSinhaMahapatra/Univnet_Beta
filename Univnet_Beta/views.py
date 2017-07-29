from django.shortcuts import render


def handler400(request):
    response = render(request, '404.html', status=404)
    return response


def handler500(request):
    response = render(request, '500.html', status=500)
    response.status_code = 500
    return response
