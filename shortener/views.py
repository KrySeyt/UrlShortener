from hashlib import sha1

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


def main_page(request: HttpRequest, context: dict = None):
    return render(request, 'shortener/main-page.html', context=context)


def add_url(request: HttpRequest):
    if request.method != 'POST':
        return

    full_url: str = request.POST.get('full-url')
    url = models.Url.objects.filter(full_url=full_url)
    if url.exists():
        context: dict = {
            'full_url': full_url,
            'short_url': url.short_url,
        }
        return main_page(request, context)

    short_url_key = sha1(full_url.encode()).hexdigest()[:16]
    models.Url.objects.create(short_url_key=short_url_key, full_url=full_url)

    short_url = request.build_absolute_uri(reverse('redirect-to-origin', args=(short_url_key,)))
    context: dict = {
        'full_url': full_url,
        'short_url': short_url,
    }
    return main_page(request, context)


def redirect_to_origin(request: HttpRequest, short_url_key):
    url = models.Url.objects.get(short_url_key=short_url_key)
    return redirect(url.full_url)
