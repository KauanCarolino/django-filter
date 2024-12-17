# Lista de Produtos com Filtro e Pesquisa

Este projeto é um site simples desenvolvido com Django, que lista produtos e permite a pesquisa com base em critérios definidos. Ele utiliza as bibliotecas **django-filters** e **django-widget-tweaks** para implementar e personalizar os filtros de pesquisa.

## Funcionalidades

- **Listagem de Produtos**: Exibe uma lista de produtos cadastrados.
- **Pesquisa Personalizada**: Inclui inputs de pesquisa dinâmica para facilitar a filtragem.
- **Filtros Avançados**: Implementados com **django-filters**, permitindo consultas específicas e refinadas.
- **Customização de Inputs**: Utiliza **django-widget-tweaks** para personalizar os campos do formulário de pesquisa.

## Tecnologias Utilizadas

- **Python 3.10.0**
- **Django 5.1.4**
- **django-filters 24.3**
- **django-widget-tweaks 1.5.0**
- **HTML5**
- **CSS3**

## Como Executar o Projeto

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
   ```bash
   Dentro da pasta 'sql_data/' existe os dados sql. Execute primeiro Category depois Products 
   ```

6. **Inicie o servidor local**:  
   ```bash
   python manage.py runserver
   ```

7. **Acesse o site**:  
   Abra seu navegador e visite [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Estrutura do Projeto

```
django-filter/
├── manage.py
├── base_static/
│   ├── style.css
├── product/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── product/
│   ├── admin.py
│   ├── apps.py
│   ├── filters.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
└── templates/
│       └── pesquisa.html
├── requirements.txt
└── README.md
```

## Como Contribuir

1. **Fork este repositório**.  
2. **Crie uma branch para sua feature**:  
   ```bash
   git checkout -b minha-feature
   ```
3. **Implemente sua feature e realize o commit**:  
   ```bash
   git commit -m "Minha nova feature"
   ```
4. **Envie suas alterações para o repositório remoto**:  
   ```bash
   git push origin minha-feature
   ```
5. **Abra um Pull Request**.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido por** [KauanCarolino](https://github.com/KauanCarolino)
