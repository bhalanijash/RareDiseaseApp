from db import get_connection

def get_all_diseases():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM diseases")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_disease_by_id(disease_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM diseases WHERE id = %s", (disease_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def add_disease(name, description):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO diseases (name, description) VALUES (%s, %s)", (name, description))
    connection.commit()
    cursor.close()
    connection.close()

def update_disease(disease_id, name, description):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE diseases SET name = %s, description = %s WHERE id = %s", (name, description, disease_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_disease(disease_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM diseases WHERE id = %s", (disease_id))
    connection.commit()
    cursor.close()
    connection.close()
