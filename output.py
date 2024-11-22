import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rottenpotato03",  # Replace with your MySQL password
    database="menagerie"       # Replace with your database name
)

cursor = mydb.cursor()

# Query to fetch name, birth, and the month of birth
cursor.execute("""
    SELECT name, birth, MONTH(birth) AS birth_month
    FROM pet;
""")

# Print column headers with proper alignment
print(f"{'Name':<12} {'Birth Date':<15} {'MONTH(birth)':<12}")
print("-" * 40)

# Fetch and display the results
for name, birth, birth_month in cursor:
    birth_date = birth.strftime("%Y-%m-%d") if birth else "N/A"  # Format birth as YYYY-MM-DD
    print(f"{name:<12} {birth_date:<15} {birth_month:<12}")

# Close the connection
cursor.close()
mydb.close()
