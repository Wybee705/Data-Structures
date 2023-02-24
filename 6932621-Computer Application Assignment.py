#6932621
#BOAKYE SEKYERE NANA YAW
#https://github.com/Wybee705
Car=["toyota land cruiser","toyota v8","honda civic","honda accord","mitshibushi","toyota rav4","lexus", "ferrari","G-Wagon","benz s-class","toyota vitz","KIA","nissan pickup","ford pickup", "bugatti","BMW","Mesarrartti", "Jeep","Toyota highlander", "wolf wagon","hyundai","toyota camry","toyota sequai v8","cheveroltt SUV","toyota SUV"]
Models=["2001","2005","2010","2015","2020"]
Price=[2453000,4453500,1645600,15035600,23566600]
CarModelPrice=[]
print("Welcome to Wybees Car Garage")
order=input("Name the car you like to buy?")
if order in Car:
   model=input(" enter the model of the car you would like to purchase.")
   if model in Models:
     if model=="2001":
      print("The price of the vehicle chosen is GHS",Price[0])
     elif model=="2005":
      print("The price of the vehicle chosen is GHS",Price[1])
     elif model=="2010":
      print("The price of the vehicle chosen is GHS",Price[2])
     elif model=="2015":
      print("The price of the vehicle chosen is GHS",Price[3])
     elif model=="2020":
      print("The price of the vehicle chosen is GHS",Price[4])
   else:
     print("This model is not available")
else:
 print("This vehicle is not available")
 
      
    