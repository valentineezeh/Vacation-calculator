print ('Welcome to Emcee Travel Buddy Calculator!')
print("==================================================================================================================================")

user_name = input ('What is your name? ')
print ('Welcome %s to Emcee Travel Buddy :) ' %(user_name))
print("==================================================================================================================================")

while True:
    user_quit = input("Type 'quit' to exist the app or type 'continue': " )
    if user_quit == "quit":
        print ('You have successfully existed the app.')
        print ('Thanks for using Emcee Travel Buddy Calculator. :)')
        print("==================================================================================================================================")
        break
    
    elif user_quit == "continue":
        print("==================================================================================================================================")
        city_name = input('What is the name of the city you would like to visit: ')
        print("==================================================================================================================================")
        city_cost = float(input('What is the cost of visiting %s from your current location: ' %(city_name)))
        print ('The city you would like to visit is %s' %(city_name))
        print("==================================================================================================================================")
        print ('The cost to travel to %s from your current location is %s' %(city_name, city_cost))
        print("==================================================================================================================================")
        
        hotel_name = input('What is the name of the hotel you would like to stay in while you are in %s? ' %(city_name))
        print("==================================================================================================================================")
        
        hotel_cost = float(input('How much does spending the night in %s cost? ' %(hotel_name)))
        print("==================================================================================================================================")
        
        number_nights = float(input('How many nights will you spend in %s? ' %(hotel_name)))
        print("==================================================================================================================================")
        
        print ('You have chosen to stay in %s and have decided to spend %s nights at the cost of %s per night' %(hotel_name, number_nights, hotel_cost))
        print("==================================================================================================================================")
        
        hotel_bill = hotel_cost * number_nights
        total = city_cost + hotel_bill

    car_question = input("Would you like to rent a vehicle for the number of days you would be staying in %s pick? 'yes' or 'no' ? " %(city_name))
    print("==================================================================================================================================")
    if car_question == "yes":
        car_cost = float(input('What is the cost, the rental company charge for their vehicles? '))
        print("=============================================================================================================================")
        car_rental_days = int(input("How many days will you like to use the car rental services? "))
        rental_bill = car_cost * car_rental_days
        total = total + rental_bill
        print ('Your total travel expenses to %s for a number of %s night in %s will cost you %s with car rental package. ' %(city_name, number_nights, hotel_name, total))
        print("==================================================================================================================================")
    
    elif car_question == "no":
        total = city_cost + hotel_bill
        print ('Your travel expenses without the car rental services is %s' %(total))
        print("==================================================================================================================================")
    
    else:
        print ('Invalid Request')
        print("==================================================================================================================================")