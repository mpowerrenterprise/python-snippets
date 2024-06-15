# Copy
# dict(name)
# Nexted dictionary
# Change value

employee = {"name":"David", "age":45, "job":"Engineer"}
employee.pop("job")

new_dic = employee.copy()
new_dic_2 = dict(new_dic)


print(new_dic)

employee = {

"employee_1":{"name":"David", "age":45, "job":"Engineer"},
"employee_2":{"name":"Frank", "age":32, "job":"Web Developer"},
"employee_3":{"name":"Guna", "age":24, "job":"Engineer"}

}


print(employee["employee_2"]["job"])