from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os


def profile(request):
    return render(request, "resume/index.html")


def resume_pdf(request):
    with open(os.path.join(settings.BASE_DIR, 'static/resume/kmankowska_resume.pdf'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        return response
