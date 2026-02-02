DROP TABLE IF EXISTS updates;
DROP TABLE IF EXISTS risks;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    head TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT NOT NULL,
    department_id INTEGER,
    created_at TEXT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (id) ON DELETE SET NULL
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    owner TEXT NOT NULL,
    status TEXT NOT NULL,
    department_id INTEGER,
    budget REAL NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (id) ON DELETE SET NULL
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    assignee_id INTEGER,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    due_date TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE,
    FOREIGN KEY (assignee_id) REFERENCES employees (id) ON DELETE SET NULL
);

CREATE TABLE risks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    impact TEXT NOT NULL,
    likelihood TEXT NOT NULL,
    mitigation TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
);

CREATE TABLE updates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    summary TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
);

CREATE INDEX idx_projects_department ON projects (department_id);
CREATE INDEX idx_tasks_project ON tasks (project_id);
CREATE INDEX idx_tasks_assignee ON tasks (assignee_id);
CREATE INDEX idx_risks_project ON risks (project_id);
CREATE INDEX idx_updates_project ON updates (project_id);
