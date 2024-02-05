import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# Set up a connection pool
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    password=os.getenv("DB_PASSWORD")
)

cur = conn.cursor()

# Loopa igenom alla filer i mappen och lägg till dem i databasen
image_folder = 'static/img'  # Ange sökvägen till mappen med bilderna
room_id = 1  # Börja med rum_id = 1 och öka med 1 för varje bild

for filename in os.listdir(image_folder):
    if filename.endswith('.webp'):
        filepath = os.path.join(image_folder, filename)
        # Öppna filen och läs dess innehåll
        with open(filepath, 'rb') as file:
            file_content = file.read()

        # Bestäm filtyp baserat på filändelsen
        filetype = 'image/webp'

        # Bestäm filstorlek
        filesize = os.path.getsize(filepath)

        # SQL-kommando för att infoga filen i tabellen Files
        sql = """INSERT INTO Files (Filename, Filetype, Filesize, File_content, room_id)
                 VALUES (%s, %s, %s, %s, %s)"""

        # Utför INSERT-operationen
        cur.execute(sql, (filename, filetype, filesize, file_content, room_id))

        # Öka rum_id med 1 för nästa bild
        room_id += 1

# Utför en commit för att spara ändringarna i databasen
conn.commit()

# Stäng cursor och anslutning
cur.close()
conn.close()
