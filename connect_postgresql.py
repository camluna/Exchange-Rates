import psycopg2
from configparser import ConfigParser

def read_config(filename='config.ini', section='database'):
    # Lee la configuración desde el archivo config.ini
    parser = ConfigParser()
    parser.read(filename)

    # Extrae la sección 'database' del archivo config.ini
    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db_config

def test_connection():
    try:
        config = read_config()
        conn = psycopg2.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )
        cursor = conn.cursor()
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(f"Connected to PostgreSQL database, version: {db_version}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to PostgreSQL database: {e}")

if __name__ == '__main__':
    test_connection()
