from db import Database
from models.user import Company, User, Product





def main():
    """
    Main function that demonstrates the usage of the Database class.
    The function performs the following steps:
        1. Creates a connection to the SQLite database file "sqlite.db".
        2. Creates necessary tables in the database.
        3. Creates a list of User objects.
        4. Inserts each User object into the database.
        5. Retrieves a user with the ID of 1 from the database.
        6. Prints the retrieved user.
        7. If a user is found, updates the user's name to "John Smith" and deletes the user.
        8. Drops the tables from the database.
    """
    with Database("sqlite.db") as db:
        #db.create_tables()

        users = [
            User(name="John Doe"),
            User(name="Jane Doe"),
            User(name="Jack Doe"),
            User(name="Jill Doe"),
        ]

        for user in users:
            db.create_user(user)

        user = db.get_user(1)

        print(user)

        if user:
            db.update_user(user_id=user.id, name="John Smith")
            db.delete_user(user_id=user.id)


        companies = [
            Company(name="AAAAA"),
            User(name="BBB"),
            User(name="CCCC"),
            User(name="DDDD"),
        ]

        for user in companies:
            db.create_company(user)


#witd Database.create_company

# # Assuming you have models defined like User and Product
# new_user = User(name="John Doe", email="john@example.com")
# new_product = Product(name="Laptop", price=1000.00)

# # Create a user record
# self.create_record(User, new_user)

# # Create a product record
# self.create_record(Product, new_product)




#        db.drop_tables()



if __name__ == "__main__":
    main()
