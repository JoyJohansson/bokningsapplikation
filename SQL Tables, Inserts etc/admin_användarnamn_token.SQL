CREATE TABLE hotel.admins (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    token VARCHAR(256)
);


"Se till att hasha lösenorden innan du lagrar dem i databasen. Du kan använda ett bibliotek som bcrypt för detta."


CREATE SCHEMA hotel;