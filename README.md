Såhär kör du applikationen
Vi har använt Postgres databas
1. Kör filen Create.tables.SQL
2. Kör filen Inserts.SQL
3. Skapa views i views.SQL
4. Skapa en .env-fil med följande text : 
DB_PASSWORD=ditt_lösenord
DB_NAME=postgres
DB_USER=postgres
DB_HOST=localhost

5. Kör filen add_all_img.py
6. Skriv in kommandot pip install -r requirements.txt i din terminal
7. Skriv flask run i din terminal
Se på fan, nu är vi LIVE!
