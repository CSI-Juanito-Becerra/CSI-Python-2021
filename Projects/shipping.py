print("Welcome to Simpsons' Shipping")
weight:float = float(input("What is the weight of your package:"))
#ground shipping
if (weight == 2 and weight < 2):
  cost_ground = weight * 1.5 + 20
  print("Ground Shipping: $", float(cost_ground))
elif (weight > 2 and weight < 6):
  cost_ground = weight * 3 + 20
  print("Ground Shipping: $", float(cost_ground))
elif (weight > 6 and weight < 10):
  cost_ground = weight * 4 + 20
  print("Ground Shipping: $", float(cost_ground))
else:
  cost_ground = weight * 4.75 + 20
  print("Ground Shipping: $", float(cost_ground))

cost_ground_premium = 125
print("Ground Shipping Premium: $",float(cost_ground_premium))