--  a SQL script that creates a trigger 
-- that resets the attribute valid_email only 
-- when the email has been changed.

CREATE TRIGGER reset_valid_email AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email
        SET NEW.valid_email = 0;
    END IF;
END;