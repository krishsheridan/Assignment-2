#Import the random module to enable random numbers
import random

class Product:

    def __init__(self):
        #prompt user for all product details
        self.code = self.get_input("Please enter the Product Code: ", int)
        self.name = input("Please enter the Product Name: ")
        self.stock_level = self.get_input("Please enter the Current Stock: ", int)
        self.sale_price = self.get_input("Please enter the Product Sale Price: ", float)
        self.manufacture_cost = self.get_input("Please enter the Product Manufacture Cost: ", float)
        self.monthly_units = self.get_input("Please enter Estimated Monthly Production: ", int)
        #intitialize the sold, revenue, and costr functions
        self. total_sold = 0
        self.total_revenue = 0.0
        self.total_cost = 0.0

    def __str__(self):
        #this is the string with all the product details
        return (f"Product Code: {self.code}\n"
                f"Product Name: {self.name}\n"
                f"Stock Level: {self.stock_level}\n"
                f"Product Sale Price: {self.sale_price}\n"
                f"Product Manufacture Cost: {self.manufacture_cost}\n"
                f"Estimated Monthly Units Manufactured: {self.monthly_units}")
    
    def generate_statement(self):
        #sales for each month
        for month in range(1,13):
            self.simulate_month(month)
            #print the sold, revenue, cost, and profit functions
            print(f"Total Sold: {self.total_sold}\n"
                  f"Total Revenue: ${self.total_revenue}\n"
                  f"Total Cost: ${self.total_cost}\n"
                  f"Profit: ${self.total_revenue - self.total_cost:.2f}")

    #simulate sales for all months        
    def simulate_month(self,month):

        manufactured_this_month = self.monthly_units
        self.stock_level += manufactured_this_month
        sold = random.randint(max(0, manufactured_this_month - 15), manufactured_this_month + 15)
        self.total_sold += sold
        self.total_revenue += sold * self.sale_price
        self.total_cost += manufactured_this_month * self.manufacture_cost
        self.stock_level -= sold

        #print a summary of all months sales and remaining stocks
        print(f"MONTH [{month}]\nUnits Sold: {sold}\nStock Level: {self.stock_level}")

    def get_input(self, prompt, value_type):
        while True:
            try:
                #prompt for input and return specific type
                return value_type(input(prompt))
            except: ValueError
            #print the error message if input is not the specific type
            print("Invalid input, please try again.")

#MAIN
print("Welcome")

product = Product()
#print all product details
print(Product)
#generates and prints all months statements
product.generate_statement()
