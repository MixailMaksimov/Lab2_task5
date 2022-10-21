def creat_list(n):
    sailor_list = list()
    for i in range(0,n):
        name = input("Введите имя \n")
        age = input("Введите возраст \n")
        print("\n")
        sailor_list.append(name + " " + age)
    sailor_list.sort()
    print("Список всех моряков: " + str(sailor_list))
    return sailor_list
def take_age(n_a):
    age = int(n_a.split(" ")[1])
    return age
def take_name(n_a):
    name = n_a.split(" ")[0]
    return name
n = int(input("Введите количество моряков  \n"))
sailor_list = creat_list(n)
team1 = list()
team2 = list()
for i in range(0,n):
    if (take_age(sailor_list[i]) > 40) or (take_age(sailor_list[i]) < 20):
        team1.append(take_name(sailor_list[i]))
    else:
        team2.append(take_name(sailor_list[i]))
print("Команда 1: " + str(team1) + "\n")
print("Команда 2: " + str(team2) + "\n")