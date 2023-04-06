ticket = int(input('Количество билетов:'))
count = 0
for i in range(1, ticket+1):
    years_old = int(input('Возраст посетителя:'))
    if years_old < 18:
        count += 0
    elif 18 <= years_old <= 25:
        count += 990
    else:
        count += 1390
if ticket > 3:
    print(count*0.9)
else:
    print(count)
