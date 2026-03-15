from django import forms

from .models import Employe


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ["name", "email", "poste", "salaire"]
        labels = {
            "name": "Nom",
            "email": "Email",
            "poste": "Poste",
            "salaire": "Salaire",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "email": forms.EmailInput(attrs={"class": "input input-bordered w-full"}),
            "poste": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "salaire": forms.NumberInput(
                attrs={"class": "input input-bordered w-full", "step": "0.01", "min": "0"}
            ),
        }
