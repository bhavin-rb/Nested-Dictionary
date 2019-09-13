"""
1. Convert the table below to nested Dictionary
2. Print the content of below table using a loop and the print() function
"""

firstName = [
    "Jack", "Samantha", "Juma", "Samuel", "Catherine"]
lastName = [
    "Nicols", "Johns", "Hamisi", "Adams", "Soka"]
age = [
    35, 28, 30, 58, 35]
gender = [
    "Male", "Female", "Male", "Male", "Female"]
position = [
    "Sales Executive", "Secretary", "Financial Officer", "CEO", "Manager"]
location = [
    "Sanfrancisco, California", "London, UK", "DSM, Tanzania", "Nairobi, Kenya", "Kigali, Rwanda"]

employees = {}
for i in range(1, 6):
    employees["employee" + str(i)] = dict(firstName=firstName[i - 1], lastName=lastName[i - 1], age=age[i - 1],
                                          gender=gender[i - 1], position=position[i - 1], location=location[i - 1])

print(employees)

for i in range(1, 6):
    x = "employee" + str(i)
    print(
        "{0} : {1}, {2}, {3}, {4}, {5}, {6}".format(x, employees[x]["firstName"], employees[x]["lastName"],
                                                    str(employees[x]["age"]), employees[x]["gender"],
                                                    employees[x]["position"], employees[x]["location"])
    )

