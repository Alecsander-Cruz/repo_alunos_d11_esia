# AV1.1 — Decidir o que delegar

**Individual — 35min — B1, 25/09/2026, 21h15–21h50 (Brasília).** Integra AV1, que vale 20% da nota pela média simples dos desafios dos blocos com presença. Consulte a [avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero escolher como realizar três tarefas de engenharia, comparar uma alternativa e justificar o que preciso verificar e assumir como responsabilidade técnica.

## Contexto e insumos

A equipe da organização fictícia Fila Clara recebe três pedidos. Todos os dados e cartões abaixo são simulados para esta avaliação. Trabalhe com o contrato fornecido; não é necessário consultar um modelo ou executar código.

- **R2:** a listagem inclui `aberto` e `em_andamento`, exclui `fechado` e preserva a ordem de entrada.
- **R3:** uma pessoa só pode visualizar chamados do próprio departamento, independentemente do estado ou da prioridade.
- [Contrato completo](../../caso/regras.md) e [template individual](template-registro.md).

| Cartão | Pedido e informações disponíveis | Resultado solicitado |
|---|---|---|
| C1 | A pessoa responsável pela manutenção quer critérios de aceite para R2. O contrato acima está aprovado; entradas são fictícias e válidas. | Rascunho de critérios que outra pessoa consiga verificar. |
| C2 | A equipe quer um teste de R3. Há dois departamentos, Oficina e Laboratório, e os estados aberto, em_andamento e fechado. | Proposta de entrada, saída esperada e justificativa do teste. |
| C3 | A operação pede autorização urgente para implantar uma alteração de visibilidade. Há apenas o resumo “facilitar acesso entre áreas”; a regra nova, os dados afetados, as verificações e o responsável pela aprovação não foram confirmados. | Decisão sobre autorizar a mudança em produção nas condições atuais. |

## Passos — 35min

1. **Ler — 5min.** Identifique entrada, saída e restrições de cada cartão. Defina o que permitiria aceitar o resultado antes de escolher a modalidade.
2. **Produzir individualmente — 20min.** Complete as três linhas do mapa. Use **sem IA**, **com assistência** ou **sem delegar a decisão**; não é obrigatório usar cada rótulo uma única vez. Descreva o processo sem IA, a tarefa eventualmente delegada, a verificação e quem assume o aceite. Para um cartão, compare outra modalidade plausível e indique uma condição concreta que mudaria sua escolha. Inclua ao menos um exemplo de evidência de aceite, com entrada/saída ou informação necessária.
3. **Revisar pela rubrica — 5min.** Confira se cada escolha está vinculada às condições do cartão e se a alternativa altera algum custo, risco ou responsabilidade identificável.
4. **Entregar — 5min.** Finalize um único registro individual de até uma página, usando o template. O canal acadêmico será informado pelo professor; este material não presume endereço de envio.

## Entrega e checklist

- [ ] Três linhas identificadas por C1–C3: processo sem IA, modalidade, justificativa, verificação e responsável.
- [ ] Trecho essencial de evidência para ao menos uma decisão; nos demais cartões, critério de aceite explícito.
- [ ] Uma alternativa comparada e a condição para rever uma escolha.
- [ ] Origem simulada dos cartões e declaração de IA, se utilizada.

**Critério de conclusão:** outra pessoa consegue relacionar cada modalidade ao pedido e localizar a verificação que sustenta o aceite. A entrega escrita é suficiente e não depende de fala ou câmera.

| Critério AV1 | Peso | Indicadores deste desafio |
|---|---:|---|
| Aplicação/decisão | 30% | Modalidade justificada para cada cartão; responsabilidade e alternativa comparada. |
| Evidência | 40% | Restrições localizadas nos cartões e exemplo examinável de entrada/saída ou informação de aceite. |
| Limites/alternativa | 30% | Fronteira da delegação, informação ausente e condição concreta para mudar a escolha. |

**Dica:** separe produzir uma sugestão de assumir a decisão de usá-la. IA é opcional e deve ser declarada; não são necessários conta, API, Git ou publicação. Não inclua dados do empregador.
