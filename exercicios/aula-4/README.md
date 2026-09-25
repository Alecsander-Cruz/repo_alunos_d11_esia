# AV1.4 — Revisar uma proposta e o alcance do seu teste

**Individual — 35min — B4, 02/10/2026, 21h15–21h50 (Brasília).** Integra AV1, que vale 20% pela média simples dos desafios dos blocos com presença. [Avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero confrontar uma proposta de listagem com R2, avaliar o que seu teste cobre e justificar o aceite ou o ajuste necessário com revalidação.

## Contexto e insumos

Uma pessoa entregou o candidato abaixo e um teste como suporte à revisão. **São artefatos simulados criados para esta avaliação**, distintos dos exemplos demonstrados pelo professor. O nome do campo é `estado`.

**R2:** incluir `aberto` e `em_andamento`, excluir `fechado` e preservar a ordem de entrada. Entradas são válidas. [Contrato completo](../../caso/regras.md).

```python
# Candidato isolado para análise; não substitua o código do repositório.
def listar_ativos_proposta(chamados):
    ativos = [c for c in chamados if c["estado"] in ("aberto", "em_andamento")]
    return sorted(ativos, key=lambda c: c["impacto"] + c["urgencia"], reverse=True)
```

**Entrada de revisão, na ordem apresentada:**

| id | departamento | estado | impacto | urgencia |
|---|---|---|---:|---:|
| TR-41 | Oficina | em_andamento | 1 | 1 |
| TR-42 | Laboratório | aberto | 3 | 3 |
| TR-43 | Oficina | fechado | 2 | 2 |
| TR-44 | Oficina | aberto | 2 | 2 |

**Teste entregue junto com o candidato:** a entrada contém os mesmos registros, mas na ordem TR-42, TR-44, TR-41, TR-43. A única asserção compara a lista de IDs retornada a `["TR-42", "TR-44", "TR-41"]`. Não há resultado de execução fornecido; você deve analisar seu alcance.

Use o [template individual](template-registro.md). Inspeção por tabela é suficiente; executar o candidato em uma cópia isolada é opcional.

## Passos — 35min

1. **Ler — 5min.** Registre o comportamento esperado por R2 antes de analisar o candidato e o teste.
2. **Produzir individualmente — 20min.** Para a entrada de revisão, registre os IDs esperados e os retornados pelo candidato, explicando o mecanismo. Marque o retorno como inferido por inspeção ou observado em execução. Analise se o teste entregue permite distinguir uma implementação conforme R2 de outra que não a cumpra. Emita parecer de aceite, aceite condicionado ou rejeição. Proponha um ajuste, em texto ou código, e um caso de revalidação com entrada/esperado e resultado previsto ou observado. Compare com a alternativa de manter a proposta atual e explicite um limite.
3. **Revisar pela rubrica — 5min.** Confira contrato, tabela, alcance do teste e revalidação; não descreva previsão como execução realizada.
4. **Entregar — 5min.** Finalize um registro individual de até uma página, pelo canal a ser informado pelo professor.

## Entrega e checklist

- [ ] R2, IDs esperados e retorno do candidato com status explícito.
- [ ] Trecho de código/asserção essencial para explicar o comportamento e a cobertura.
- [ ] Parecer, comparação, ajuste e um caso de revalidação.
- [ ] Limite remanescente e condição que mudaria o parecer.

**Critério de conclusão:** outro leitor consegue refazer sua inspeção, avaliar o alcance do teste e conferir o ajuste proposto contra o mesmo requisito.

| Critério AV1 | Peso | Indicadores deste desafio |
|---|---:|---|
| Aplicação/decisão | 30% | Parecer vinculado a R2; comparação de manter/ajustar e responsabilidade de aceite. |
| Evidência | 40% | Entrada, esperado, retorno, mecanismo e alcance da asserção rastreáveis. |
| Limites/alternativa | 30% | Ajuste e revalidação coerentes; limite de cobertura e condição de revisão. |

**Dica:** teste que passa em uma entrada pode não distinguir comportamentos concorrentes. A via textual vale pelos mesmos critérios; não se exige Git, publicação, conta ou API. Declare eventual assistência de IA e use apenas os dados fictícios.
