import logging
from sqlalchemy import Column, create_engine
from sqlalchemy.orm import sessionmaker


from models.user import Company, User, Product


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Database:
    """
    SQLAlchemy database class to manage SQLite database connection and operations with Alembic.
    """

    def __init__(self, db_path: str) -> None:
        """
        Initialize the database connection.
        """
        assert db_path
        self.db_path = db_path
        self.engine = create_engine(f"sqlite:///{self.db_path}")
        self.current_session = None
        logger.info(f"Initiate database connection : {self.db_path}")
    
    
# """    def __init__(self, db_path: str): 
#         """
#         Initialize the database connection.
#         """
#         self.db_path = db_path
#         self.engine = create_engine(f"sqlite:///{self.db_path}")
#         self.Session = sessionmaker(bind=self.engine)

#         logger.info(f"Database connection established at {self.db_path}")

# """
        

    def __enter__(self):
        """
        Enter the context manager.
        """
        self.current_session = sessionmaker(self.engine)
        logger.info(f"Database connection established at {self.db_path}")
        return self


    
    def get_by_field(self,model: callable, field: str, key, all: bool):
            result = self.current_session.query(model).filter(getattr(model,field)==key)
            return result.all() if all else result.first()
            
    def create(self, model: callable, ):
        assert self.current_session
        self.current_session.add(model(**kwargs))
        self.current_session.commit()
        # create(company, {name: cenas})

    def update(self, model: callable, key: int, **kwargs):
        assert self.current_session
        obj = self. get_by_field(model=model, field='id', key = key, all = false)
        assert obj
        for field, value in kwargs:
            if not hasattr(obj, field):
                raise Exception('Field is not valid')
            setattr(obj,field,value)
        self.current_session.commit()
        
    def delete(self, model:callable, key: int):
        assert self.current_session
        obj = self. get_by_field(model=model, field='id', key = key, all = false)
        obj.delete()
        self.current_session.commit()
        


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context manager.
        """
        self.engine.dispose()

    
    def create_tables(self):
        """
        Create all tables in the database.
        """
        Base.metadata.create_all(self.engine)
        logger.info("All tables created in the database")

    def drop_tables(self):
        """
        Drop all tables from the database.
        """
        Base.metadata.drop_all(self.engine)
        logger.info("All tables dropped from the database")



    def create_user(self, user: User):
        """
        Create a user in the database.
        """
        with self.Session() as session:
            session.add(user)
            session.commit()
            logger.info(f"User {user} created in the database")

    def create_company(self, company: Company):
        """
        Create a company in the database.
        """
        with self.Session() as session:
            session.add(company)
            session.commit()
            logger.info(f"Company {company} created in the database")

    def get_user(self, user_id: int) -> User | None:
        """
        Get a user from the database by its ID.
        """
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            logger.info(f"User {user} retrieved from the database")
            return user


    def delete_user(self, user_id: int):
        """
        Delete a user from the database.
        """
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            session.delete(user)
            session.commit()
            logger.info(f"User {user} deleted from the database")

    def update_user(self, user_id: int, **kwargs):
        """
        Update a user in the database.
        """
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()

            for key, value in kwargs.items():
                if not hasattr(user, key):
                    raise AttributeError(f"User does not have attribute {key}")

                setattr(user, key, value)
            session.commit()
            logger.info(f"User {user} updated in the database")

        return self.get_user(user_id)

    # # def generica para criar registos em qualquer tabela    
    # def create_record(self, table: object, record: object):
    #     """
    #     Create a record in the specified table (model) in the database.
        
    #     Args:
    #         table: The table/model class where the record should be added.
    #         record: An instance of the table/model that needs to be added.
    #     """
    #     with self.Session() as session:
    #         session.add(record)
    #         session.commit()
    #         logger.info(f"Record {record} created in the {table.__name__} table")

