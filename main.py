# This program takes the input of the customer name and the amount they spent in a day.
# Then the program chooses the customer that spent the most money and displays them as the
# best customer for that day

# Creating the main function where most of the program will run
def main():
    # Establishing the two lists, one for sales and one for names
    sales = []
    names = []

    # Takes the amount spent and name of the customer and assigns them to their corresponding list
    amount = float(input("Enter the sale amount: "))
    while amount != -1:
        sales.append(amount)

        name = input("Enter the customer's name: ")
        names.append(name)

        amount = float(input("Enter the customer's name: "))

    # Finds the customer that spent the most money and displays their name
    bestName = nameOfBestCustomer(sales, names)
    print("The best customer was:", bestName)

# The function that finds the most money spent in the sales list and links the corresponding money spent
# to the customer and then returns the customer name
def nameOfBestCustomer(sales, customers):
    largest = max(sales)

    for i in range(0, len(sales)):
        if sales[i] == largest:
            return customers[i]

# Calling the main function
main()