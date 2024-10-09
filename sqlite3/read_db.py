import sqlite3
conn = sqlite3.connect('example.db') #подключили базу данных
cursor = conn.cursor() #для выполнения запросов и извлечения данных
cursor.execute('select * from product')
items = cursor.fetchall()
print(items)
conn.close()