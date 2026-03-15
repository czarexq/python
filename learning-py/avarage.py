def avarage():

    amount_of_number = (int(input("Enter amount of numbers: ")))
    
    avarage = 0

    weight = 0

    for i in range(amount_of_number):
        avarage_collect = (int(input("Enter a number: ")))
        weight_collect = (int(input("Enter a weight: ")))

        avarage += avarage_collect * weight_collect 
        weight += weight_collect

    result = avarage / weight

    print(result)

avarage()