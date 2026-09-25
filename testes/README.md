# Verificações do caso

As nove verificações usam `unittest` e a biblioteca padrão do Python **3.13.3**. Execute os comandos a partir da raiz do pacote, onde está o `README.md` principal.

```text
python -B testes/test_fila_clara.py --codigo caso/fila_clara.py
```

`--codigo` recebe o caminho do arquivo Python a verificar. Pode apontar para uma cópia de trabalho; quando omitido, usa `caso/fila_clara.py`. A opção `-B` evita arquivos auxiliares de cache.

Para selecionar uma verificação pelo nome de comportamento:

```text
python -B testes/test_fila_clara.py --codigo caso/fila_clara.py --teste TestFilaClara.test_prioridade_alta_no_limiar_cinco
```

| Regra | Cobertura |
|---|---|
| R1 | As nove combinações válidas de impacto e urgência, organizadas em três testes |
| R2 | Inclusão de chamados em andamento, exclusão dos fechados e ordem de entrada dos abertos |
| R3 | Visibilidade no mesmo departamento e bloqueio entre departamentos em diferentes escores |
| R4 | Revisão humana da coerência entre documentação, contrato e evidências; não é automatizada por esta suíte |

No material inicial, seis testes passam e três falham. `ok` indica verificação satisfeita; `FAIL` indica divergência da expectativa e `ERROR` indica impedimento para executar a verificação. O processo retorna `0` quando o conjunto executado passa e `1` se há falha ou erro.

A saída é evidência sobre este material, não nota de aluno. Sucesso nos testes não demonstra segurança completa, qualidade geral ou produtividade da IA. Não se verifica comportamento de um modelo de linguagem. A transcrição acessível está em [resultado-textual.md](../apoio/resultado-textual.md).
