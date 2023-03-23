def_data = {"employees": ["john", "mike", "marry", "chris" , "aaron" , "paul"],
     "salaries":         [ 4000,   1000, 50000, 10000,30000,50000],
     "qualifications":   ["GCSE,BSc", "GCSE", "GCSE, BSc,Msc,PhD", "GCSE,B.E", "MBA", "GCSE,BSc,Msc,PhD"],
     "departments":      ["IT", "HR", 'Academic', "IT", "HR", "reserach"],
     }
class PersonalInfo:
    def __init__(self, name: str, salary: int, qualifications, departaments):
        self.name = name
        self.salary = salary
        self.qualifications = qualifications
        self.departaments = departaments

    def __str__(self) -> str:
        return "\n{\n name: " + self.name + ",\t\n salary: " + str(self.salary) + ",\t\n qualifications: " + str(self.qualifications) + ",\t\n departments: " + str(self.departaments) + "\n}"
        

def getDB():
    database  = dict()
    for i, person in enumerate(def_data["employees"]):
        database[person] = PersonalInfo(
                                 name = def_data["employees"][i], 
                                 salary = def_data["salaries"][i],
                                 qualifications = def_data["qualifications"][i].split(','),
                                 departaments = def_data["departments"][i]
             )
    return database    


def emp(y):
    my_string =''
    for x in y:
        my_string += ' ,'+ x
    return my_string

def indexing(name):
    for i in range(len(def_data["employees"])):
        if name == def_data["employees"][i]:
            return i


