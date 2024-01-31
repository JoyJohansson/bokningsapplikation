-- Mockdata för RoomType
INSERT INTO RoomType (Roomtype, Capacity) VALUES 
('Double Room', 2);

-- Mockdata för Hotel
INSERT INTO Hotel (Hotel_ID, Name, Country, City, Address, Email, Phone) VALUES
(1, 'Crazy Frog Hotel', 'USA', 'Las Vegas', 'Las Vegas Boulevard 14', 'CrazyFrogHotel@example.com', 123456789);

-- Mockdata för Room
INSERT INTO Room (Room_ID, Hotel_ID, RoomType_ID, PricePerNight) VALUES
(1, 1, 1, 100.00),
(2, 1, 1, 190.00),
(3, 1, 1, 120.00),
(4, 1, 1, 180.00),
(5, 1, 1, 150.00);