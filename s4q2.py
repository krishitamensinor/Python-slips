student={
  "name" : "krishita",
  "roll_no" : 14,
  "marks" : 67
}

print("Original dictionary : ",student)

print("Name : ",student["name"])
student["grade"]="A"

print("After adding grade : ",student)
student["marks"]=90

print("After Updating Marks : ",student)
student.pop("roll_no")

print("After Removing Roll No : ",student)

print("Keys : ",student.keys())

print("Value : ",student.values())

if "name" in student:
  print("Name key exists")