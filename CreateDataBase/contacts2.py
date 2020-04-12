import sqlite3

db = sqlite3.connect("contact.sqlite")

new_email = "another@email.com"
phone = input("Please enter the phone number: ")

# update_sql = "UPDATE contact SET email='{}' WHERE contact.phone={}".format(new_email, phone)
update_sql = "UPDATE contact SET email=? WHERE phone=?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connection hte same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contact"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()