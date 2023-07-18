from cs50 import SQL

db = SQL("sqlite:///database2.db")
db.execute("CREATE TABLE IF NOT EXISTS Employees(id NUMBER, name TEXT, age NUMBER, fav_food STRING)")
db.execute("INSERT INTO Users(name, age, fav_food) VALUES(?, ?, ?)", "Kingsley", 33, "Fried Rice and plantain")
people = db.execute("SELECT * FROM Users")

print(people)