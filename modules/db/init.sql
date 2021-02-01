CREATE TABLE IF NOT EXISTS tasks (
   	id integer PRIMARY KEY,
    name text NOT NULL,
    task_text text NOT NULL,
  	from_date datetime NOT NULL,
	to_date datetime NOT NULL,
	active BOOLEAN
);

CREATE TABLE IF NOT EXISTS groups (
	id integer PRIMARY KEY,
	group_name text NOT NULL
);

CREATE TABLE IF NOT EXISTS group_to_task (
	id integer PRIMARY KEY,
	group_id integer,
	task_id integer
);