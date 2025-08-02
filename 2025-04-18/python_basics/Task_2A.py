name="Arun"
age=22
marks=[92.5,90.0,88.5]
details={"name":"Arun","age":22,"marks":[92.5,90.0,88.5]}

print("name:",type(name))
print("age:",type(age))
print("marks:",type(marks))
print("details:",type(details))

total_mark=sum(details["marks"])
average_mark=total_mark/len(details["marks"])
print("Total_mark:",total_mark)
print("Average_mark:",average_mark)

if average_mark>=40:
    is_passed=True
else:
    is_passed=False

for mark in marks:
    print(mark)

marks_set=set(marks)
print(marks_set)

subject_names=("Mathematics","English","Physics")
print("Subjects:",subject_names)

remarks=None
print("Remarks:",remarks)

print("is_passed type:",type(is_passed))

print("\n")
print("=======SudentReport============")

print("Name:",name)
print("Age:",age)
print("Marks:",marks)
print("Subjects:",subject_names)
print("TotalMark:",total_mark)
print("AverageMark:",average_mark)
print("Result:","Passed" if is_passed else "Failed")

print("================================")
