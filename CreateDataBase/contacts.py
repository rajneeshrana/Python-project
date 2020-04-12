import sqlite3

db = sqlite3.connect("contact.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contact (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contact (name, phone, email) VALUES('raj', 123456, 'raj@email.com')")
db.execute("INSERT INTO contact VALUES ('rana', 456789, 'rana@email.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contact")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 30)

cursor.close()
db.commit()
db.close()