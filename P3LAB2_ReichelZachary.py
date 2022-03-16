CostofService_OilChange = int('35')
CostofService_TireRotation = int('19')
CostofService_CarWash = int('7')

desired_service = input("Enter desired auto service:\n")
print('You entered: ', end='')
print(desired_service)

if (desired_service=="Oil change"):
   print('Cost of oil change: $', end='')
   print(CostofService_OilChange)
   
elif (desired_service=="Tire rotation"):
   print('Cost of tire rotation: $', end='')
   print(CostofService_TireRotation)
   
elif (desired_service=="Car wash"):
   print('Cost of car wash: $', end='')
   print(CostofService_CarWash)
   
else:
   print('Error: Requested service is not recognized')
