import sqlite3

class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    def save(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO bands (name, hometown) VALUES (?, ?)', (self.name, self.hometown))
        connection.commit()
        connection.close()

    @staticmethod
    def most_performances():
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT bands.name, COUNT(concerts.id) as num_concerts
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        GROUP BY concerts.band_id
        ORDER BY num_concerts DESC
        LIMIT 1
        ''')
        result = cursor.fetchone()
        connection.close()
        return result

class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city

    def save(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO venues (title, city) VALUES (?, ?)', (self.title, self.city))
        connection.commit()
        connection.close()

    @staticmethod
    def most_frequent_band(venue_title):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT bands.name, COUNT(concerts.id) as num_concerts
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = (SELECT id FROM venues WHERE title = ?)
        GROUP BY concerts.band_id
        ORDER BY num_concerts DESC
        LIMIT 1
        ''', (venue_title,))
        result = cursor.fetchone()
        connection.close()
        return result

class Concert:
    def __init__(self, band_id, venue_id, date):
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    def save(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)', (self.band_id, self.venue_id, self.date))
        connection.commit()
        connection.close()
