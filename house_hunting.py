# Write your code here
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input(
    "Enter the percent of your salary to save, as a decimal [.10]: "))

rate_of_return = float(input("Enter the expected rate of return [0.04]: "))

total_cost = float(input("Enter the cost of your dream home: "))
dp = float(input(
    "Enter the percent of your home's cost to save as a down payment [0.25]: ")) * total_cost

# down_payment = total_cost * .25
current_savings = 0
months = 0


while current_savings < dp:
    annual_return_rate = (current_savings * (rate_of_return/12))
    current_savings += (portion_saved*annual_salary/12 + annual_return_rate)

    months += 1

print("Number of months:", months)
