from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeForm
from .models import Employe


def effet_splash(request):
    return render(request, "employe/effet_splash.html")


def list_employe(request):
    employes = Employe.objects.all()
    return render(request, "employe/list_employe.html", {"employes": employes})


def ajouter_employe(request):
    if request.method == "POST":
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_employe")
    else:
        form = EmployeForm()

    return render(request, "employe/ajouter_employe.html", {"form": form})


def modifier_employe(request, employe_id):
    employe = get_object_or_404(Employe, id=employe_id)

    if request.method == "POST":
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect("list_employe")
    else:
        form = EmployeForm(instance=employe)

    return render(request, "employe/modifier_employe.html", {"form": form, "employe": employe})


def supprimer_employe(request, employe_id):
    employe = get_object_or_404(Employe, id=employe_id)
    if request.method == "POST":
        employe.delete()
        return redirect("list_employe")

    return render(request, "employe/supprimer_employe.html", {"employe": employe})
