CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name, s.size FROM dogs d, sizes s WHERE d.height > s.min AND d.height <= s.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d.name FROM dogs d, (SELECT p.child name, d.height height FROM dogs d, parents p WHERE p.parent = d.name) t WHERE d.name = t.name ORDER BY t.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT d1.name first, d2.name second FROM dogs d1, dogs d2, parents p1, parents p2 WHERE d1.name = p1.child AND d2.name = p2.child AND p1.parent = p2.parent AND d1.name < d2.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT sib.first || " and " || sib.second || " are " || sod1.size || " siblings" FROM siblings sib, size_of_dogs sod1, size_of_dogs sod2 WHERE sib.first = sod1.name AND sib.second = sod2.name AND sod1.size = sod2.size ORDER BY sib.first, sib.second;

-- Total size for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE avg_height AS
  SELECT AVG(d.height) height, d.fur, COUNT(*) cnt FROM dogs d GROUP BY d.fur;

CREATE TABLE low_variance AS
  SELECT d.fur, SUM(d.height) height FROM dogs d, avg_height ah WHERE d.fur = ah.fur AND d.height >= ah.height * 0.7 AND d.height <= ah.height * 1.3 GROUP BY d.fur HAVING ah.cnt = COUNT(d.fur);
