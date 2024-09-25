from sqlalchemy import create_engine, String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mariadb+mariadbconnector://root:abc123@localhost:3306/hw1')

base = declarative_base()
class Student(base):
    __tablename__ = "student"
    ID = Column(String, primary_key=True)
    Name = Column(String)
    Dept_Name = Column(String)
    Tot_Cred = Column(Integer)

factory = sessionmaker(bind=engine)
session = factory()

def queryStudents(str):
    print(str)
    for instance in session.query(Student):
        print(f"ID: {instance.ID}, Name: {instance.Name}, Dept_Name: {instance.Dept_Name}, Tot_Cred: {instance.Tot_Cred}")
    print("\n\n")

queryStudents("initial query: ")

new_student = Student(ID="S011", Name="ns_name", Dept_Name="Computer Science", Tot_Cred=0)
session.add(new_student)
session.commit()

queryStudents("after insert: ")

updated_student = session.query(Student).filter_by(ID="S011").first()
updated_student.ID = "S012"
session.commit()

queryStudents("after update: ")

deleted_student = session.query(Student).filter_by(ID="S012").first()
session.delete(deleted_student)
session.commit()

queryStudents("after delete: ")
