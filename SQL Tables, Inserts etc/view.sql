CREATE VIEW room_details AS
SELECT room.room_id, roomtype.roomtype, files.filename,files.filetype,files.file_content, roomtype.Capacity, room.pricepernight  
FROM files
JOIN room ON files.room_id = room.room_id
JOIN roomtype ON room.roomtype_id = roomtype.roomtype_id;


CREATE VIEW AvailableRooms AS
SELECT DISTINCT r.Room_ID, rt.roomtype, b.check_in_date, b.check_out_date,f.Filename, f.filetype, f.file_content, rt.capacity, r.pricepernight 
FROM Room r
LEFT JOIN Booking b ON r.Room_ID = b.room_id
LEFT JOIN RoomType rt ON r.RoomType_ID = rt.RoomType_ID
LEFT JOIN Files f ON r.Room_ID = f.Room_ID

SELECT * FROM availablerooms
DROP VIEW availablerooms

CREATE VIEW BookedRooms AS
SELECT DISTINCT r.Room_ID, rt.roomtype, rt.capacity
FROM Room r
INNER JOIN Booking b ON r.Room_ID = b.room_id
LEFT JOIN RoomType rt ON r.RoomType_ID = rt.RoomType_ID