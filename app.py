from flask import Flask, render_template, request, redirect, url_for
from disease import get_all_diseases, get_disease_by_id, add_disease, update_disease, delete_disease
from tables import create_tables

app = Flask(__name__)

create_tables()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/diseases', methods=['GET'])
def get_diseases():
    diseases = get_all_diseases()
    return render_template('index.html', diseases=diseases)

@app.route('/diseases/<int:disease_id>', methods=['GET'])
def get_disease(disease_id):
    disease = get_disease_by_id(disease_id)
    if disease:
        return render_template('disease.html', disease=disease)
    return "Disease not found", 404

@app.route('/diseases/add', methods=['GET'])
def add_disease_form():
    return render_template('add_disease.html')

@app.route('/diseases', methods=['POST'])
def create_disease():
    name = request.form.get('name')
    description = request.form.get('description')

    if not name or not description:
        return "Missing name or description", 400

    add_disease(name, description)
    return redirect(url_for('get_diseases'))

@app.route('/diseases/<int:disease_id>/edit', methods=['GET'])
def modify_disease_form(disease_id):
    disease = get_disease_by_id(disease_id)
    if disease:
        return render_template('update_disease.html', disease=disease)
    return "Disease not found", 404

@app.route('/diseases/<int:disease_id>', methods=['POST'])
def modify_disease(disease_id):
    name = request.form.get('name')
    description = request.form.get('description')

    if not name or not description:
        return "Missing name or description", 400

    update_disease(disease_id, name, description)
    return redirect(url_for('get_diseases'))

@app.route('/diseases/<int:disease_id>/delete', methods=['GET'])
def delete_disease_form(disease_id):
    disease = get_disease_by_id(disease_id)
    if disease:
        return render_template('delete_disease.html', disease=disease)
    return "Disease not found", 404

@app.route('/diseases/<int:disease_id>/delete', methods=['POST'])
def remove_disease(disease_id):
    delete_disease(disease_id)
    return redirect(url_for('get_diseases'))

if __name__ == '__main__':
    app.run(debug=True)