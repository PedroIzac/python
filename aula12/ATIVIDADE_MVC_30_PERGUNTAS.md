# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: _______________________________
- Turma: _______________________________

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

Caminho: models/
Explicação: Ficam nessa pasta porque ela centraliza toda a lógica de dados do projeto. É onde criamos os arquivos Python para mapear o que vai virar tabela no banco de dados.

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

Caminho do Banco: instance/streamflix.db (ou na raiz como streamflix.db)
Caminho da Configuração: app.py
Explicação: O arquivo do banco é gerado automaticamente pelo SQLite com a extensão .db. A configuração que define onde ele vai ser criado fica na linha app.config['SQLALCHEMY_DATABASE_URI'] no arquivo principal do projeto.

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

Caminho e Classes: models/filme_favorito.py -> Classe FilmeFavorito
models/historico_busca.py -> Classe HistoricoBusca
Explicação: O projeto usa só essas duas classes: uma lida com os filmes que o usuário favoritou e salvou, e a outra lida com os termos de texto que a galera pesquisa.

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

Caminho: models/filme_favorito.py e models/historico_busca.py
Explicação: Ambas as classes herdam de db.Model. Por conta dessa herança e do ciclo de vida do SQLAlchemy, elas ganham automaticamente a capacidade de mapeamento objeto-relacional (ORM), além de recursos comuns se implementados em uma classe base, mas nativamente recebem atributos como o mapeamento do campo de chave primária (id), a habilidade de executar queries (query.filter, query.all) e a sessão de persistência de dados.

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

Caminho: models/filme_favorito.py
Explicação: O __tablename__ costuma ser definido como 'favoritos' ou 'filmes_favoritos'. Usamos essa propriedade explicitamente para forçar o banco de dados a usar um nome de tabela padronizado em letras minúsculas e no plural, evitando que o SQLAlchemy crie a tabela com o nome exato da classe em CamelCase (FilmeFavorito), o que viola boas práticas de bancos de dados.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

Caminho: models/filme_favorito.py
Explicação: O campo geralmente é chamado de tmdb_id ou filme_id (do tipo db.Integer). Ele possui a restrição unique=True (para evitar que o mesmo filme seja favoritado em duplicidade) e nullable=False (visto que é obrigatório saber qual filme da API externa está sendo associado).

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

Caminho: models/filme_favorito.py
Explicação: O método recebe os dados do filme, faz uma busca no banco usando cls.query.filter_by(tmdb_id=...).first() para checar se ele já existe. Se o filme já existir, o método simplesmente ignora a inserção ou retorna o objeto existente (evitando erro de duplicidade). Se não existir, ele instancia um novo objeto FilmeFavorito, adiciona à sessão (db.session.add) e commita as alterações no banco (db.session.commit).

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

Caminho: models/historico_busca.py
Classe / Método: Classe HistoricoBusca, método listar_recentes ou similar (geralmente uma @classmethod).
Explicação: Esse método executa uma consulta interna utilizando cls.query.order_by(cls.data_criacao.desc()).limit(8).all(), trazendo de forma decrescente as últimas consultas digitadas pelos usuários.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

Caminho: models/filme_favorito.py
Explicação: O model grava apenas alguns campos espelhados de forma estratégica para não sobrecarregar o banco de dados local. Quatro campos salvos comuns são: tmdb_id, titulo, poster_path (caminho da imagem) e data_lancamento (ou voto_media).

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

Caminho: models/__init__.py
Explicação: Além do objeto db, são exportadas as classes FilmeFavorito e HistoricoBusca. O controller importa diretamente from models import FilmeFavorito porque o arquivo __init__.py unifica o pacote, permitindo uma sintaxe de importação mais limpa e organizada, sem a necessidade de expor a estrutura interna de arquivos físicos da pasta.

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

Caminho: controllers/ (arquivos de inicialização dos controladores)
Explicação: O projeto possui normalmente 3 Blueprints principais:
favoritos_bp → url_prefix='/favoritos'
main_bp (ou home_bp) → url_prefix='/'
filmes_bp → url_prefix='/filmes'

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

Caminho: controllers/filmes_controller.py
Função Python: def populares():
Explicação: Essa função intercepta as requisições destinadas à listagem principal de filmes populares e aciona a camada de serviço correspondente.

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

Caminho: controllers/filmes_controller.py
Explicação: Antes de renderizar o HTML, ela faz uma chamada à camada de serviço/API externa (tmdb_api.get_populares()) para buscar a lista de filmes do servidor do TMDB e, opcionalmente, faz uma consulta ao banco local (HistoricoBusca) ou define variáveis de paginação.

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

Caminho: controllers/filmes_controller.py (ou main_controller.py dependendo de onde fica a rota de busca).
Model e Linha: Usa o model HistoricoBusca. A linha aproximada varia conforme o arquivo, localizando-se logo no início da função de busca (ex: HistoricoBusca.registrar(termo) ou db.session.add(HistoricoBusca(termo=termo))).

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

Caminho: controllers/favoritos_controller.py
Método HTTP: POST (por boa prática de modificação de dados no servidor).
URL de exemplo: http://localhost:5000/favoritos/adicionar/550

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

Caminho: controllers/filmes_controller.py
Explicação: Se a API retornar None, significa que o filme com aquele ID não foi encontrado. O controller faz um desvio condicional (if not filme:) e chama a função abort(404) para exibir a página de erro padrão de recurso não encontrado, ou redireciona o usuário para a home com uma mensagem flash de aviso.

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

Caminho: app.py
Comandos usados:
app.register_blueprint(main_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)
Explicação: O arquivo central da aplicação importa as instâncias dos Blueprints e utiliza a função nativa app.register_blueprint() para acoplar as rotas ao servidor HTTP.

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

Caminho: controllers/main_controller.py (ou home_controller.py).
Variáveis enviadas: Envia uma lista de filmes em destaque/recentes (ex: filmes) e a lista com o histórico das últimas pesquisas armazenadas no banco (buscas_recentes).

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

Caminho: services/tmdb_api.py
Classificação: Não pertence rigidamente a nenhuma das três camadas (MVC), ela é uma classe de Serviço/Helper.
Justificativa: Quem chama essa classe são os Controllers. Ela serve para isolar as requisições HTTP (requests.get) feitas para a API externa do TMDB, limpando o código do controller e impedindo que as regras de rede fiquem misturadas com as regras de rotas.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

Caminho: controllers/filmes_controller.py (ou correspondente da busca).
Origem: request.args
Explicação: O formulário da home faz uma requisição do tipo GET (padrão para buscas), o que significa que o termo digitado é anexado diretamente na URL (ex: /buscar?q=avatar). Usamos request.args.get('q') para capturar dados vindos da URL, enquanto o request.form seria usado se o formulário realizasse um envio oculto via método POST.

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

Caminho: views/templates/
Explicação: Por padrão do Flask adaptado à arquitetura MVC do projeto, esta é a pasta designada para armazenar todos os arquivos .html renderizados pelo Jinja2.

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

Caminho Base: views/templates/layout.html (ou base.html).
Comando Jinja: Os outros arquivos estendem este layout usando o comando {% extends 'layout.html' %} no topo do arquivo e substituem blocos de conteúdo com {% block conteudo %} ... {% endblock %}.

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

Caminho: views/templates/layout.html
Links e url_for:
Home / Início: url_for('main.index')
Filmes Populares: url_for('filmes.populares')
Favoritos: url_for('favoritos.lista')
Histórico: url_for('main.historico')
Sobre: url_for('main.sobre')

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

Caminho: views/templates/filmes/detalhe.html
Origem da Variável: A variável streaming (ou provedores) vem do Controller (filmes_controller.py), que por sua vez a obtém fazendo uma requisição para o endpoint de Watch Providers da API do TMDB na camada Service.

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

Caminho: views/templates/filmes/_card.html
Explicação: É um pedaço de HTML reutilizável (componente/partial). Ele é incluído por arquivos como populares.html ou index.html usando a tag Jinja {% include 'filmes/_card.html' %} dentro de um laço de repetição.

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

Caminho: views/templates/filmes/detalhe.html
Explicação: O controller faz a checagem no banco de dados e envia para o template uma variável booleana chamada eh_favorito (ou favoritado, contendo True ou False). O template usa a condicional {% if eh_favorito %} para decidir se renderiza o botão com a ação de "Remover" ou a ação de "Salvar".

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

Caminho do CSS: views/static/css/style.css (ou pasta static/css/).
Função Flask: O arquivo layout.html injeta o estilo usando a função:
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

Caminho: views/templates/favoritos/lista.html
Loop Jinja: {% for filme in favoritos %}
Campos Exibidos:
filme.titulo (Título do Filme)
filme.data_lancamento (Ano/Data de Lançamento)
filme.tmdb_id (Código de Referência ID)

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

Caminho: views/templates/layout.html
Explicação: Serve para exibir um aviso visual ou travar certas funções caso o sistema esteja rodando em modo de demonstração. Quem disponibiliza essa variável para todos os templates de forma global é um processador de contexto no app.py usando o decorador @app.context_processor.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

Descrição do Fluxo:
View (filmes/detalhe.html): O usuário clica no botão "Salvar Favorito", que submete um formulário POST enviando o ID do filme para a rota correspondente.
Controller (controllers/favoritos_controller.py): A rota intercepta o pedido via método POST, valida se o ID é íntegro e extrai as informações básicas do filme recebidas ou requisitadas na API.
Model (models/filme_favorito.py): O Controller invoca o método FilmeFavorito.adicionar(...). O model abre a transação, insere o registro na tabela de banco de dados SQLite e executa o db.session.commit().
Redirect (Controller → View): Após o commit bem-sucedido, o Controller executa um return redirect(url_for('filmes.detalhe', filme_id=id)) enviando opcionalmente uma mensagem via flash(). A página de detalhe é recarregada na View, exibindo agora o botão alternado para "Remover".

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
