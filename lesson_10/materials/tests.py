from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from . import factories


class MaterialTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.material = factories.FakeMaterial()

    def test_material_list(self):
        response = self.client.get(reverse('materials:material_list'))
        self.assertEqual(response.status_code, 200)

    def test_material_detail(self):
        response = self.client.get(
            reverse(
                'materials:material_detail', kwargs={'pk': self.material.pk}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_material_create(self):
        data = {
            'name': 'Steel 45'
        }
        response = self.client.post(
            reverse('materials:material_create'),
            data=data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)


class MaterialListViewTest(TestCase):
    """Test case for the MaterialListView."""

    def setUp(self) -> None:
        self.client = Client()
        self.material1 = factories.FakeMaterial(name='material_1')
        self.material2 = factories.FakeMaterial(name='material_2')
        self.material3 = factories.FakeMaterial(name='material_3')

    def test_view_url_exists_at_desired_location(self) -> None:
        response = self.client.get('/materials/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('materials:material_list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('materials:material_list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'materials/material_list.html')

    def test_list_all_tasks(self) -> None:
        response = self.client.get(reverse('materials:material_list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context['materials']), 3)

    def test_material_name_search(self) -> None:
        response = self.client.get(
            reverse('materials:material_list'), {'name': 'Al_2'}
        )
        material_list = response.context['materials']
        self.assertIn(self.material2, material_list)
        self.assertNotIn(self.material1, material_list)
        self.assertNotIn(self.material3, material_list)
