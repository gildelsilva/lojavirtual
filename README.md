# Loja Virtual

Uma aplicação web de e-commerce desenvolvida com Django, permitindo a gestão de produtos, categorias e carrinho de compras.

## Funcionalidades

- **Catálogo de Produtos**: Listagem de produtos por categoria
- **Detalhes do Produto**: Visualização detalhada de produtos com imagens
- **Carrinho de Compras**: Adição e gestão de itens no carrinho
- **Formulário de Contato**: Página "Fale Conosco" para contato com a loja
- **Administração**: Interface administrativa do Django para gestão de dados

## Tecnologias Utilizadas

- **Backend**: Django 6.0
- **Banco de Dados**: PostgreSQL (produção) / SQLite (desenvolvimento)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Outros**: Pillow (para imagens), psycopg2-binary (conector PostgreSQL)

## Pré-requisitos

- Python 3.13+
- PostgreSQL (para produção) ou SQLite (para desenvolvimento)
- Virtualenv (recomendado)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd lojavirtual
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install django pillow psycopg2-binary python-dotenv
   ```

4. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis (para PostgreSQL):
   ```
   POSTGRES_DB=lojavirtual
   POSTGRES_USER=seu_usuario
   POSTGRES_PASSWORD=sua_senha
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   ```

5. **Execute as migrações**:
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário** (opcional, para acessar o admin):
   ```bash
   python manage.py createsuperuser
   ```

7. **Execute o servidor**:
   ```bash
   python manage.py runserver
   ```

Acesse a aplicação em `http://localhost:8000`.

## Estrutura do Projeto

- `lojavirtual/`: Configurações principais do Django
- `main/`: App principal com modelos de Produto, Categoria, Cliente, etc.
- `carrinho/`: App para gestão do carrinho de compras
- `templates/`: Templates HTML
- `static/`: Arquivos estáticos (CSS, JS, imagens)
- `imagens-produtos/`: Diretório para upload de imagens de produtos

## Uso com Docker

Para executar com Docker Compose (PostgreSQL):

1. Certifique-se de ter o Docker e Docker Compose instalados.

2. Configure o arquivo `.env` com as variáveis do banco.

3. Execute:
   ```bash
   docker-compose up -d
   ```

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Para dúvidas ou sugestões, use o formulário "Fale Conosco" na aplicação ou envie um e-mail para gildelsilva@gmail.com.