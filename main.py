#Repo Pattern
#Create
#class vehicleRepository: 
 #def __init__(self):
  #self.allowed_vehicles = [
      #'Ford F-150',
      #'Chevrolet Silverado',
      #'Tesla CyberTruck',
      #'Toyota Tundra',
      #'Nissan Titan'
  #]
#Read
#def get_all_vehicle(self):
  #return self.allowed_vehicles
#Update 
#def add_vehicle(self, vehicle_name):
  #if vehicle_name in self.allowed_vehicles:
    #return False
  #self.allowed_vehicles.append(vehicle_name)
  #return True
#Delete
#def search_vehicle(self, vehicle_name):
  #return vehicle_name in self.allowed_vehicles

#vehicle_repo = vehicleRepository()

#Define List(Array) 
AllowedVehiclesList = [
   'Ford F-150',
   'Chevrolet Silverado',
   'Tesla CyberTruck',
   'Toyota Tundra',
   'Nissan Titan'
]

#Define function to print the menu
def print_menu():
 print('********************************')
 print('AutoCountry Vehicle Finder v0.3')
 print('********************************')
 print('Please Enter the following number below from the following menu:')
 print('1. PRINT all Authorized Vehicles')
 print('2. SEARCH for Authorized Vehicle')
 print('3. ADD Authorized Vehicle')
 print('4. Exit') 
 print('********************************')  

#Define function to print the list of authorized vehicles
def print_vehicles():
  print('\nThe AutoCountry sales manager as authorized the purchase and selling of the following vehicles:')
  for vehicle in AllowedVehiclesList:
    print(vehicle)
  print ()

#Define function to search for a vehicle
def search_vehicle():
  vehicle_name = input('\nPlease Enter the full vehichle name: ')
  if vehicle_name in AllowedVehiclesList:
     print(f'\n{vehicle_name} is an authorized vehicle')
  else:
      print(f'\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again.') 
  print () 

#Define function to add a vehicle
def add_vehicle():
  vehicle_name = input('\n Please enter the full vehicle name you would like to add: ')
  if vehicle_name in AllowedVehiclesList: 
    print(f'\n {vehicle_name} is already an authorized vehicle.')
  else:
    AllowedVehiclesList.append(vehicle_name)
    print(f'\nYou have added "{vehicle_name}" as an authorized vehicle.')
  print()   

#Define the main loop
while True:
  print_menu()
  choice = input('\nEnter your choice:')

  if choice == '1':
    print_vehicles()
  elif choice == '2':
    search_vehicle()
  elif choice == '3':
    add_vehicle()
  elif choice == '4':
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
    break
  else:
    print('Invalid choice, please try again')
