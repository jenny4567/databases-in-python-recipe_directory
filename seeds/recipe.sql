DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipe_id;

CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  recipe_name text,
  cooking_time int,
  rating int
);

DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipe_id;

CREATE SEQUENCE IF NOT EXISTS recipe_id;
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  recipe_name text,
  cooking_time int,
  rating int
);

INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Lasagna', 150, 4);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Pizza', 30, 2);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Pudding', 70, 3);

