CREATE VIEW K2 AS
SELECT Roomtype, Capacity, PricePerNight FROM roomtype, room;

SELECT * FROM K2 ORDER BY pricepernight;