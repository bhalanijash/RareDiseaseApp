from db import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS diseases (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")
