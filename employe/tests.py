from django.test import TestCase
from django.urls import reverse

from .models import Employe


class EmployeCrudTests(TestCase):
    def setUp(self):
        self.employe = Employe.objects.create(
            name="Alice",
            email="alice@example.com",
            poste="Dev",
            salaire="2000.00",
        )

    def test_list_view_loads(self):
        response = self.client.get(reverse("list_employe"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice")

    def test_create_employe(self):
        response = self.client.post(
            reverse("ajouter_employe"),
            {
                "name": "Bob",
                "email": "bob@example.com",
                "poste": "QA",
                "salaire": "1800.00",
            },
        )
        self.assertRedirects(response, reverse("list_employe"))
        self.assertTrue(Employe.objects.filter(email="bob@example.com").exists())

    def test_update_employe(self):
        response = self.client.post(
            reverse("modifier_employe", args=[self.employe.id]),
            {
                "name": "Alice Updated",
                "email": "alice@example.com",
                "poste": "Lead Dev",
                "salaire": "2500.00",
            },
        )
        self.assertRedirects(response, reverse("list_employe"))
        self.employe.refresh_from_db()
        self.assertEqual(self.employe.name, "Alice Updated")
        self.assertEqual(str(self.employe.salaire), "2500.00")

    def test_delete_employe(self):
        response = self.client.post(reverse("supprimer_employe", args=[self.employe.id]))
        self.assertRedirects(response, reverse("list_employe"))
        self.assertFalse(Employe.objects.filter(id=self.employe.id).exists())
