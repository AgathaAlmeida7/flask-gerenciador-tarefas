from flask import Flask, render_template
#funcao template,responsavel por renderizar templates

app = Flask(__name__)
#criando a aplicacao flask que vai me permitir ter servidor,rotas,backend

@app.route("/")
def home():
    return render_template("index.html",titulo="Página Inicial")
#fazendo uma mudancao de cada vez, começando pela pagina inicial
#o titulo agora nao esta mais gravado no html,ele veio propriamentedo backend
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return render_template("tarefas.html",titulo="Lista de Tarefas")


@app.route("/tarefas/nova")
def nova_tarefa():
    return render_template("nova_tarefa.html",titulo="Nova Tarefa")

#o que deve ser percebido:
#todas as paginas possuem o  mesmo cabeçalho
#todas usam a mesma estrutura
#apenas o conteudo central muda
#o titulo da aba do navegador muda conforme a rota
#objetivo:evitar duplicidade e centralizar aquilo que é comum
