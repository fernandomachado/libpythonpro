from unittest import TestCase

from libpythonpro import github_api


class TesteGithubApi(TestCase):

    def teste_buscar_avatar(self):
        usuario = 'fernandomachado'
        url_obtida = github_api.buscar_avatar(usuario)
        url_esperada = 'https://avatars.githubusercontent.com/u/32027?v=4'
        self.assertEqual(url_obtida, url_esperada)
