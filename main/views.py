from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Kevin",
        "npm": "2506621466",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Currently IS student at Universitas Indonesia,"
            "always excited to learn new things and build cool stuffs along the way."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Kevin",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)