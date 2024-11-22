import mysql.connector

def fetch_female_dogs():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rottenpotato03",
            database="menagerie"
        )
        cursor = mydb.cursor()
        query = "SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';"
        cursor.execute(query)
        rows = cursor.fetchall()

        print("Records of female dogs in the 'pet' table:")
        print("{:<10} {:<10} {:<10} {:<5} {:<12} {:<12}".format(
            "Name", "Owner", "Species", "Sex", "Birth", "Death"
        ))
        print("-" * 60)
        for row in rows:
            print("{:<10} {:<10} {:<10} {:<5} {:<12} {:<12}".format(
                row[0], row[1], row[2], row[3], str(row[4]), str(row[5]) if row[5] else "NULL"
            ))

    except mysql.connector.Error as e:
        print(f"Database error: {e}")

    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    fetch_female_dogs()
