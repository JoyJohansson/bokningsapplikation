CREATE VIEW room_details AS
SELECT room.room_id, roomtype.roomtype, files.filename,files.filetype,files.file_content, roomtype.Capacity, room.pricepernight  
FROM files
JOIN room ON files.room_id = room.room_id
JOIN roomtype ON room.roomtype_id = roomtype.roomtype_id;