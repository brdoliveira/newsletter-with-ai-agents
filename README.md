# Automação de Newsletter da Crew AI
![fluxo-agentes](https://github.com/brdoliveira/newsletter-with-ai-agents/assets/66849496/a9be09e0-f39f-43eb-974c-3d3f1aee20b0)


## Visão Geral
Este documento README descreve o propósito e a funcionalidade de um código Python projetado para automatizar o processo de geração de newsletters, utilizando uma equipe de agentes especializados. Cada agente realiza tarefas distintas, como explorar conteúdo, escrever e criticar, para garantir que as newsletters sejam informativas, envolventes e de alta qualidade. A automação lida com newsletters baseadas em conteúdo de relatórios do Reddit e Google, além de críticas de blogs.

## Componentes

### CrewAI
O módulo `crewai` apresenta as classes centrais necessárias para a automação:

- `Process`: Enumera o tipo de fluxo de processo que a equipe seguirá, neste caso, sequencial.
- `Crew`: Gerencia um grupo de agentes e atribui tarefas a eles com base no processo especificado.

### Tarefas
Definidas em `tasks.py`, a classe `TasksNewsletter` fornece acesso a várias tarefas, como gerar relatórios do Reddit e Google, criar conteúdo de blog e realizar críticas.

### Agentes
Definidos em `agents.py`, a classe `AgentsNewsletter` abriga os agentes responsáveis pela execução das tarefas:

- `Explorer`: Busca por conteúdo.
- `Writer`: Elabora o conteúdo da newsletter.
- `Critic`: Avalia e sugere melhorias para o conteúdo.

## Uso
O script inicializa as tarefas e os agentes, formando então duas equipes, `reddit_crew` e `google_crew`, cada uma responsável por gerar newsletters a partir de relatórios do Reddit e Google, respectivamente. Ambas as equipes seguem um processo sequencial, onde cada agente completa sua tarefa antes de passá-la para o próximo. O parâmetro `verbose` definido como 2 possibilita um registro detalhado ao longo do processo.

Após inicializar as equipes, o script inicia o processo de geração da newsletter para o conteúdo do Reddit e Google, imprimindo os resultados no console.

## Como Executar
1. Certifique-se de ter o Python 3.x instalado.
2. Instale os pacotes necessários: os módulos `crewai`, `tasks` e `agents` devem estar disponíveis no seu ambiente. Isso pode exigir a configuração de um pacote local, caso esses módulos sejam construídos sob medida para este projeto.
3. Execute o script: `python <nome_do_script>.py`

## Dependências
- Python 3.x
- Módulos personalizados: `crewai`, `tasks`, `agents`. Garanta que estes estejam instalados ou disponíveis no diretório do seu projeto.

## Contribuição
Sinta-se à vontade para fazer fork do repositório e enviar pull requests para contribuir com o desenvolvimento do processo de automação de newsletters. Certifique-se de seguir os padrões de codificação e escrever testes para novas funcionalidades.


## 🧐 Autor
<a href="https://github.com/brdoliveira" title="Github"><b>Bruno Ribeiro</b> ⚓</a>
