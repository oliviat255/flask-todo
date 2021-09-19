CREATE TABLE IF NOT EXISTS todos (
  id INT NOT NULL,
  title varchar(250) NOT NULL,
  complete BOOLEAN NOT NULL, 
  PRIMARY KEY (id)
);