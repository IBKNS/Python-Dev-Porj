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
    ## create a dictionary to hold the fields to update and their new values
    filds_to_update = {
        "name": input("Enter new name (leave blank to keep current): "),
        "address": input("Enter new address (leave blank to keep current): "),
        "age": input("Enter new age (leave blank to keep current): "),
        "number": input("Enter new number (leave blank to keep current): ") 
    }
    print(f"Fields to update: {filds_to_update}")
    ## filter out the fields that are empty
    filds_to_update = {k: v for k, v in filds_to_update.items() if v}
    print(f"Fields to update after filtering: {filds_to_update}")
    ## create the update query dynamically based on the fields to update
    set_clause = ", ".join([f"{k}=%s" for k in filds_to_update.keys()])
    values = list(filds_to_update.values())
    values.append(student_id)
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
        cursor.execute(f"UPDATE students SET {set_clause} WHERE student_id=%s", values)
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