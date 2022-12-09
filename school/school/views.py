from django.shortcuts import render


def error_handler_404(request, exception):
    return render(request, '404.html', status=404)