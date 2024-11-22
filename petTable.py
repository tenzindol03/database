import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rottenpotato03"
)

mycursor = mydb.cursor()
mycursor.execute("USE menagerie")

with open(r"C:\Users\Student\Desktop\pet.txt","r") as file:
  for line in file:
    fields = line.strip().split("\t")
    fields = [None if field == r'\N' else field for field in fields]
    query = """
    INSERT INTO pet (name, owner, species, sex, birth, death) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    mycursor.execute(query, fields)

mydb.commit()
print("Data successfully loaded into the pet table.")


