from django.test import TestCase

# Create your tests here.

class TestarPaginasMain(TestCase):
    def test_pagina_inicial(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Loja Virtual')

    def test_pagina_ajuda(self):
        response = self.client.get('/ajuda/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, '<h2>Ajuda</h2>')