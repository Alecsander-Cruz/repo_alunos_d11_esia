# D1.1 — Engenharia de Software na Era da IA Generativa

Plano de ensino da turma · CESAR School · Turma 2026.2 · Revisão pedagógica: demonstrações docentes e avaliações individuais.
Escopo deste documento: disciplina D1.1, de 24h, integrante do módulo institucional M1, de 72h. Os canais de aula, envio e acompanhamento de acessibilidade serão comunicados pela organização.

## 1. Ficha técnica do módulo

| Campo | Definição |
|---|---|
| Curso | Pós-Graduação Lato Sensu em Engenharia de Software e IA — CESAR School |
| Escopo | D1.1 — Engenharia de Software na Era da IA Generativa, 24h; integra M1 institucional, de 72h |
| Professor/turma | Victor Freire · 2026.2 |
| Carga | 18h ao vivo (seis blocos de 180min) + 6h autônomas; hora de 60min |
| Método | Demonstração docente comentada, discussão orientada e avaliações individuais de aplicação |
| B1/B2/B3 | 25/09/2026, 19–22h; 26/09/2026, 9–12h e 14–17h |
| B4/B5/B6 | 02/10/2026, 19–22h; 03/10/2026, 9–12h e 14–17h |
| Público | 42 profissionais de software, familiaridade heterogênea com IA; remoto ao vivo; apoio de Libras a confirmar |
| Pré-requisitos | Leitura de código e noções de requisitos/testes; instalação local não é condição de avaliação |
| Ferramentas | Python e biblioteca padrão para demonstrações do caso; runtime de preparação 3.13.3; assistente no navegador intercambiável |
| Alternativa de acesso | Inspeção textual, saídas simuladas identificadas e transcrição de execução; sem API paga obrigatória |
| Normas institucionais | Limite de falta de 25%, gravação após 48h por 90 dias sem gerar presença e abono somente pela Secretaria; recuperação, atraso e lançamento ainda aguardam confirmação |

Horários de Brasília. Almoço 12–14h, fora da carga; encerramento dos sábados às 17h. Datas confirmadas no calendário da turma.

Ementa de referência: impactos da IA generativa na engenharia de software; fundamentos operacionais de LLM; papel e responsabilidade do engenheiro; aplicações no ciclo de desenvolvimento; qualidade, verificação e revisão; riscos e uso corporativo; maturidade e adoção.

## 2. Contexto: a trilha completa do curso

O curso tem 360h em cinco módulos de 72h. A progressão institucional é M1: fundamentos e desenvolvimento → M2: arquitetura e integração → M3: agentes e automação → M4: avaliação, segurança e operação → M5: produto e projeto aplicado. A disciplina inaugura o curso: pode pressupor experiência com software, mas não vocabulário comum de processo e de IA. Por isso B1 começa por um nivelamento com definições, antes da primeira demonstração.

| Disciplina de M1 | Carga | Contribuição e fronteira |
|---|---:|---|
| D1.1 — Engenharia de Software na Era da IA Generativa | 24h | Decidir quando usar IA, verificar saídas, reconhecer riscos e sustentar decisões com evidência |
| D1.2 — Desenvolvimento Assistido por IA | 24h | Desenvolver fluência operacional no editor e com agente de codificação; recebe critérios de delegação e revisão de D1.1 |
| D1.3 — Prompting Técnico, Especificação e Contexto | 24h | Aprofundar especificação verificável, critérios de aceite e organização/comparação de contexto |

O salto de D1.1 é passar de impressões sobre uma ferramenta para decisões justificadas. A implementação de agentes, subagentes, hooks e MCP pertence às disciplinas posteriores e não compõe as competências ou avaliações desta disciplina.

## 3. Filosofia pedagógica do módulo

**Nivelar antes de engatar.** Parte da turma já atua no mercado e parte chega direto da graduação. B1 dedica 59min a definições de processo de software, verificação e validação, IA, aprendizado de máquina e funcionamento de LLMs, com um fluxograma por conceito, e só depois aplica essa base a uma decisão de delegação. Os blocos seguintes retomam essas definições e indicam leitura de apoio para estudo fora de sala.

**Demonstração que torna o raciocínio observável.** O professor formula a tarefa, define critério, faz uma previsão, opera a ferramenta, confronta a saída e revê a decisão. A aula mostra também incerteza, limite e alternativa, em vez de apenas uma execução bem-sucedida. B1 reserva 35min a esse processo, depois do nivelamento; os demais blocos, 75min. Em B3, um ato de 25min é execução acompanhada dos estudantes, dentro dos mesmos 75min, mantendo 50min de demonstração docente.

**Avaliação individual de transferência.** Após a demonstração e a discussão, o estudante aplica os conceitos a um insumo diferente durante 35min. O desempenho aparece em decisão, evidência e argumento próprios. Não há nota por presença, repetição da solução ou participação oral; não há entrega coletiva obrigatória.

**Exigência de pós-graduação.** Analisar, avaliar e propor são ações centrais: comparar alternativas sob restrições, formular verificação independente, examinar contraprova e integrar literatura à recomendação final. AV3 reutiliza duas referências de L0, com localização e análise de limites.

**Autonomia proporcional à consequência.** Revisão técnica acompanha a produção; autorização humana é explicitada antes de ação com consequência grave. Decisão acadêmica não depende de uma ferramenta específica. O caso usa dados fictícios, sem material do empregador.

**Equidade e carga verificável.** Materiais acessíveis antecipados, instruções escritas e micropausas de fala; resposta escrita é evidência válida. A alternativa textual usa a mesma rubrica. L0, AV2 e AV3 somam 6h, sem pesquisa, defesa ou implementação extra obrigatória.

## 4. Tendências 2026 (pesquisa aplicada)

Os recortes abaixo são questões para análise dos tópicos da disciplina, sem afirmar novidades ou liderança de produtos em 2026 nem uma pesquisa externa atualizada de tendências. A bibliografia básica teve título, autoria e registro conferidos no diagnóstico, não uma revisão sistemática atualizada.

### B1 — Mudança no trabalho e evidência

Qual parte de uma tarefa muda com assistência e qual responsabilidade permanece? Distinguir relato, demonstração e evidência de produtividade; não converter uma experiência em alegação causal geral.

### B2 — Limites operacionais

Como contexto, informação ausente, variabilidade, custo e latência afetam uma decisão? Três repetições por condição servem à observação exploratória; resultados iguais também são válidos. Execução local não implica custo zero, determinismo ou latência menor.

### B3 — Assistência ao longo do ciclo

Onde há benefício, retrabalho e intervenção humana em requisitos, testes e documentação? A análise observa o fluxo e suas dependências, preservando o aprofundamento operacional para D1.2.

### B4 — Verificação independente

Como distinguir um artefato convincente de um correto? Relacionar requisito, contraexemplo e evidência; discutir dívida técnica, autoria e formação de profissionais iniciantes sem tomar a autoconfiança da ferramenta como validação.

### B5 — Governança observável

Que dados podem entrar, quem decide e como se verifica uma regra? Retenção, permissões, segurança, licenciamento e portabilidade são perguntas para consulta às políticas e condições aplicáveis, sem conclusão jurídica presumida.

### B6 — Adoção e maturidade

Que evidência diferencia exploração, protótipo, piloto e uso sustentado? Definir próximo passo, condição de interrupção e métrica antes de recomendar expansão.

## 5. Conceitos-base da ferramenta base (glossário operacional)

| Conceito | O que é | Onde aparece | Quando usar |
|---|---|---|---|
| Modelo | Componente que produz respostas a partir da entrada | Identificação exposta pela interface, quando disponível | Registrar qual componente foi usado, sem confundi-lo com o aplicativo |
| Produto/interface | Aplicação que reúne modelo e recursos de interação | Navegador e tela de conversa | Descrever o ambiente e seus limites observáveis |
| Sessão/contexto | Informações fornecidas e histórico disponíveis naquela interação | Conversa, anexos autorizados e instruções | Controlar o que foi mantido ou alterado entre tentativas |
| Token/janela de contexto | Unidade de processamento e limite de informação do modelo | Documentação ou medição disponível | Explicar limites; marcar como não disponível quando a interface não os expõe |
| Variabilidade | Possibilidade de resultados distintos sob entradas aparentemente iguais | Comparação de execuções | Planejar observação e verificação; não exigir diferença artificial |
| Alucinação | Conteúdo afirmado sem suporte suficiente ou incorreto | Resposta, justificativa, referência ou código | Separar alegação da evidência usada para aceitá-la |
| Critério de aceite | Condição verificável para aceitar um resultado | Enunciado, requisito e registro de revisão | Definir o esperado antes de examinar a resposta |
| Teste independente | Checagem fundada no requisito, além do artefato avaliado | Teste, caso de fronteira ou inspeção documentada | Verificar código, documentação e afirmações |
| Runtime Python | Ambiente que executa o código didático | Terminal; referência de preparação 3.13.3 | Reproduzir B3/B4; não é versão de modelo de IA |
| Evidência/limite | Registro observável e alcance da conclusão | Portfólio individual | Sustentar decisão sem extrapolar a atividade |
| Saída didática simulada | Texto construído para análise, identificado como simulação | Pacote de contingência offline | Assegurar participação sem conta, cota ou execução; não serve como medição real de modelo |

## 6. Pré-requisitos e setup

- A organização comunicará sala, ambiente da turma, canal de entrega e acompanhamento de acessibilidade quando confirmados.
- Disponibilizar previamente enunciados textuais, glossário, código fictício e pacote de contingência; usar fonte legível e descrever o conteúdo exibido.
- Selecionar interface no navegador apenas se houver acesso gratuito disponível e permitido na data da aula. Não pressupor licença de turma, API, conta ou cota; validar antes do encontro.
- Para execução local em B3/B4, preparar Python 3.13.3 e biblioteca padrão; o aluno sem instalação acompanha o mesmo código e analisa resultados fornecidos, com origem identificada.
- Não exigir download de LLM local, chave de API, pagamento ou dados do empregador para atingir os objetivos.

**Smoke test de preparação:** abrir o material; registrar a versão de Python com `python --version` se o caminho local for usado; abrir uma sessão de IA e pedir a reformulação de um requisito fictício; salvar entrada, saída e identificação exposta. Se não houver acesso, abrir a saída simulada correspondente e registrar a modalidade. No kit de B3/B4, o procedimento de execução está documentado em testes/README.md: nove verificações, com seis sucessos e três falhas intencionais no material inicial. A transcrição em apoio/resultado-textual.md registra a execução de preparação.

**Contingência equivalente:** o pacote textual deve conter todos os insumos, respostas simuladas rotuladas e transcrições verificadas de execução do código. Quem o utiliza analisa critérios, limites e decisões com a mesma rubrica; não declara ter feito chamadas ou medições que não executou. No B2, discute como desenharia o experimento e compara exemplos, identificando a limitação.

## 7. Mapa de competências e outputs do módulo

| Objetivo | Desempenho esperado | Instrumentos |
|---|---|---|
| O1 — Mudanças e permanências | Distinguir produção de artefato de responsabilidade e comparar alternativa sem IA | AV1.1, AV3 |
| O2 — Capacidades e limites operacionais | Relacionar contexto, variabilidade e informação ausente à confiança na decisão | AV1.2, AV2, AV3 |
| O3 — Ciclo e autonomia | Delimitar etapa assistida, responsabilidade e condição de aceite | AV1.1/3, AV2, AV3 |
| O4 — Verificação e responsabilidade | Formular critério independente, localizar evidência e sustentar revisão | AV1.2/3/4, AV2, AV3 |
| O5 — Riscos e mecanismos | Formular controles proporcionais, responsáveis e evidência de funcionamento | AV1.5, AV3 |
| O6 — Maturidade e adoção | Classificar iniciativa por fatos e propor avanço/interrupção verificáveis | AV1.6, AV3 |

Fluência em Python ou fornecedor específico não é competência avaliada. A precisão do argumento e a capacidade de auditar sua evidência determinam o nível da rubrica.

## 8. Plano de aulas detalhado

| Etapa | B1 | B2–B6 |
|---|---:|---:|
| Abertura/retomada; em B1, quebra-gelo e contrato | 26min | 10min |
| Fundamentos aplicados; em B1, nivelamento | 59min | 30min |
| Demonstração; em B3, execução acompanhada no ato 2 | 35min | 75min |
| Discussão orientada; em B1, com mapa de delegação | 15min | 20min |
| Avaliação individual AV1 | 35min | 35min |
| Fechamento | 10min | 10min |
| **Total** | **180min** | **180min** |

Dois atos de 15+20min em B1, com o mapa de delegação preenchido na discussão; três atos de 25+25+25min nos demais. Em B3, o segundo ato (15h05–15h30) é execução acompanhada: cada estudante verifica R1 no próprio ambiente por execução ou inspeção documentada, com registro pessoal sem entrega nem nota. São 385min de demonstração docente e 25min de execução acompanhada no conjunto da disciplina. AV1: leitura 5min, produção 20min, revisão 5min, entrega 5min. Discussão com 2–3 contribuições curtas e chat; sem salas simultâneas. Nenhuma atividade é contada duas vezes. Planos, roteiros e instruções dos slides detalham os mesmos intervalos.

### B1 — O que muda na engenharia de software

**25/09, 19–22h.** Abertura com quebra-gelo de uma frase por pessoa (nome, de onde fala, se trabalha e com o quê) e contrato da disciplina. Nivelamento: processo de software e seus artefatos; verificação, validação e critério de aceite; IA, aprendizado de máquina e LLM; como um LLM gera texto; modelo, produto e ferramenta; IA no processo e limite de alegações de produtividade; delegação e responsabilidade. Demonstração: comparar documentação manual de R1 com saída solicitada pelo professor a um assistente, quando disponível, ou candidato simulado identificado. Discussão: o que a assistência muda e o que continua sob responsabilidade profissional, com o mapa de delegação preenchido pelo professor. **AV1.1, 21h15–21h50:** três cartões novos sobre R2, R3 e mudança em produção; mapa individual com decisão, alternativa, evidência e limite. Fechamento orienta o diagnóstico sem nota, a responder até 26/09, 8h, a L0 e a leitura de nivelamento, sem entrega.

### B2 — Fundamentos que afetam decisão técnica

**26/09, 9–12h.** Contexto, tokens/janela, variabilidade, informação ausente, alucinação, custo e latência. Demonstração: protocolo A/B, coleta real pelo professor quando houver acesso ou inspeção das seis saídas simuladas identificadas; critério anterior à coleta/leitura, comparação e limites da observação. Resultados reais e simulados são mantidos separados. Não inventar medições de modelo. **AV1.2, 11h15–11h50:** avaliar duas respostas novas, verificar uma classificação e uma inferência sobre determinismo. Registros iguais são válidos; nenhuma comparação curta comprova desempenho geral ou produtividade causal.

### B3 — IA no ciclo de desenvolvimento

**26/09, 14–17h.** Requisitos, implementação, teste, revisão, documentação e leitura de legado. Demonstração: percorrer R1 por requisito, teste e documento; professor solicita sugestões ao assistente quando disponível, verifica e registra aceite, usando material simulado identificado como contingência. No ato 2, cada estudante verifica R1 no próprio ambiente durante 25min, por execução ou rastreamento textual, sem entrega ou nota adicional. **AV1.3, 16h15–16h50:** aplicar o percurso a R2, com três casos, ordem de entrada, documentação e decisão de autonomia. Fechamento orienta AV2, estudo técnico de 2h, com candidato distinto do exemplo de aula.

### B4 — Qualidade, verificação e responsabilidade

**02/10, 19–22h.** Plausibilidade versus correção, fronteiras, teste independente, dívida técnica e responsabilidade. Retomar padrões de AV1/AV2 por amostra disponível, sem presumir correção integral imediatamente após o prazo. Demonstração: revisar candidatos existentes de código/teste/documento, examinar falhas e corrigir em cópia com revalidação. **AV1.4, 21h15–21h50:** examinar proposta nova que ordena a listagem de ativos; parecer individual com critério, verificação, decisão, ajuste e revalidação.

### B5 — Riscos, segurança e uso corporativo

**03/10, 9–12h.** Dados, retenção, permissões, licenciamento e dependência de fornecedor como condições a verificar. Demonstração: construir política para tarefas fictícias e simular exceção, relacionando mecanismo e evidência. **AV1.5, 11h15–11h50:** decidir sobre pedido hipotético de uso de log interno sem condições de fornecedor confirmadas; alternativa viável e duas regras operáveis. Não exigir parecer jurídico nem dado real.

### B6 — Maturidade, adoção e próximos passos

**03/10, 14–17h.** Exploração, protótipo, piloto e uso sustentado; estágio depende de evidência, não de intenção. Demonstração: classificar a iniciativa e desenhar próximo passo com métrica e condição de interrupção. **AV1.6, 16h15–16h50:** analisar novo cartão com piloto planejado, mas sem execução; comparar estágio alternativo e justificar decisão. Fechamento: diagnóstico sem nota 3min, AV3 5min, passagem para D1.2 2min. Encerrar às 17h.

## 9. Projeto integrador do módulo

O caso transversal Fila Clara sustenta demonstrações e avaliações. O produto integrador é **AV3, parecer individual fundamentado**, apoiado nas evidências das avaliações e nas leituras, sem construir aplicação completa. O contrato R1–R4 define prioridade, estados ativos, acesso por departamento e documentação coerente.

| Trabalho autônomo | Carga | Entrega | Prazo proposto, Brasília |
|---|---:|---|---|
| L0 — leitura orientada | 2h | Fichamento até 400 palavras; dois textos, afirmações localizadas e limites | 02/10/2026, 18h59 |
| AV2 — estudo técnico | 2h | Até duas páginas + até duas páginas de anexo; requisito, matriz de verificação, evidência e decisão | 30/09/2026, 23h59 |
| AV3 — parecer integrador | 2h | Até três páginas + até duas páginas de evidências/referências; decisão, literatura, verificação, riscos e maturidade | 10/10/2026, 23h59 |

AV2 usa candidato próprio de acesso e documentação, sem depender de conteúdo posterior a B3. AV3 aplica duas referências já lidas e reutiliza os registros, sem pesquisa extra. O [índice de avaliações](avaliacoes/README.md) reúne enunciados e modelos; o [estudo autônomo](estudo-autonomo.md) delimita esforço e procedência.

## 10. Avaliação e rubricas

**AV1 20% + AV2 30% + AV3 50%.** AV1 é a média dos desafios dos blocos com presença registrada. Todas as notas estão entre 0 e 10. L0 é formativa e não acrescenta peso. Pesos e prazos são proposta docente; normas administrativas seguem a instituição.

| Instrumento | Critérios internos, soma 100% |
|---|---|
| AV1, cada desafio | Aplicação/decisão 30%; evidência 40%; limites/alternativa 30% |
| AV2 | Recorte/requisito 15%; estratégia 25%; evidência/rastreabilidade 30%; decisão/alternativa 20%; procedência/limites 10% |
| AV3 | Problema/alternativas 15%; autonomia/responsabilidade 15%; evidências 25%; riscos/mecanismos 20%; maturidade/próximo passo 15%; fundamentação/argumentação 10% |

Níveis por critério: 0 ausente, 1 incipiente, 2 adequado, 3 consistente. Nota = 10 × soma(peso × nível/3); todos os níveis 2 produzem 6,67. As [rubricas públicas completas](avaliacao.md) descrevem os níveis com comportamentos observáveis, fórmula, exemplo de cálculo, consulta, autoria, devolutiva e revisão de nota.

IA é permitida com declaração e julgamento próprios. Avaliar aplicação a caso distinto, evidência localizada, comparação e limite; não aparência da resposta, frequência, câmera, quantidade de prompts ou testes verdes. Execução e inspeção textual são modalidades válidas; a origem do resultado deve estar clara. A avaliação é manual.

### Presença, ausência e cálculo de AV1

Os seis desafios permanecem avaliativos. **AV1 é a média simples das notas dos blocos com presença registrada, sem reposição de desafio por ausência.** O bloco ausente fica fora da soma e do denominador; a falta permanece registrada para frequência. Com seis presenças, a média usa as seis notas; com cinco presenças, usa cinco. Exemplo: notas 8, 7, 9, 8 e 8 em cinco blocos com presença resultam em AV1 = 40 ÷ 5 = 8,0.

Presença e entrega são registros distintos: o bloco com presença integra o denominador mesmo quando não há entrega. Sem evidência, os critérios correspondentes recebem nível 0. Uma barreira de acesso registrada segue o encaminhamento institucional antes da consolidação; não deve ser confundida com ausência ou falta de competência. Se não houver nenhum bloco com presença, não dividir por zero nem inventar uma média: registrar AV1 sem média calculável e encaminhar o lançamento à Secretaria. A regra de frequência permanece independente da nota.

### Devolutiva de AV1

O professor registra **nível 0–3 e evidência curta por critério em todos os desafios dos blocos com presença**. A devolutiva individual desenvolvida — uma força, uma lacuna e uma ação de melhoria — ocorre em **AV1.3 e AV1.6**. Nos demais desafios, a turma recebe devolutiva coletiva, sem identificação nominal, além dos níveis registrados individualmente. Se houver ausência em AV1.3 ou AV1.6, a devolutiva individual é transferida para outro desafio realizado, sem duplicá-lo, priorizando o mais recente daquele fim de semana; havendo dois desafios realizados, são duas devolutivas individuais. AV2 e AV3 mantêm devolutiva individual.

Pedidos de revisão podem indicar critério e evidência de qualquer desafio, inclusive dos que tiveram devolutiva coletiva. A escolha do formato de feedback não altera os pesos nem os descritores das rubricas.

### Frequência, gravações e abono

O limite institucional de falta é **25% da carga de 24h (6h)**. Acima desse limite, há reprovação por falta, independentemente da nota. A frequência segue o registro acadêmico institucional; excluir um bloco ausente da média de AV1 não abona a falta.

As gravações são liberadas **48h após a aula**, ficam disponíveis por **90 dias** e servem apenas à revisão: assistir à gravação **não gera presença**. Abono de falta é atribuição exclusiva da **Secretaria, mediante comprovante**. Recuperação, prazos de lançamento e canais acadêmicos serão comunicados após confirmação institucional.

## 11. Repositório de apoio

O [material do aluno](README.html) contém contrato, seis dados sintéticos, código, nove verificações, saídas simuladas, transcrição e dossiês de avaliação. As demonstrações usam o caso; AV1, AV2 e AV3 têm enunciados, entregáveis, modelos e critérios próprios.

O material inicial contém três divergências funcionais intencionais e sua referência passa nas nove verificações. Elas apoiam demonstração e revisão; não obrigam todos os desafios a corrigir código. AV2 examina candidato isolado e AV1.4 apresenta outra proposta para análise, sem alterar a base do caso.

A turma recebe o ZIP discente com este plano de ensino, os enunciados e os materiais do caso. As [rubricas públicas](avaliacao.md) apresentam critérios, níveis e regras de cálculo.

## 12. Referências e fontes

**Bibliografia básica:** títulos, autoria e registros conferidos no diagnóstico; não se afirma leitura integral nem atualização sistemática para 2026.

- FAN, Angela et al. *Large Language Models for Software Engineering: Survey and Open Problems*. 2023. [Registro e versão v4](https://arxiv.org/abs/2310.03533v4).
- HOU, Xinyi et al. *Large Language Models for Software Engineering: A Systematic Literature Review*. Submissão de 2023; [versão v6 de 2024](https://arxiv.org/abs/2308.10620v6).
- NGUYEN-DUC, Anh et al. *Generative Artificial Intelligence for Software Engineering — A Research Agenda*. 2023. [Registro e versão v1](https://arxiv.org/abs/2310.18648v1).

**Referência operacional:** [documentação oficial do Python 3.13](https://docs.python.org/3.13/), para a biblioteca padrão do caso. O número 3.13.3 é o runtime local de referência, não garantia de reprodução de saídas de IA. A documentação da interface de IA deve ser conferida quando o professor escolher o serviço; nenhum fornecedor integra o contrato pedagógico.

## 13. Apêndices: templates e checklists

**Registro de avaliação:** identificação acadêmica; instrumento; insumo/versão; critério; método; entrada; esperado; encontrado; decisão; alternativa; limite; procedência e assistência. Somente os campos pertinentes ao enunciado precisam ser preenchidos; não exigir execução onde o objetivo é decisão organizacional.

**AV1:** um registro individual até uma página por bloco. **AV2:** requisito → matriz de quatro casos → código/documento → verificação → decisão/alternativa → revalidação. **AV3:** problema/alternativas → autonomia → evidência/contraponto → dois riscos/controles → estágio/próximo passo → fundamentação em duas referências.

**Checklist do estudante:** usar apenas insumos autorizados; aplicar ao caso; identificar fonte e método; separar esperado e encontrado; não atribuir execução à inspeção; justificar decisão; examinar limite/alternativa; declarar assistência; revisar pela rubrica e entregar no canal institucional.

**Ficha docente de correção:** critério | peso | nível 0–3 | evidência localizada | comentário. A AV1 não tem reposição por ausência. Recuperação, atrasos e prazo de lançamento dependem das regras acadêmicas ainda a confirmar.
