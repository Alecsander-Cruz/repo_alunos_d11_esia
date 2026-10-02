# Registro individual — AV1.3

**Limite: uma página.** Estudante: Alecsander D. Cruz — Data: 02/10/2026
**O que a listagem e a documentação precisam cumprir, conforme R2/R4:** incluir os estados `aberto` e `em_andamento`, excluir o estado `fechado`, manter a ordem de entrada. A documentação precisa descrever exatamente essas mesmas regras.

| Caso / estado a verificar | Entrada (IDs e ordem) | IDs esperados na ordem | Obrigação de R2 e como verificar |
|---|---|---|---|
| 1 / aberto | TR-33 | TR-33 | Incluir no resultado o TR-33 (aberto). A saída precisa ser apenas o id TR-33. |
| 2 / em_andamento | TR-31 | TR-31 | Incluir no resultado o TR-31 (em_andamento). A saída precisa ser apenas o id TR-31. |
| 3 / fechado | TR-32 | [] | Excluir do resultado o TR-32 (fechado). A saída precisa ser uma lista vazia, sem listar o TR-32. |

**Entrada combinada TR-31, TR-32, TR-33 → IDs esperados:** [TR-31, TR-33]
**Como conferiria a ordem (compare a posição dos IDs na entrada e na saída esperada):** Na entrada o TR-31 está na primeira posição e o TR-33 na última. Na saída o TR-31 vai continuar na primeira posição e o TR-33 vai passar para a segunda posição, obedecendo a regra da ordem de entrada. Já o TR-32 não deve estar presente na lista de saída devido ao seu estado ser `fechado`.
**Documentação proposta (até três frases):** A regra R2 prevê que a função `listar_ativos` inclua na saída os chamados da lista de entrada que possuam os estados `aberto` ou `em_andamento`, e exclua os chamados que possuam o estado `fechado`. A regra também exige que a ordem de entrada dos chamados seja preservada na saída. 

**Etapa em que admitiria IA / tarefa que ela faria / pessoa responsável por conferir:** Usar IA na etapa de fazer a documentação proposta, de acordo com R2. Eu seria o responsável por conferir e aprovar, tendo em vista que a IA não deveria decidir o aceite.
**O que essa pessoa deve verificar antes de aprovar:** Se o texto fala sobre os dois estados incluídos (`aberto`, `em_andamento`), se fala sobre o estado excluído (`fechado`), e se fala sobre a preservação da ordem de entrada. Conferir também se a IA não alucinou e incluiu algo que a R2 não dita, como por exemplo alguma ordenação diferente da de entrada. Conferir se a documentação estaria de acordo com as saídas esperadas dos 3 casos e a saída combinada.
**Alternativa sem IA e comparação:** Escrever o texto manualmente, como fiz. Demora um pouco mais pra escrever mas diminui a chance de alucinação. Com IA, o texto sai mais rápido mas eu teria que conferir de qualquer maneira. Por ser algo de baixo risco e fácil de ser conferido contra R2, poderia ser admitido o uso de IA.
**O que os casos não verificam e o que me faria rever a aprovação:** Não distinguem preservar a ordem de entrada de ordenar por ID; a entrada combinada já está em ordem crescente de ID, o que faria uma implementação de ordenação por ID passar sem ser detectada. Também não cobrem lista de entrada vazia ou apenas com chamados `fechado`, nem o comportamento real do código, já que as saídas são esperadas por R2 e não executadas. A aprovação seria revista se a execução divergisse dos resultados esperados, caso a R2 fosse alterada ou se uma combinação [TR-33, TR-31] retornasse os IDs em outra ordem.

**Origem dos dados e como fiz a análise:** entrada fictícia do enunciado; esperado por contrato: R2; inspeção própria: contrato R2, template de registro; execução opcional (comando/resultado, se houver): não realizada.
**Uso de IA neste registro:** ferramenta-modelo visível: Claude Code (extensão VS Code), modelo Claude Opus 5.5; contexto/tarefa: enunciado do exercicio, contrato de regras / explicar enunciado, conferir meus registros e correção de grafia; trecho aproveitado e minha verificação: "lista de entrada vazia e apenas chamados `fechado`" / Comparar tudo com R2 e o enunciado.

**Revisão:** [x] três estados; [x] ordem; [x] texto; [x] aceite/limite; [ ] uma página.
