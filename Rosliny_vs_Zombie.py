'''
Створіть функцію, яка прийматиме два масиви несортованих чисел (перший - масив рослин, що захищається, другий - атакуючий масив зомбі) і поверне boolean значення в залежність від того чи перемогли захисники.

➡️ Умови:

    Кожен елемент масиву атакує елемент іншого масиву з тим самим індексом масиву. Той, хто вижив, - це число з найбільшим значенням.
    Якщо значення однакове, вони обидва гинуть.
    Якщо одне із значень відсутнє (різна довжина масивів), солдат з непустим значенням виживає.
    Щоб вижити, сторона, що обороняється, повинна мати більше тих, хто вижив, ніж атакуюча сторона.
    У випадку, якщо з обох боків однакова кількість людей, що вижили, перемагає команда з найбільшою початковою силою атаки. Якщо загальна сила атаки з обох сторін однакова, поверніть True.
    Початкова сила атаки є сумою всіх значень у кожному масиві.

Тести:

zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 6, 8 ] -> True
zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4 ] -> False
zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 0, 8 ] -> True
zombies=[ 2, 1, 1, 1 ] plants=[ 1, 2, 1, 1 ] -> True '''
zombies=[ 1, 3, 5, 7 ]
plants=[ 2, 4,]
zombies_t=[[1,3,5,7],[ 1, 3, 5, 7 ],[ 1, 3, 5, 7 ],[2,1,1,1]]
plants_t=[[2,4,6,8],[2,4],[2,4,0,8],[1,2,1,1]]

def start_pawer(units):
    sum_power=0
    for unit in units:
        sum_power+=unit
    return sum_power

def check_lenght(zombies,plants):
    rez=0
    amount_zombies=len(zombies)
    amount_plants=len(plants)
       
    if amount_zombies==amount_plants:
        return zombies,plants
    elif amount_zombies>amount_plants:
        rez=amount_zombies-amount_plants
        for i in range (rez):
            plants.append(0)
        return plants ,zombies
    elif amount_zombies<amount_plants:
        rez=amount_plants - amount_zombies
        for i in range(rez):
            zombies.append[0]
        

'''def battles(zombies,plants):
    count_z=0
    count_p=0
    for i in range(len(zombies)):
        
        if plants[i]>zombies[i]:
            count_p+=1
        elif plants[i]>zombies[i]:
            count_z+=1
    print(count_z,count_p)
    return count_p,count_z'''

def battle(zombies,plants):
    check_lenght(zombies,plants)
    #print(zombies,plants)
    count_z=0
    count_p=0
    #battles(zombies,plants)
    for i in range(len(zombies)):
        
        if plants[i]>zombies[i]:
            count_p+=1
        elif plants[i]<zombies[i]:
            count_z+=1
    #print(count_z,count_p)
    if count_z>count_p:

        print(False)
    elif count_z<count_p:
        print(True)
    elif count_p==count_z:
        power_z= start_pawer(zombies)
        power_p= start_pawer(plants)
        if power_p>=power_z:
            print(True)
        else:
            print(False)

def test_date(zombies_t,plants_t):
    
    for i in range(4):
            
            battle(zombies_t[i],plants_t[i])
            

if __name__== "__main__":
    test_date(zombies_t,plants_t)
    #battle(zombies,plants)