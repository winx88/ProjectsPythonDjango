CREATE TABLE log_users(nameuser varchar(30),data_sign date);

CREATE OR REPLACE FUNCTION logowanie()
        RETURNS trigger AS $$
        BEGIN
        IF (TG_OP = 'INSERT') THEN
		INSERT INTO log_users VALUES (new.username, current_date);
		RETURN NEW;
        END IF;
        END;
        $$ LANGUAGE plpgsql;

CREATE TRIGGER logUsers BEFORE INSERT ON  auth_user FOR EACH ROW EXECUTE PROCEDURE logowanie();
