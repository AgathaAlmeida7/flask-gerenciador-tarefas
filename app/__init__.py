from flask import Flask

app = Flask(__name__)
#criando a aplicacao flask que vai me permitir ter servidor,rotas,backend

@app.route("/")
def home():
    return "Sistema Gerenciador de Tarefas"


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return "Lista de tarefas"


@app.route("/tarefas/nova")
def nova_tarefa():
    return "Criar nova tarefa"