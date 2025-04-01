from box import ConfigBox

student: dict[str, object] = {
    'name': 'John Doe',
    'age': 21,
    'grade': 85
}
print(type(student))            # <class 'dict'>

print(student['name'])          # John Doe
print(student.get('name'))      # John Doe

# to call a key using dot notation
student = ConfigBox(student)
print(student.name)
