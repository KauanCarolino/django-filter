# 🛍️ Lista de Produtos com Filtro e Pesquisa

Este é um projeto simples e funcional desenvolvido com **Django**, focado em listar produtos e permitir pesquisas personalizadas. Utilizamos **django-filters** para criar filtros avançados e **django-widget-tweaks** para personalizar os formulários, garantindo uma experiência de uso otimizada.

---

## 🚀 Funcionalidades

✅ **Listagem de Produtos**:  
Exibe uma lista clara e objetiva dos produtos cadastrados.  

✅ **Pesquisa Personalizada**:  
Permite que os usuários filtrem produtos rapidamente por meio de inputs dinâmicos.  

✅ **Filtros Avançados**:  
Criados com **django-filters**, permitindo buscas detalhadas e refinadas.  

✅ **Customização de Inputs**:  
Campos de formulário estilizados com **django-widget-tweaks** para melhor visualização e usabilidade.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10.0**
- **Django 5.1.4**
- **django-filters 24.3**
- **django-widget-tweaks 1.5.0**
- **HTML5**
- **CSS3**

---

## ⚙️ Como Executar o Projeto

1. **Clone este repositório**:  
   ```bash
   git clone https://github.com/KauanCarolino/django-filter.git
   cd django-filter
   ```

2. **Crie e ative um ambiente virtual**:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**:  
   Atualize o arquivo `settings.py` com as informações do banco de dados e execute:  
   ```bash
   python manage.py migrate
   ```

5. **Adicione dados iniciais (opcional)**:  
   Dentro da pasta `sql_data/` existem arquivos SQL contendo dados iniciais.  
   Execute os scripts nesta ordem:  
   - **Category**  
   - **Products**

6. **Inicie o servidor local**:  
   ```bash
   python manage.py runserver
   ```

7. **Acesse o site**:  
   Abra seu navegador e visite [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📂 Estrutura do Projeto

```
django-filter/
├── manage.py                    # Ponto de entrada do Django
├── base_static/                 # Arquivos estáticos gerais
│   ├── style.css                # Estilo customizado
├── product/                     # Diretório principal do app
│   ├── __init__.py              # Arquivo de inicialização do módulo
│   ├── asgi.py                  # Configuração para servidores ASGI
│   ├── settings.py              # Configuração geral do Django
│   ├── urls.py                  # Rotas do projeto
│   ├── wsgi.py                  # Configuração para servidores WSGI
│   ├── admin.py                 # Configuração do admin
│   ├── apps.py                  # Configuração do aplicativo
│   ├── filters.py               # Configurações do django-filters
│   ├── forms.py                 # Formulários customizados
│   ├── models.py                # Definição dos modelos de dados
│   ├── urls.py                  # Rotas específicas do app
│   ├── views.py                 # Lógica das views
├── templates/                   # Diretório de templates HTML
│   └── pesquisa.html            # Template da página de pesquisa
├── requirements.txt             # Dependências do projeto
└── README.md                    # Documentação do projeto
```

---

## 🤝 Como Contribuir

Quer contribuir para o projeto? Siga os passos abaixo:

1. Faça um **fork** deste repositório.  
2. Crie uma nova branch para sua feature:  
   ```bash
   git checkout -b minha-feature
   ```
3. Implemente sua feature e realize o commit:  
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie suas alterações para o repositório remoto:  
   ```bash
   git push origin minha-feature
   ```
5. Abra um **Pull Request** e descreva as alterações.

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido por** [KauanCarolino](https://github.com/KauanCarolino) 🚀
