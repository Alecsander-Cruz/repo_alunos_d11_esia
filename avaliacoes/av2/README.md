# AV2 — Estudo técnico de verificação

**Individual · 30% da nota · 2h autônomas após B3.** Prazo proposto: **30/09/2026, 23h59, Brasília**. Entrega: **até duas páginas de análise + até duas páginas de anexo técnico**. Canal acadêmico a ser informado pelo professor. [Avaliação e rubrica pública completa](../../avaliacao.md).

## Objetivo

Quero verificar uma proposta de visibilidade contra um requisito aprovado, produzir evidência rastreável e decidir seu encaminhamento comparando uma alternativa.

## Contexto e insumos

A manutenção de Fila Clara recebeu um candidato de código e uma documentação para revisão. Os [insumos de AV2](insumos.md) fornecem o contrato, a proposta isolada, a documentação fictícia e dados suficientes para a análise. Todos são didáticos; não representam saída observada de um modelo real. O candidato é objeto de avaliação e não substitui as funções do repositório.

Use o [template de entrega](template-entrega.md). Você pode executar o candidato em uma cópia isolada ou inspecioná-lo por tabela. As duas vias permitem atingir todos os níveis da mesma rubrica; a qualidade da análise define a nota.

## Trabalho e tempo — 120min

| Etapa | Tempo | Ação e produto |
|---|---:|---|
| Recorte e critério | 20min | Leia R3/R4; delimite a tarefa, escreva o critério de aceite antes de avaliar o candidato e formule a matriz. |
| Verificação | 60min | Analise no mínimo quatro casos cruzando departamento igual/diferente e estado aberto/fechado; confronte esperado, comportamento do código e texto da documentação; investigue uma alternativa. |
| Registro e revisão | 40min | Escreva a análise, selecione trechos essenciais para o anexo, aplique a rubrica e finalize a entrega. |

1. **Defina o recorte.** Identifique função, usuário do resultado, entradas válidas e requisito que governa a decisão. Não acrescente requisitos de autenticação, persistência ou validação de dados externos.
2. **Formule a matriz.** Inclua ao menos as quatro combinações: mesmo departamento/aberto; mesmo departamento/fechado; departamento diferente/aberto; departamento diferente/fechado. Escolha valores válidos de impacto e urgência. Registre o esperado por R3 antes de comparar com a proposta.
3. **Verifique.** Em cada linha, registre entrada completa ou referência aos dados, esperado, retorno do candidato e status **observado em execução** ou **inferido por inspeção**. Explique o caminho lógico de ao menos um caso decisivo e um caso de controle. Confronte a documentação com R3 e com o código, localizando o trecho relevante.
4. **Decida e compare.** Emita aceite, aceite condicionado ou rejeição para código e documentação. Compare com uma alternativa de encaminhamento ou de implementação/documentação; se propuser ajuste, diga o que muda e reaplique os casos, em tabela ou execução. Identifique responsável pelo aceite e condição para rever sua decisão.
5. **Delimite.** Declare origem, método, uso de IA e o que as verificações não demonstram. Planejar um teste não equivale a executá-lo. Não conclua sobre segurança de um sistema real ou produtividade de IA a partir desta análise.

## Conteúdo da entrega

**Análise — até duas páginas:** requisito e critério; estratégia; principais achados com ponteiros para a matriz e trechos; decisão comparada, responsável e limite. **Anexo — até duas páginas:** matriz completa, trechos essenciais de código/documentação e eventual comando/saída. Evite logs extensos ou transcrições integrais de conversa.

| Critério | Peso | O que deve estar examinável |
|---|---:|---|
| Recorte e requisito | 15% | Tarefa, contrato R3/R4, escopo e critério prévio. |
| Estratégia de verificação | 25% | Quatro combinações e justificativa da cobertura; casos decisivo e de controle. |
| Evidência e rastreabilidade | 30% | Entradas, esperado, retorno, trechos e status suficientes para repetir ou auditar a análise. |
| Decisão e alternativa | 20% | Encaminhamento coerente, comparação e verificação da alternativa proposta. |
| Procedência e limites | 10% | Origem e eventual IA declaradas; inferência separada de execução; limite com efeito na decisão. |

## Checklist de entrega

- [ ] Até duas páginas de análise + até duas de anexo técnico.
- [ ] Matriz de pelo menos quatro casos cobrindo todas as combinações solicitadas.
- [ ] Esperado por contrato separado do retorno e de seu status observado/inferido.
- [ ] Código e documentação confrontados com evidência localizada.
- [ ] Decisão, alternativa, responsável, revalidação quando houver ajuste e limite.
- [ ] Origem simulada e eventual IA declaradas; raciocínio e decisão próprios.

A entrega escrita basta. Não se exigem instalação, conta, API, Git, publicação, pesquisa externa ou demonstração adicional. Não altere o código do kit nem use dados reais.
