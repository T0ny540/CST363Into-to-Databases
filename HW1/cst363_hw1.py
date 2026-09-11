#Anthony Lopez
#CST363
#This program demonstrates using tables in python and using different functions to manipulate/display data across the table.



from dataclasses import dataclass
from typing import List, Optional, Union

@dataclass(eq=False) 
class Instructor:
    ID: int
    name: str
    dept_name: str
    salary: int

    def __eq__(self, other):
        """
        Stub for equality comparison.
        Should compare only the ID attribute.
        """
        if not isinstance(other,Instructor):
            return NotImplemented
        
        return self.ID == other.ID

class Table:
    """
    Simulates a database table containing rows of Instructor objects.
    Methods to complete:
        insert: Adds a new instructor to the table.
        delete: Removes an instructor by ID.
        lookup: Finds an instructor by ID.
        eval: Filters rows based on an attribute and value.
    """



    def __init__(self):
        self.instructors = []

    def insert(self, instructor: Instructor) -> bool:
        """
        Add an Instructor object to the table.
        If an Instructor with the same ID exists, return False.
        Otherwise, add the Instructor and return True.
        """
        if self.lookup(instructor.ID) is not None:
            return False
        
        self.instructors.append(instructor)
        return True



    def delete(self, ID: int) -> bool:
        """
        Remove the Instructor with the specified ID from the table.
        If no such Instructor exists, return False. Otherwise, return True.
        """
        for instructor in self.instructors:
            if instructor.ID == ID:
                self.instructors.remove(instructor)
                return True
        return False



    def lookup(self, ID: int) -> Optional[Instructor]:
        """
        Find and return the Instructor with the specified ID.
        Return None if no such Instructor exists.
        """
        for instructor in self.instructors:
            if instructor.ID == ID:
                return instructor
        return None



    def eval(self, attr_name: str, attr_value: Union[int, str]) -> List[Instructor]:
        """
        Return a list of Instructors that match the specified attribute and value.
        attr_name can be 'ID', 'name', 'dept_name', or 'salary'.
        """
        return [
            instructor
            for instructor in self.instructors
            if getattr(instructor,attr_name) == attr_value
        ]


    def __str__(self) -> str:
        """
        Return a string representation of the table.
        """
        if not self.instructors:
            return "Empty Table"

        result = ""
        for instructor in self.instructors:
            result += str(instructor) + "\n"
        return result
    

table = Table()
instructor1 = Instructor(101, "John Smith", "English", 74000)
instructor2 = Instructor(102, "Bob Bobby", "Computer Science", 65000)
instructor3 = Instructor(103, "Susan Brown", "Computer Science", 80000)
instructor4 = Instructor(104, "Grace Jones", "Psychology", 78000)
instructor5 = Instructor(105, "Chris Redfield", "Criminal Justice", 72000)

table.insert(instructor1)
table.insert(instructor2)
table.insert(instructor3)
table.insert(instructor4)
table.insert(instructor5)

print ("table after inserting 5 instructors:")
print(table)

print("Deleting ID 104:", table.delete(104))
print("Deleting ID 999:", table.delete(999))

print(table)

print("Lookup ID 102:", table.lookup(102))
print("Lookup ID 999:", table.lookup(999))

print("Multiple rows:")
print(table.eval("dept_name", "Computer Science"))

print("One row:")
print(table.eval("salary", 65000))

print("No rows:")
print(table.eval("dept_name", "Biology"))