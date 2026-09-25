# B3 — Execução acompanhada de uma verificação

**26/09/2026 · 15h05–15h30 · 25min dentro da aula.** Registro pessoal formativo, sem entrega e sem nota. O professor orienta a turma; cada estudante opera no próprio editor, navegador ou terminal. Instalação e conta não são necessárias.

## Objetivo e insumos

Ligar requisito, resultado e mecanismo de uma verificação de **R1**, antes de aplicar o método a outro requisito na AV1.3. Abrir o [contrato](../caso/regras.md), a função `prioridade` no [código didático](../caso/fila_clara.py) e este roteiro. As entradas são fictícias: impacto = 2 e urgência = 3.

## Passos e registro — 5 + 8 + 7 + 5 minutos

1. **15h05–15h10 — Preparar e prever (5min).** Abrir um registro no próprio ambiente. Ler R1 e calcular a saída esperada antes de examinar o retorno do código.
2. **15h10–15h18 — Operar (8min).** Escolher um dos caminhos abaixo e preencher a tabela. O professor acompanha dúvidas de procedimento.
3. **15h18–15h25 — Comparar e explicar (7min).** Comparar seu registro com o trecho R1 da [transcrição fornecida](resultado-textual.md), após a orientação do professor. Localizar o ramo lógico que explica o resultado. Identificar o que foi observado, inferido ou apenas lido na transcrição.
4. **15h25–15h30 — Rever a decisão (5min).** Registrar uma intervenção necessária e um limite da verificação. Guardar o registro pessoal; não enviar como avaliação ou realizar tarefa extra depois da aula.

**Caminho A — Python já disponível.** Na raiz do kit, executar somente a verificação de R1 abaixo; não é necessário alterar o código nem instalar dependências:

```text
python -B testes/test_fila_clara.py --codigo caso/fila_clara.py --teste TestFilaClara.test_prioridade_alta_no_limiar_cinco
```

O material contém divergências intencionais. Registrar a saída real e seu significado; não confundir falha do caso com problema no seu desempenho. Ver [instruções de execução](../testes/README.md).

**Caminho B — Inspeção no editor ou navegador.** Ler somente `prioridade`, substituir os valores fornecidos e acompanhar as condições na ordem em que aparecem. Registrar qual ramo é percorrido e o retorno inferido. Esse caminho também exercita a verificação; uma inferência não deve ser apresentada como execução de Python.

| Campo | Meu registro |
|---|---|
| Entrada e escore | |
| Esperado pelo contrato R1 | |
| Resultado observado ou inferido | |
| Condição/ramo que explica o resultado | |
| Modalidade: execução própria, inspeção ou transcrição | |
| Intervenção necessária | |
| O que esta verificação não demonstra | |

A comparação final é conduzida pelo professor. O registro não atribui nota nem comprova qualidade geral, produtividade de IA ou correção já executada. A AV1.3 continua com seu próprio enunciado sobre R2 e os mesmos 35min, das 16h15 às 16h50.
