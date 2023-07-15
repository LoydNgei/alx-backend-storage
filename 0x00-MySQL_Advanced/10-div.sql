-- Create a function SafeDiv that divides (and returns) the first by second number
-- Or returns 0 if the second number is equal to 0

DROP FUNCTION IF EXISTS SafeDiv;
DELIMETER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    IF (b = 0)
    THEN
        RETURN (0);
    ELSE
        RETURN (a / b);
    END IF;
END
$$
DELIMITER ;