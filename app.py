from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, template_folder="templates")

funcionarios = []

@app.route('/')
def home():
    return render_template('index.html', funcionarios=funcionarios)

@app.route("/editar-funcionario/<int:id>", methods=["POST", "GET"])
def editar_funcionario(id):
    funcionario_index = next((index for index, funcionario in enumerate(funcionarios) if funcionario['id'] == id), None)
    if funcionario_index is None:
        return "Funcionário não encontrado"

    if request.method == "GET":
        return render_template('editar_funcionarios.html', funcionario=funcionarios[funcionario_index], id=id)
    elif request.method == "POST":
        funcionarios[funcionario_index]['nome'] = request.form['nome']
        funcionarios[funcionario_index]['cidade'] = request.form['cidade']
        funcionarios[funcionario_index]['estado'] = request.form['estado']
        funcionarios[funcionario_index]['cargo'] = request.form['cargo']
        return redirect(url_for('ver_funcionarios'))

@app.route('/excluir-funcionario/<int:id>', methods=['POST'])
def excluir_funcionario(id):
    if request.method == 'POST':
        if 0 <= id < len(funcionarios):
            funcionarios.pop(id)
    return redirect(url_for('ver_funcionarios'))


@app.route('/ver_funcionarios')
def ver_funcionarios():
    return render_template('ver_funcionarios.html', funcionarios=funcionarios)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        nome = request.form['nome']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cargo = request.form['cargo']
        funcionario = {'id': len(funcionarios), 'nome': nome, 'cidade': cidade, 'estado': estado, 'cargo': cargo}
        funcionarios.append(funcionario)
        return redirect(url_for('ver_funcionarios'))
    return render_template('cadastrar_funcionarios.html')

if __name__ == '__main__':
    app.run(debug=True)
