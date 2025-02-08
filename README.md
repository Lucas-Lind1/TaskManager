# Task Manager API

Este projeto é um gerenciador de tarefas serverless desenvolvido com Python, utilizando AWS Lambda, DynamoDB e API Gateway. A aplicação fornece uma API REST para gerenciar tarefas, permitindo criar, listar, atualizar e excluir tarefas.

## Estrutura do Projeto

```
task-manager
├── src
│   ├── app.py                # Ponto de entrada da aplicação
│   ├── controllers           # Controladores para gerenciar as tarefas
│   │   ├── create_task.py    # Função para criar novas tarefas
│   │   ├── list_tasks.py     # Função para listar tarefas
│   │   ├── update_task.py    # Função para atualizar tarefas existentes
│   │   └── delete_task.py    # Função para excluir tarefas
│   ├── models                # Modelos de dados
│   │   └── task.py           # Estrutura do modelo de dados da tarefa
│   ├── services              # Serviços de interação com o DynamoDB
│   │   └── dynamodb_service.py # Funções para acessar o DynamoDB
│   └── utils                 # Utilitários
│       └── response.py       # Funções para formatar respostas da API
├── requirements.txt          # Dependências do projeto
├── serverless.yml            # Configuração do Serverless Framework
└── README.md                 # Documentação do projeto
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd task-manager
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para iniciar a aplicação localmente, execute o seguinte comando:

```
uvicorn src.app:app --reload
```

## Endpoints da API

- `POST /tasks`: Cria uma nova tarefa.
- `GET /tasks`: Lista todas as tarefas.
- `PUT /tasks/{id}`: Atualiza uma tarefa existente.
- `DELETE /tasks/{id}`: Exclui uma tarefa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.