from crud.singleton import Logging

import sqlite3

log_obj = Logging()
log_obj.set_log_level("DATABASE", 'DEBUG')
logger = log_obj.get_logger('DATABASE')

class Database():
    def __init__(self):
        self.conn = sqlite3.connect('data.db', check_same_thread=False)

    # def create_conn(self):
    #     self.conn = sqlite3.connect('data.db')
        
    def create_table():
        try:
            c = self.conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)""")
            conn.commit()
            return {'message': 'Table created successfully'}

        except Exception as e:
            logger.error(e)
            return {'error': f'Error creating table: {e}'}

    def get_items(self):
        try:
            c = self.conn.cursor()
            items = c.execute("""SELECT * FROM products""").fetchall()
            return items

        except Exception as e:
            logger.error(e)
            return {'error': f'Error retrieving products: {e}'}

    def add_item(self, name, description):
        try:
            c = self.conn.cursor()
            item = c.execute("""INSERT INTO products (name, description) values (?, ?)""", (name, description,)).fetchone()
            self.conn.commit()
            return item

        except Exception as e:
            logger.error(e)
            return {'error': f'Error retrieving item: {e}'}

    def update_item(self, name, description, id):
        try:
            c = self.conn.cursor()
            c.execute("""UPDATE products SET name=?, description=? WHERE id=?""", (name, description, id,))
            self.conn.commit()
            return {'message': 'Item add successfully'}

        except Exception as e:
            logger.error(e)
            return {'error': f'Error adding item: {e}'}

    def delete_item(self, id):
        c = self.conn.cursor()
        c.execute("""DELETE FROM products WHERE id=?""", (id,))
        self.conn.commit()
        return {'message': 'Item deleted successfully'}

    def close_connection(self):
        self.conn.close()
        return {'message': 'Connection closed successfully'}
