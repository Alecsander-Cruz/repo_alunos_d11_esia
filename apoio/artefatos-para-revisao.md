# Artefatos propostos para revisão em B4

**Textos e trechos construídos para fins didáticos.** Não são transcrições de um modelo real. São candidatos a artefato: a turma decide o que aceitar, rejeitar ou pedir para esclarecer, usando [o contrato do caso](../caso/regras.md). Esta página não é documentação normativa do sistema.

## Candidato 1 — documentação de prioridade

> A prioridade combina impacto e urgência por soma. Chamados com escore superior a cinco recebem prioridade alta; escores três a cinco recebem prioridade média. Os demais têm prioridade baixa. O algoritmo garante que apenas os casos mais graves entram na fila de alta prioridade.

Evidência solicitada ao revisor: uma condição em que o texto pode ser confrontado com o requisito, uma decisão de aceite e uma proposta de revalidação.

## Candidato 2 — teste proposto

```python
def test_prioridade_cobre_extremos():
    assert prioridade(1, 1) == "baixa"
    assert prioridade(3, 3) == "alta"
```

Justificativa candidata: “Os extremos passam; portanto, a classificação de prioridade está validada.”

Evidência solicitada: descrever o alcance do teste, uma hipótese que ele não examina e um critério independente para avaliar a conclusão. O teste pode verificar dois casos corretamente sem sustentar uma conclusão sobre todos os casos.

## Candidato 3 — nota de revisão de acesso

> A função usa departamento e gravidade. O atalho para chamados de alta prioridade parece útil para resposta rápida. A mudança é pequena e pode ser aceita porque não altera a estrutura dos dados.

Evidência solicitada: identificar o requisito que autoriza ou impede essa justificativa, o efeito de erro e quem poderia decidir uma alteração de regra. Tamanho do diff e adequação do comportamento são propriedades diferentes.

## Forma de responder

Usar a estrutura: afirmação do artefato → requisito de referência → verificação/contraexemplo → decisão → correção ou esclarecimento → revalidação. A revisão deve separar o que está demonstrado, o que foi inferido e o que ainda precisa ser verificado.
