import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# Set up a connection pool
conn= psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    password=os.getenv("DB_PASSWORD"),
    
)

# Skapa en cursor för att utföra SQL-operationer
cur = conn.cursor()

# Öppna filen och läs dess innehåll
with open('static/nedladdning.jpeg', 'rb') as file:
    file_content = file.read()

# SQL-kommando för att infoga filen i tabellen Files
sql = """INSERT INTO Files (Filename, Filetype, Filesize, File_content, room_id)
         VALUES (%s, %s, %s, %s, %s)"""

# Definiera värden för SQL-kommandot
filename = 'edf36bef-b50f-4e98-9de8-8e3c4add39aa.webp'
filetype = 'image/webp'
filesize = len(file_content)
room_id = 4

# Utför INSERT-operationen
cur.execute(sql, (filename, filetype, filesize, file_content, room_id))

# Utför en commit för att spara ändringarna i databasen
conn.commit()

# Stäng cursor och anslutning
cur.close()
conn.close()