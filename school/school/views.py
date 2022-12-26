from django.shortcuts import render


def error_handler_404(request, exception):
    return render(request, '404.html', status=404)

def error_handler_500(request, *args, **argv):
    return render(request, '404.html', status=500)