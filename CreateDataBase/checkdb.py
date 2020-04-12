import sqlite3

conn = sqlite3.connect("contact.sqlite")
name = input("Please enter a name search for ")

# for row in conn.execute("SELECT * FROM contact WHERE name=?", (name,)):
for row in conn.execute("SELECT * FROM contact WHERE name LIKE ?", (name,)):
    print(row)


conn.close()