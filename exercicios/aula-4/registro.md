# Registro individual — AV1.4

**Limite: uma página.** Estudante: Alecsander D. Cruz — Data: 09/10/2026
**Critério de aceite por R2:** Para ser aceita, a listagem deve incluir `aberto` e `em_andamento`, excluir `fechado` e preservar a ordem da entrada. A saída só será aceita se os IDs retornados forem os mesmos e se eles estiverem nas posições esperadas.

| Entrada | IDs esperados por R2 | IDs do candidato | Status: inferido/observado | Mecanismo/trecho essencial |
|---|---|---|---|---|
| TR-41, TR-42, TR-43, TR-44 | TR-41, TR-42, TR-44 | TR-42, TR-44, TR-41 | Inferido por leitura de código; não executado. | Filtro `c["estado"] in ("aberto", "em_andamento")` atende R2 (exclui TR-43). Porém `sorted(ativos, key=lambda c: c["impacto"] + c["urgencia"], reverse=True)` reordena pela soma decrescente (6, 4, 2) e leva TR-41 para a última posição, o que viola "preservar a ordem de entrada". |

**Teste entregue — o que verifica e o que não consegue distinguir:** Por leitura, o candidato devolve `["TR-42", "TR-44", "TR-41"]` para a entrada do teste e passaria na asserção; o teste verifica a exclusão de `fechado` (TR-43). Porém não consegue verificar a exigência de R2 de "preservar a ordem de entrada": essa entrada já está em ordem decrescente de soma (6, 4, 2), então preservar a ordem e ordenar pela soma produzem a mesma lista. Uma função que cumpre R2 e o candidato passariam igualmente, ou seja, o teste não distingue os dois comportamentos.
**Trecho do teste (entrada e comparação de IDs) que sustenta minha análise:** O teste usa a entrada na ordem `TR-42, TR-44, TR-41, TR-43` (somas 6, 4, 2, 4) e compara os IDs retornados a `["TR-42", "TR-44", "TR-41"]`. Esse esperado é ao mesmo tempo a ordem de entrada filtrada e a ordem por soma decrescente, por isso a asserção não expõe o `sorted(ativos, key=lambda c: c["impacto"] + c["urgencia"], reverse=True)`. Já com a entrada da primeira tabela, `["TR-41", "TR-42", "TR-43", "TR-44"]`, R2 exige `["TR-41", "TR-42", "TR-44"]`, mas o candidato devolveria `["TR-42", "TR-44", "TR-41"]`, indicando, por leitura, que o código viola a preservação da ordem exigida por R2.
**Decisão (aceitar, aceitar com condições ou rejeitar) e motivo:** Rejeito, pois o código proposto não faz o que foi exigido por R2 e o retorno dele altera a ordem de entrada.
**Comparação entre manter e ajustar / responsável pelo aceite:** Com a proposta mantida, a preservação da ordem exigida por R2 seria violada sempre que a entrada não estivesse em ordem decrescente de soma, e o teste entregue continuaria passando sem detectar a violação; se a proposta for alterada para cumprir R2, teremos uma pequena mudança no código e novos testes feitos com entradas fora da ordem de soma, conferindo novamente os IDs e as posições contra R2; existe também outra alternativa, que seria mudar o próprio contrato. Se isso fosse desejado, a mudança teria de ser proposta e aprovada formalmente pelo responsável do contrato, o que não cabe a esta revisão; quem aprovaria o aceite seria o responsável pela manutenção da listagem, após conferir o caso de revalidação.
**Ajuste proposto (texto ou código):** Remoção da função `sorted` do retorno da listagem, deixando apenas
```python
def listar_ativos_proposta(chamados):
    return [c for c in chamados if c["estado"] in ("aberto", "em_andamento")]
```
Após a mudança no código, testar outra ordem de entrada, como, por exemplo, `["TR-41", "TR-44", "TR-43", "TR-42"]`, que deveria retornar `["TR-41", "TR-44", "TR-42"]`.

| Caso para conferir o ajuste: entrada e ordem | IDs esperados | Resultado previsto ou observado / status |
|---|---|---|
| TR-41, TR-44, TR-43, TR-42 | TR-41, TR-44, TR-42 | TR-41, TR-44, TR-42; inferido por inspeção; não executado |

**Limite remanescente e condição para rever o parecer:** A análise foi feita por leitura, com três entradas de quatro registros cada. Nem o candidato nem o ajuste proposto foram executados. Não examinei lista vazia, entrada apenas com `fechado` nem os dados de `chamados.json`. Os resultados das tabelas são previstos, e a conformidade do ajuste com R2 é demonstrada apenas nesses casos. Caso uma execução do ajuste, em cópia isolada, divergisse do previsto, eu reveria o meu parecer. Também seria revisto caso o contrato fosse alterado para permitir a ordenação por soma.
**Origem dos dados e da análise:** candidato/teste/entrada simulados; método próprio: inspeção; comando e trecho de saída: não realizado.
**Uso de IA neste registro:** ferramenta-modelo: Claude Code (Claude Opus 5.5); tarefa/contexto: forneci os guias de atividades e o enunciado da AV1.4 do repositório e pedi explicação da atividade, além de revisões sucessivas do registro contra R2 e o guia, com sugestões de redação e correções gramaticais finais; trecho aproveitado e minha verificação: redação do mecanismo da tabela, dos campos sobre o alcance e o trecho do teste, e sugestões incorporadas à comparação manter/ajustar e ao limite. Conferi manualmente IDs, ordens e somas contra R2 e o código do candidato.

**Revisão:** [x] comparação com R2; [x] alcance do teste; [x] ajuste/revalidação; [x] status; [ ] uma página.
