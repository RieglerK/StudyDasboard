import sqlite3

conn = sqlite3.connect("study-dashboard-test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS studiengang (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    abschluss TEXT NOT NULL,
    gesamt_ects INTEGER NOT NULL
);
""")

cursor.execute("INSERT INTO studiengang (name, abschluss, gesamt_ects) VALUES (?, ?, ?)",
               ("Informatik", "B.Sc.", 180))

conn.commit()

cursor.execute("SELECT id, name, abschluss, gesamt_ects FROM studiengang")
rows = cursor.fetchall()

print("Studiengänge in der Datenbank:")
for row in rows:
    print(row)

conn.close()
