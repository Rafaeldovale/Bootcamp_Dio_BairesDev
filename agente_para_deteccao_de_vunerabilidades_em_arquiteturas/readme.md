Análise de Ameaças de Arquitetura com IA 

Este projeto implementa uma API RESTful capaz de analisar diagramas de arquitetura de software e gerar uma análise de ameaças automatizada, utilizando o poder da inteligência artificial generativa. A solução integra o poder do modelo de IA multimodal do Azure OpenAI para processar a imagem do diagrama e, com base em metadados da aplicação, gerar uma análise detalhada utilizando a metodologia STRIDE.

Metodologia: STRIDE
O sistema de análise de ameaças é baseado na metodologia STRIDE, que classifica as ameaças de segurança em seis categorias:

Spoofing (Falsificação de Identidade)

Tampering (Violação de Integridade)

Repudiation (Repúdio)

Information Disclosure (Divulgação de Informações)

Denial of Service (Negação de Serviço)

Elevation of Privilege (Elevação de Privilégio)

Tecnologias Utilizadas
Backend: Python

Framework: FastAPI

Serviço de IA: Azure OpenAI Service (com modelo que suporta processamento de imagens)

Bibliotecas Python:

dotenv: Para gerenciar as variáveis de ambiente.

openai: Para interagir com a API do Azure OpenAI.

fastapi: Para construir a API.

uvicorn: Para servir a aplicação FastAPI.

python-multipart: Para lidar com o upload de arquivos via formulário.

Estrutura do Projeto
A estrutura de pastas do projeto é organizada de forma simples e direta, facilitando a configuração e execução.

/modulo-1/
|-- fontend
    |-- index.html
|-- backend
    |-- main.py                   # Arquivo para as variáveis de ambiente
|-- README.md                     # Este arquivo de documentação


Configuração e Instalação
Pré-requisitos
Python 3.8 ou superior

Acesso a um serviço Azure OpenAI com um modelo de implantação que suporte processamento de imagens (ex: GPT-4 com gpt-4-vision-preview).

1. Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e configure as variáveis de ambiente necessárias para autenticar com o Azure OpenAI.

AZURE_OPENAI_API_KEY="sua_chave_de_api_aqui"
AZURE_OPENAI_ENDPOINT="https://seu-endpoint.openai.azure.com/"
AZURE_OPENAI_API_VERSION="2023-12-01-preview"
AZURE_OPENAI_DEPLOYMENT_NAME="seu_nome_de_deploy_aqui"
2. Instalação de Dependências
Instale todas as bibliotecas Python necessárias executando o seguinte comando:

Bash

pip install "fastapi[all]" uvicorn openai python-dotenv
3. Executar a Aplicação
Para iniciar o servidor da API, execute o seguinte comando na pasta do projeto:

Bash

uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000. A documentação interativa estará disponível em http://127.0.0.1:8000/docs.

Como Usar a API
A API expõe um único endpoint (/analisar_ameacas) que recebe uma imagem e dados adicionais da aplicação para gerar a análise.

Endpoint
POST /analisar_ameacas

Parâmetros do Formulário (Form Data)
A requisição deve ser enviada como multipart/form-data com os seguintes campos:

imagem: file (Imagem do diagrama de arquitetura, em formatos como PNG ou JPEG).

tipo_aplicacao: string (Ex: "API REST", "Aplicativo Web", "Aplicativo Mobile").

autenticacao: string (Ex: "OAuth2.0", "Token JWT", "Sem autenticação").

acesso_internet: string (Ex: "Sim", "Não").

dados_sensiveis: string (Ex: "Senhas, dados de cartão de crédito", "Dados pessoais").

descricao_aplicacao: string (Uma breve descrição textual da aplicação).

Front-end (Interface de Usuário)
A interface do usuário é uma página web simples em HTML, CSS e JavaScript que serve como a "ponte" entre o usuário e a API de análise de ameaças. Ela permite que o usuário faça o upload do desenho de arquitetura e insira os metadados necessários para a análise.

O front-end é responsável por:

Coletar Dados: Apresenta um formulário amigável para o usuário preencher os detalhes da aplicação e selecionar o arquivo de imagem.

Enviar Requisição: Empacota os dados do formulário e a imagem em uma requisição POST para o endpoint da API (/analisar_ameacas).

Exibir Resultados: Recebe a resposta da API (o JSON contendo a análise STRIDE) e a exibe de forma clara na página. O front-end também inclui uma visualização interativa de um grafo de ameaças usando a biblioteca Cytoscape.js.

Tecnologias do Front-end
HTML: Estrutura da página.

CSS: Estilização básica com o framework Bootstrap 5.3.

JavaScript: Lógica para interagir com o formulário, enviar dados para a API e processar a resposta.

Cytoscape.js: Biblioteca JavaScript para criar e visualizar grafos, que são usados para demonstrar um exemplo de visualização de ameaças.

Como Usar o Front-end
Para usar a interface, você precisa primeiro garantir que o seu backend está rodando. Siga os passos de configuração e execução da API que já detalhamos.

Salve o arquivo: Salve o código HTML fornecido em um arquivo chamado index.html.

Abra o arquivo: Simplesmente abra o arquivo index.html em seu navegador web (Google Chrome, Firefox, etc.). Não é necessário um servidor web para esta etapa.

Use a interface: Preencha o formulário e faça o upload de um desenho de arquitetura. Clique em "Analisar" para enviar os dados para a sua API local e ver o resultado na tela.

Créditos e Agradecimentos

Este projeto foi desenvolvido em colaboração, com o objetivo de aplicar e documentar conceitos de segurança cibernética, inteligência artificial e desenvolvimento web.


Professor: [Henrique Eduardo Souza]

Curso/Plataforma: DIO (Digital Innovation One)

Ferramentas Adicionais: Agradecimentos especiais às bibliotecas e frameworks de código aberto, como Cytoscape.js e Bootstrap, que facilitaram a construção da interface.