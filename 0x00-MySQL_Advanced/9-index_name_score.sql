-- Creates an index id_name_score on the table names
-- And the first letter of name and the score
CREATE INDEX idx_name_first_score
ON names (name(1), score);