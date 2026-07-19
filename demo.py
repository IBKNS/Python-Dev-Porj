import psycopg2

def connect_to_postgresql():
    """
    Connect to PostgreSQL database
    """
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="",
            port="5432"
        )
        
        cursor = connection.cursor()
        print("Connected to PostgreSQL successfully!")
        
        # Example query
        #cursor.execute("SELECT version();")
        cursor.execute("create table students(student_id serial primary key,name text,address text,age int,number text);")
        connection.commit()
        print(f"Students table created")
        
        cursor.close()
        connection.close()
        print("Connection closed.")
        
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")

## insert data into table
def insert_data():
    """
    Insert data into students table
    """
    # Code to accept data from the user can be added here
    name = input("Enter student name: ")
    address = input("Enter student address: ")
    age = int(input("Enter student age: "))
    number = input("Enter student number: ")

    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="",
            port="5432"
        )
        
        cursor = connection.cursor()
        print("Connected to PostgreSQL successfully!")
        
        # Example insert query
        cursor.execute("INSERT INTO students (name, address, age, number) VALUES (%s, %s, %s, %s)", 
                       (name, address, age, number))
        connection.commit()
        print(f"Data inserted into students table")
        
        cursor.close()
        connection.close()
        print("Connection closed.")
        
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")

## update the existing data in the table
def update_data():
    """
    Update data in students table
    """
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new student name: ")
    address = input("Enter new student address: ")
    age = int(input("Enter new student age: "))
    number = input("Enter new student number: ")

    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="",
            port="5432"
        )
        
        cursor = connection.cursor()
        print("Connected to PostgreSQL successfully!")
        
        # Example update query
        cursor.execute("UPDATE students SET name=%s, address=%s, age=%s, number=%s WHERE student_id=%s", 
                       (name, address, age, number, student_id))
        connection.commit()
        print(f"Data updated in students table")
        
        cursor.close()
        connection.close()
        print("Connection closed.")
        
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
if __name__ == "__main__":
    #connect_to_postgresql()
    #insert_data()
    update_data()