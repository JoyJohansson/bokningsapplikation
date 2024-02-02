CREATE OR REPLACE FUNCTION check_room_availability()
RETURNS TRIGGER AS
$$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM BookingRoom br
        JOIN Booking b ON br.Booking_ID = b.Booking_ID
        WHERE br.Room_ID = NEW.Room_ID
        AND b.Check_out_date > NEW.Check_in_date
        AND b.Check_in_date < NEW.Check_out_date
    ) THEN
        RAISE EXCEPTION 'Room is already booked for the selected dates';
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER prevent_double_booking
BEFORE INSERT ON BookingRoom
FOR EACH ROW
EXECUTE FUNCTION check_room_availability();

DROP FUNCTION check_room_availability;
DROP TRIGGER prevent_double_booking ON BookingRoom;