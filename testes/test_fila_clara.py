"""Verificar R1–R3 com dados fictícios controlados e biblioteca padrão.

Na raiz do pacote: python -B testes/test_fila_clara.py --codigo caso/fila_clara.py
Use --teste TestFilaClara.nome_do_teste para executar uma verificação isolada.
"""

import argparse
import importlib.util
import json
from pathlib import Path
import unittest


RAIZ = Path(__file__).resolve().parents[1]
CAMINHO_CODIGO = RAIZ / "caso" / "fila_clara.py"


class TestFilaClara(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        especificacao = importlib.util.spec_from_file_location("codigo_em_analise", CAMINHO_CODIGO)
        cls.codigo = importlib.util.module_from_spec(especificacao)
        especificacao.loader.exec_module(cls.codigo)
        cls.chamados = json.loads((RAIZ / "caso" / "chamados.json").read_text(encoding="utf-8"))

    def test_prioridade_alta_no_limiar_cinco(self):
        resultados = [self.codigo.prioridade(2, 3), self.codigo.prioridade(3, 2)]
        self.assertEqual(resultados, ["alta", "alta"])

    def test_prioridade_baixa_no_escore_dois(self):
        self.assertEqual(self.codigo.prioridade(1, 1), "baixa")

    def test_prioridade_nos_demais_escores_validos(self):
        casos = [(1, 2, "media"), (2, 1, "media"), (1, 3, "media"),
                 (2, 2, "media"), (3, 1, "media"), (3, 3, "alta")]
        for impacto, urgencia, esperado in casos:
            with self.subTest(impacto=impacto, urgencia=urgencia):
                self.assertEqual(self.codigo.prioridade(impacto, urgencia), esperado)

    def test_listagem_inclui_chamados_em_andamento(self):
        entrada = [self.chamados[1], self.chamados[4]]
        resultado = self.codigo.listar_ativos(entrada)
        self.assertEqual([chamado["id"] for chamado in resultado], ["FC-002", "FC-005"])

    def test_listagem_exclui_chamados_fechados(self):
        entrada = [self.chamados[2], self.chamados[5]]
        self.assertEqual(self.codigo.listar_ativos(entrada), [])

    def test_listagem_preserva_ordem_dos_abertos(self):
        entrada = [self.chamados[3], self.chamados[2], self.chamados[0]]
        resultado = self.codigo.listar_ativos(entrada)
        self.assertEqual([chamado["id"] for chamado in resultado], ["FC-004", "FC-001"])

    def test_visibilidade_bloqueia_outro_departamento_em_alta_prioridade(self):
        resultados = [self.codigo.pode_visualizar(self.chamados[1], "Oficina"),
                      self.codigo.pode_visualizar(self.chamados[2], "Laboratório")]
        self.assertEqual(resultados, [False, False])

    def test_visibilidade_permite_mesmo_departamento_em_todos_os_estados(self):
        for chamado in self.chamados:
            with self.subTest(chamado=chamado["id"]):
                self.assertTrue(self.codigo.pode_visualizar(chamado, chamado["departamento"]))

    def test_visibilidade_bloqueia_outro_departamento_nos_demais_escores(self):
        for indice in [0, 3, 4, 5]:
            chamado = self.chamados[indice]
            outro = "Laboratório" if chamado["departamento"] == "Oficina" else "Oficina"
            with self.subTest(chamado=chamado["id"]):
                self.assertFalse(self.codigo.pode_visualizar(chamado, outro))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verificar o comportamento do caso Fila Clara.")
    parser.add_argument("--codigo", type=Path, default=CAMINHO_CODIGO,
                        help="Arquivo Python a verificar; padrão: caso/fila_clara.py.")
    parser.add_argument("--teste", help="Verificação isolada: TestFilaClara.nome_do_teste.")
    argumentos = parser.parse_args()
    CAMINHO_CODIGO = argumentos.codigo.resolve()
    if not CAMINHO_CODIGO.is_file():
        parser.error(f"Arquivo de código não encontrado: {CAMINHO_CODIGO}")
    suite = (unittest.defaultTestLoader.loadTestsFromName(f"{__name__}.{argumentos.teste}")
             if argumentos.teste else unittest.defaultTestLoader.loadTestsFromTestCase(TestFilaClara))
    resultado = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if resultado.wasSuccessful() else 1)
