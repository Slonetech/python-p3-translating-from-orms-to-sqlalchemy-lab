from models import Dog
from sqlalchemy.orm import declarative_base

base = declarative_base()

    

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog) # Add the dog object to the session
    session.commit() # Commit the changes to the database

def get_all(session):
    # Return a list of all the dog objects in the database
    return session.query(Dog).all()


def find_by_name(session, name):
    # Return the first dog object whose name matches the name parameter
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    # Return the first dog object whose id matches the id parameter
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    # Return the first dog object whose name and breed match the name and breed parameters
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    # Update the breed attribute of the dog object to the breed parameter
    dog.breed = breed
    session.commit()