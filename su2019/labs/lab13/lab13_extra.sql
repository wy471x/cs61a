.read lab13.sql

CREATE TABLE su19favpets AS
  SELECT * FROM (SELECT pet, COUNT(*) cnt FROM students GROUP BY pet) t ORDER BY t.cnt DESC LIMIT 10;


CREATE TABLE su19dog AS
  SELECT pet, COUNT(*) FROM students s WHERE s.pet = 'dog';


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, COUNT(*) FROM students WHERE seven = '7' GROUP BY instructor;
