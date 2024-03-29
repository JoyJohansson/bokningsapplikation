CREATE TABLE Option (
  Option_ID INT,
  Name VARCHAR(255),
  Description VARCHAR(255),
  Price DECIMAL,
  PRIMARY KEY (Option_ID)
);

CREATE TABLE Guest_Details (
  Guest_ID SERIAL,
  Name VARCHAR(255),
  Phone INT,
  Email VARCHAR(255),
  PRIMARY KEY (Guest_ID)
);

CREATE TABLE Hotel (
  Hotel_ID INT,
  Name VARCHAR(255),
  Country VARCHAR(255),
  City VARCHAR(255),
  Address VARCHAR(255),
  Email VARCHAR(255),
  Phone INT,
  PRIMARY KEY (Hotel_ID)
);

CREATE TABLE RoomType (
  RoomType_ID SERIAL,
  Roomtype VARCHAR(255),
  Capacity INT,
  PRIMARY KEY (RoomType_ID)
);

CREATE TABLE Room (
  Room_ID INT,
  Hotel_ID INT,
  RoomType_ID INT,
  PricePerNight DECIMAL,
  PRIMARY KEY (Room_ID),
  CONSTRAINT FK_Room_Hotel_ID
    FOREIGN KEY (Hotel_ID)
      REFERENCES Hotel(Hotel_ID),
  CONSTRAINT FK_RoomType_RoomType_ID
    FOREIGN KEY (RoomType_ID)
      REFERENCES RoomType(RoomType_ID)
);

CREATE TABLE Booking (
  Booking_ID VARCHAR(250),
  Guest_ID INT,
  Room_ID INT,
  Check_in_date DATE,
  Check_out_date DATE,
  Status BOOLEAN,
  PRIMARY KEY (Booking_ID),
  CONSTRAINT FK_Guest_Details_Guest_ID
    FOREIGN KEY (Guest_ID)
      REFERENCES Guest_Details(Guest_ID),
  CONSTRAINT FK_Room_Room_ID
    FOREIGN KEY (Room_ID)
      REFERENCES Room(Room_ID)
);


CREATE TABLE HotelReview (
  Review_ID SERIAL,
  Hotel_ID INT,
  Guest_name VARCHAR(255),
  Rating INT,
  Comment VARCHAR(255),
  Date_posted DATE,
  PRIMARY KEY (Review_ID),
    CONSTRAINT FK_Hotel_Hotel_ID
    FOREIGN KEY (Hotel_ID)
      REFERENCES Hotel(Hotel_ID)
);

CREATE TABLE BookingOption (
  Booking_ID VARCHAR(250),
  Option_ID INT,
  CONSTRAINT FK_BookingOption_Option_ID
    FOREIGN KEY (Option_ID)
      REFERENCES Option(Option_ID),
  CONSTRAINT FK_BookingOption_Booking_ID
    FOREIGN KEY (Booking_ID)
      REFERENCES Booking(Booking_ID)
);

CREATE TABLE BookingRoom (
  Booking_ID VARCHAR(250),
  Room_ID INT,
  CONSTRAINT FK_BookingRoom_Room_ID
    FOREIGN KEY (Room_ID)
      REFERENCES Room(Room_ID),
  CONSTRAINT FK_BookingRoom_Booking_ID
    FOREIGN KEY (Booking_ID)
      REFERENCES Booking(Booking_ID)
);


CREATE TABLE IF NOT EXISTS admins (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    token VARCHAR(256)
);

CREATE TABLE EditPermission (
  Admin_ID INT,
  Booking_ID VARCHAR(250),
  CONSTRAINT FK_EditPermission_Admin_ID
    FOREIGN KEY (Admin_ID)
      REFERENCES admins(id)
);






CREATE TABLE Files (
    File_ID SERIAL PRIMARY KEY,
    Filename VARCHAR(255) NOT NULL,
    Filetype VARCHAR(100) NOT NULL,
    Filesize INT NOT NULL,
    Upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    File_content BYTEA,
    Room_ID INT REFERENCES Room(Room_ID)
);

