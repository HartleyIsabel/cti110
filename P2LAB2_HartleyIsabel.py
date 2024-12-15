'''
Isabel Hartley
06 Oct 2024
P2LAB2
Creating a dictionary
'''

car_mpg={ 'Camaro':18.21,'Prius':52.36,'Model S':110,'Silverado':26}
print(car_mpg.keys())
car= input('enter a vehicle to see it\'s mpg:')
print('The ' + car + 'gets' + str(car+mpg[car])+'mpg.')
miles=int(input('How many miles will you drive the' + car +'? '))
gallons = miles/ car+mpg[car]
print(str(round(gallons, 2)) + 'gallon(s) of gas are needed to drive the' + car + ''+ str(miles)+ 'miles.')
