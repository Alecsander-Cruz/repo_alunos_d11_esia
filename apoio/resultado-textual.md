# Transcrição de execução

Esta transcrição veio de uma execução real das verificações do material inicial, durante a preparação da disciplina em 23/09/2026. Não é uma resposta simulada de IA. Ambiente observado: Windows, PowerShell e **Python 3.13.3**, somente biblioteca padrão.

Origem: `testes/test_fila_clara.py`, executado na raiz deste pacote contra `caso/fila_clara.py`, com os seis registros de `caso/chamados.json`.

Comando executado:

```text
python -B testes/test_fila_clara.py --codigo caso/fila_clara.py
```

Código de saída observado: **1**. Foram executados nove testes: seis passaram e três falharam. Nos detalhes, o caminho da pasta de preparação foi substituído por `<PACOTE>` para facilitar a leitura; resultados e mensagens foram preservados. O tempo exibido é o tempo dessa execução da suíte; não mede produtividade nem tempo de uma ferramenta de IA.

```text
test_listagem_exclui_chamados_fechados (__main__.TestFilaClara.test_listagem_exclui_chamados_fechados) ... ok
test_listagem_inclui_chamados_em_andamento (__main__.TestFilaClara.test_listagem_inclui_chamados_em_andamento) ... FAIL
test_listagem_preserva_ordem_dos_abertos (__main__.TestFilaClara.test_listagem_preserva_ordem_dos_abertos) ... ok
test_prioridade_alta_no_limiar_cinco (__main__.TestFilaClara.test_prioridade_alta_no_limiar_cinco) ... FAIL
test_prioridade_baixa_no_escore_dois (__main__.TestFilaClara.test_prioridade_baixa_no_escore_dois) ... ok
test_prioridade_nos_demais_escores_validos (__main__.TestFilaClara.test_prioridade_nos_demais_escores_validos) ... ok
test_visibilidade_bloqueia_outro_departamento_em_alta_prioridade (__main__.TestFilaClara.test_visibilidade_bloqueia_outro_departamento_em_alta_prioridade) ... FAIL
test_visibilidade_bloqueia_outro_departamento_nos_demais_escores (__main__.TestFilaClara.test_visibilidade_bloqueia_outro_departamento_nos_demais_escores) ... ok
test_visibilidade_permite_mesmo_departamento_em_todos_os_estados (__main__.TestFilaClara.test_visibilidade_permite_mesmo_departamento_em_todos_os_estados) ... ok

======================================================================
FAIL: test_listagem_inclui_chamados_em_andamento (__main__.TestFilaClara.test_listagem_inclui_chamados_em_andamento)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<PACOTE>\testes\test_fila_clara.py", line 43, in test_listagem_inclui_chamados_em_andamento
    self.assertEqual([chamado["id"] for chamado in resultado], ["FC-002", "FC-005"])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [] != ['FC-002', 'FC-005']

Second list contains 2 additional elements.
First extra element 0:
'FC-002'

- []
+ ['FC-002', 'FC-005']

======================================================================
FAIL: test_prioridade_alta_no_limiar_cinco (__main__.TestFilaClara.test_prioridade_alta_no_limiar_cinco)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<PACOTE>\testes\test_fila_clara.py", line 28, in test_prioridade_alta_no_limiar_cinco
    self.assertEqual(resultados, ["alta", "alta"])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: ['media', 'media'] != ['alta', 'alta']

First differing element 0:
'media'
'alta'

- ['media', 'media']
+ ['alta', 'alta']

======================================================================
FAIL: test_visibilidade_bloqueia_outro_departamento_em_alta_prioridade (__main__.TestFilaClara.test_visibilidade_bloqueia_outro_departamento_em_alta_prioridade)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<PACOTE>\testes\test_fila_clara.py", line 57, in test_visibilidade_bloqueia_outro_departamento_em_alta_prioridade
    self.assertEqual(resultados, [False, False])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [True, True] != [False, False]

First differing element 0:
True
False

- [True, True]
+ [False, False]

----------------------------------------------------------------------
Ran 9 tests in 0.003s

FAILED (failures=3)
```

Para leitura: `ok` significa que a expectativa daquele teste foi satisfeita; `FAIL` aponta uma divergência. Em `AssertionError`, o lado esquerdo apresenta o resultado observado e o direito, a expectativa do teste. Confronte essas expectativas com [as regras do caso](../caso/regras.md).

Ao usar este material, registre a modalidade **análise de transcrição verificada**. A leitura desta saída não equivale a uma execução própria, e o resultado da suíte não atribui nota ao aluno.
