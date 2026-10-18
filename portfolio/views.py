
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Project


def home(request):
    projects = Project.objects.all().order_by("-created_at")

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                "Thank you! Your message has been sent successfully."
            )
            return redirect("home")
    else:
        contact_form = ContactForm()

    return render(
        request,
        "portfolio/index.html",
        {
            "projects": projects,
            "contact_form": contact_form,
        },
    )
