grades = [[5, 3, 2, 5], [4, 4, 5, 3], [4, 3, 5, 3], [5, 5, 5, 5, 4], [4, 3, 4, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
grades_m = []
for num in grades:
    s = sum(num)/len(num)
    grades_m.append(s)
dict1 = dict(zip(students_sort, grades_m))
print(dict1)