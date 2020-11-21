employee_file = open("/Users/adithyaswaminathan/Desktop/Coding/Python/Personal/EmployeeDemo/Employee.txt", "r") 
                                          #r stands for read mode,
                                          #w stands for write (to change data), 
                                          #a stands for append (to add data), 
                                          #r+ is for reading and writing
                                          #x to create a file
"""
print(employee_file.readline()) #reads individual lines
print(employee_file.read()) #reads rest of file
"""
for employee in employee_file.readlines(): #array of lines in text file
    print(employee)
employee_file.close()