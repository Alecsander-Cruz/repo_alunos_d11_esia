# Glossário operacional e apoio à interpretação

Material prévio da disciplina D1.1. Os termos abaixo são usados para tomar decisões de engenharia; não constituem uma aula de treinamento de modelos. As traduções são explicações textuais, não proposta de sinais em Libras. O vocabulário deve ser compartilhado com o intérprete pelo fluxo da coordenação.

| Termo | Sentido usado nas aulas | Consequência prática |
|---|---|---|
| IA generativa | Sistemas que produzem conteúdo a partir de entradas e padrões aprendidos | Conteúdo produzido precisa ser avaliado para a tarefa |
| Aprendizado de máquina | Técnica em que o comportamento é aprendido de exemplos, e não escrito como regra | Padrão aprendido precisa ser testado; regra escrita pode ser lida |
| Treino e inferência | Treino ajusta os parâmetros do modelo antes do uso; na inferência eles ficam fixos e só o contexto muda | O que a tarefa exige e não estava no treino precisa vir no contexto |
| LLM — modelo de linguagem | Modelo que representa e gera sequências de tokens | A saída pode parecer adequada e ainda conter erro |
| Modelo | Componente que recebe entradas e produz saídas | Distinguir capacidade do modelo de recursos adicionados pelo produto |
| Produto | Interface e serviços construídos em torno de modelos | Histórico, arquivos, busca e limites dependem do produto |
| Ferramenta | Recurso que apoia ou executa uma ação, como editor ou terminal | Permissões e efeitos precisam ser compreendidos |
| Prompt — instrução de entrada | Texto/instruções enviados ao modelo com a tarefa | Tornar objetivo, restrições e forma de verificação explícitos |
| Token | Unidade de representação processada pelo modelo; não equivale necessariamente a palavra | Comprimento, orçamento e custo podem ser expressos em tokens |
| Contexto | Informações disponibilizadas para a tarefa na interação | Contexto relevante ajuda; excesso ou conflito também pode prejudicar |
| Janela de contexto | Limite de tokens que uma configuração consegue processar | Capacidade de entrada não garante uso correto de toda informação |
| Variabilidade | Diferenças entre saídas em execuções de uma tarefa | Registrar condições e verificar cada artefato relevante |
| Não-determinismo | Ausência de garantia de resultado idêntico nas condições utilizadas | Três saídas iguais não demonstram determinismo universal |
| Alucinação | Conteúdo sem apoio adequado nos fatos ou fontes da tarefa | Conferir a afirmação com referência ou teste independente |
| Latência | Tempo entre iniciar uma operação e obter o resultado definido para a medição | Identificar o que foi medido, incluindo espera e ambiente |
| Custo | Recursos consumidos para obter e verificar um resultado | Incluir revisão e retrabalho, além de eventual cobrança por uso |
| Critério de aceite | Condição observável para considerar uma tarefa atendida | Definir antes de julgar a resposta |
| Processo de software | Atividades que levam uma necessidade a um sistema em uso: requisitos, projeto, implementação, verificação e operação | Cada etapa deixa um artefato; código é um deles |
| Validação | Conferência do resultado contra a necessidade de quem pediu | Um artefato pode estar verificado e ainda não resolver o problema |
| Verificação | Conferência do artefato contra requisitos e evidências | Testes, inspeção e comparação são complementares |
| Oráculo de teste | Fonte do resultado esperado usada para julgar uma execução | Uma resposta gerada não vira referência correta só por ter sido gerada |
| Diff | Registro das diferenças entre versões de um arquivo | Revisar o que mudou, não apenas executar o resultado |
| Autonomia | Liberdade para escolher ou executar ações sem nova intervenção | Ajustar ao risco, reversibilidade e qualidade da verificação |
| HITL — humano no fluxo | Ponto em que uma pessoa decide, revisa ou autoriza | Aprovação de ação e verificação de qualidade têm funções diferentes |
| Fallback — alternativa de continuidade | Caminho disponível quando a opção principal falha | Manter atividade acessível sem depender de uma única ferramenta |
| Proveniência | Origem e condições de produção de uma informação | Separar medição, simulação, referência e inferência |
| Exploração | Investigação da oportunidade e do problema | Perguntas abertas e evidências iniciais |
| Protótipo | Demonstração delimitada de viabilidade | Funcionar em exemplo não demonstra operação sustentada |
| Piloto | Uso limitado, com usuários e critérios de acompanhamento definidos | Exigir escopo, responsável, monitoramento e regra de interrupção |
| Uso sustentado | Prática operada com responsabilidades, avaliação e manutenção | Observar desempenho e riscos continuamente |

## Distinções para reforçar oralmente

“Eu obtive uma resposta” descreve uma geração. “Eu aceitei uma resposta” exige critério e verificação.

“O teste passou” descreve um teste e seu alcance. Não implica que todos os requisitos, riscos e condições foram cobertos.

“O modelo roda localmente” descreve local de execução. Não garante determinismo, ausência de custo, privacidade de todo o fluxo ou adequação a qualquer tarefa.

“O resultado foi simulado para a aula” identifica uma ilustração. Não equivale a observação de comportamento de fornecedor ou modelo real.
