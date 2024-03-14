''' If the marks obtained by a student in five different subjects are input through the keyboard,
find out the aggregate marks and percentage marks obtained by the student. Assume that the
maximum marks that can be obtained by a student in each subject is 100.'''

a = int(input("Enter any no "))
b = int(input("Enter any no "))
c = int(input("Enter any no "))
d = int(input("Enter any no "))
e = int(input("Enter any no "))

agg = a + b + c + d + e
print(agg)
perc = agg / 500 * 100
print(perc)
