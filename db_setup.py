import sqlite3

def setup_database():
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY,
        name TEXT,
        hometown TEXT
    )
    ''')

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY,
        title TEXT,
        city TEXT
    )
    ''')

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY,
        band_id INTEGER,
        venue_id INTEGER,
        date TEXT,
        FOREIGN KEY(band_id) REFERENCES bands(id),
        FOREIGN KEY(venue_id) REFERENCES venues(id)
    )
    ''')

    connection.commit()
    connection.close()
    print("Database setup complete!")

if __name__ == "__main__":
    setup_database()
