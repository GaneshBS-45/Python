class Student:
    def __init__(self,rollno:int,name:str,age:int,gender:str,marks=[])->None:
        self.rollno=rollno
        self.name=name
        self.gender=gender
        self.age=age
        self.marks=marks
    
    def updateName(self,newName):
        self.name=newName
    
    def total(self)->int:
        # return self.sum(self.marks)
        t=0
        for num in self.marks:
            t+=num
        return t
    def display(self)->None:
        print(f"self.name = {self.name}")
        print(f"self.rollno = {self.rollno}")
        print(f"self.age = {self.age}")
        print(f"self.gender = {self.gender}")
        print(f"self.marks = {self.marks}")

# s1=Student(12,"ganesh",25,"Male",[98,97,95,84,90,84])
# s2=Student(13,"Gagan",26,"Male",[84,77,78])
# so we have passed 2 objects into the list 
# students_data=[s1,s2]
# also we can pass the data directly to the list like the below example
students_data=[
    Student(12,"ganesh",25,"Male",[98,97,95,84,90,84]),
    Student(13,"Gagan",26,"Male",[84,77,78])]
students_data[0].display()
print(students_data[0].age)
print(students_data[1].marks)
print(students_data[0].name)
print(students_data[0].total())

Student_details=[]
while True:
    print("1) Add a Student")
    print("2) Remove  a Student")
    print("3) Display a Student details")
    print("4) Update a Student details")
    print("5) Exit")
    Choice=int(input("Please enter your choice ="))
    if Choice==1:
        rollno=int(input("Enter your roll no ="))
        name=input("Enter your name=")
        age=input("ENter your age =")
        gender=input("Enter your gender =")
        subject_num=int(input("Enter the number of subjects ="))
        marks=[]
        for i in range(subject_num):
            m=int(input())
            marks.append(m)
        x=Student(rollno,name,age,gender,marks)
        Student_details.append(x)
        print(Student_details)
    elif Choice==2:
        pass
    elif Choice==3:
        if len(Student_details)==0:
            print("No data in the list add the data")
        else:
            for num in Student_details:
                num.display()
    elif Choice==4:
        rolno=int(input("Enter the student rool no you want to update"))
        for num in students_data:
            if num.rollno==rolno:
                num.display()
    elif Choice==5:
        break
    else:
        print("Invalid Choice")

