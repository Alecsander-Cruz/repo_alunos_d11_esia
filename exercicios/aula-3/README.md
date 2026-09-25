# AV1.3 — Ligar requisito, verificação e documentação

**Individual — 35min — B3, 26/09/2026, 16h15–16h50 (Brasília).** Integra AV1, que vale 20% pela média simples dos desafios dos blocos com presença. [Avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero transformar R2 em casos de verificação e documentação consistentes, escolhendo uma etapa delegável e uma condição explícita de aceite humano.

## Contexto e insumos

A manutenção de Fila Clara precisa preparar a revisão de uma listagem. **R2:** incluir `aberto` e `em_andamento`, excluir `fechado` e preservar a ordem de entrada. **R4:** o texto deve descrever o mesmo comportamento. Todas as entradas abaixo são fictícias e válidas. [Contrato completo](../../caso/regras.md).

| Posição na entrada | id | departamento | estado | impacto | urgencia |
|---:|---|---|---|---:|---:|
| 1 | TR-31 | Oficina | em_andamento | 1 | 1 |
| 2 | TR-32 | Laboratório | fechado | 3 | 3 |
| 3 | TR-33 | Oficina | aberto | 2 | 3 |

O material deste desafio é o contrato e esta entrada; não se exige alterar a implementação do repositório. A saída calculada a partir do contrato é **esperada**, não observada em execução. [Template individual](template-registro.md).

## Passos — 35min

1. **Ler — 5min.** Identifique as quatro obrigações de R2 e escreva seu critério de aceite.
2. **Produzir individualmente — 20min.** Elabore três casos de verificação, um para cada estado, indicando entrada, IDs esperados e obrigação verificada. Use os registros fornecidos, isolados ou combinados. Registre também os IDs esperados quando os três entram na ordem da tabela e explique como verificaria a preservação dessa ordem. Escreva uma documentação curta, de até três frases. Escolha uma etapa em que admitiria assistência e descreva o que a pessoa responsável deve verificar antes do aceite. Compare brevemente com a realização dessa etapa sem IA e registre um limite da cobertura.
3. **Revisar pela rubrica — 5min.** Confira a consistência entre casos, ordem, documentação e critério de aceite; diferencie planejamento de teste e resultado executado.
4. **Entregar — 5min.** Finalize um registro individual de até uma página, pelo canal a ser informado pelo professor.

## Entrega e checklist

- [ ] Três casos com entrada/esperado/regra, cobrindo os três estados.
- [ ] IDs esperados da entrada combinada e verificação explícita da ordem.
- [ ] Documentação de até três frases coerente com o mesmo contrato.
- [ ] Etapa delegável, responsável, aceite, alternativa sem IA e limite.
- [ ] Origem fictícia e status de cada evidência declarados.

**Critério de conclusão:** outro leitor consegue conferir os casos e o texto contra R2/R4 e identificar a fronteira da assistência escolhida.

| Critério AV1 | Peso | Indicadores deste desafio |
|---|---:|---|
| Aplicação/decisão | 30% | Etapa e autonomia justificadas; critério e responsável pelo aceite. |
| Evidência | 40% | Três estados, ordem da entrada, resultados esperados e documentação rastreáveis a R2/R4. |
| Limites/alternativa | 30% | Comparação com etapa sem IA; limite de cobertura e condição para rever o aceite. |

**Dica:** uma verificação de pertencimento e uma verificação de ordem respondem a perguntas diferentes. A inspeção textual tem os mesmos critérios que uma execução opcional; nenhum código, conta, API, Git ou apresentação é obrigatório. Declare IA se utilizada.
