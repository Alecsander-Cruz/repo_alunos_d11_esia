# AV1.2 — Verificar respostas e o alcance de uma alegação

**Individual — 35min — B2, 26/09/2026, 11h15–11h50 (Brasília).** Integra AV1, que vale 20% pela média simples dos desafios dos blocos com presença. [Avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero formular critérios de verificação, aplicá-los a duas respostas e decidir o que cada evidência permite concluir sobre correção e repetição.

## Contexto e insumos

A equipe Fila Clara recebeu duas respostas para revisão. **As respostas A e B são simulações didáticas novas, escritas para esta avaliação. Não resultam de consultas reais a um modelo.** Não há medição disponível de tokens, custo, latência, configuração ou versão do modelo.

**Contrato R1:** impacto e urgência são inteiros de 1 a 3. Some os dois: escore ≥ 5 dá `alta`; escore de 3 a 4 dá `media`; escore < 3 dá `baixa`. [Contrato completo](../../caso/regras.md).

Primeiro registre seu critério de correção e o tipo de evidência necessário para sustentar uma afirmação geral sobre comportamento. Depois examine as respostas.

> **Resposta A — simulada.** “Para priorizar, basta considerar impacto: 1 corresponde a baixa, 2 a media e 3 a alta. Portanto, (impacto=2, urgencia=3) é media e (impacto=3, urgencia=1) é alta.”

> **Resposta B — simulada.** “Repeti três vezes o pedido ‘classifique impacto=2, urgencia=3’. As três saídas foram ‘alta’. Isso prova que o modelo é determinístico e sempre entrega a classificação correta, inclusive em outros chamados.”

Os três resultados de B são parte da narrativa simulada, e não execuções observadas por você. Use o [template individual](template-registro.md).

## Passos — 35min

1. **Ler — 5min.** Leia R1 e registre os critérios antes de avaliar os textos A e B.
2. **Produzir individualmente — 20min.** Verifique os dois pares apresentados em A: registre esperado por R1, resposta e conclusão. Analise separadamente em B a classificação daquele par e a alegação geral. Aponte um contraexemplo ou uma condição que a evidência fornecida não cobre. Decida aceitar, aceitar parcialmente ou rejeitar cada resposta para uso pela equipe; proponha uma alternativa de verificação. Diferencie cálculo/inspeção, narrativa simulada e execução real.
3. **Revisar pela rubrica — 5min.** Confira se as conclusões têm o mesmo alcance das evidências e se informação não disponível foi marcada como tal.
4. **Entregar — 5min.** Envie um registro individual de até uma página pelo canal a ser informado pelo professor.

## Entrega e checklist

- [ ] Critérios prévios e tabela dos dois pares de A, com cálculo essencial.
- [ ] Análise de B distinguindo o resultado particular e a alegação geral.
- [ ] Decisão sobre A e B, alternativa de verificação e limite concreto.
- [ ] Origem simulada declarada; nenhuma medida inventada de modelo real.

**Critério de conclusão:** outra pessoa consegue refazer os cálculos e identificar qual trecho de cada resposta sustenta sua decisão.

| Critério AV1 | Peso | Indicadores deste desafio |
|---|---:|---|
| Aplicação/decisão | 30% | Critérios aplicados e decisões separadas sobre classificação e alegações. |
| Evidência | 40% | R1, dois pares, cálculos e trechos de A/B localizados; origem e status claros. |
| Limites/alternativa | 30% | Contraexemplo ou condição não coberta; alternativa de verificação proporcional, sem generalização indevida. |

**Dica:** verifique tanto a resposta quanto a extensão da afirmação feita a partir dela. Texto é suficiente; não é necessário executar modelo, abrir conta, usar API, Git ou fazer apresentação. Declare eventual uso de IA e não inclua dados reais.
