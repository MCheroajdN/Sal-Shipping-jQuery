weight = 12

#Ground Shipping
if weight <= 2:
  ground_weight = weight * 1.5 + 20

elif weight <= 6:
  ground_weight = weight * 3 + 20

elif weight  <= 10:
  ground_weight = weight * 4 + 20

else:
  ground_weight = weight * 4.75 + 20

print("Ground Weight $", ground_weight)


""" Testing function
weight = 8.4
if weight == 8.4:
  cost_ground = weight * 4 + 20
print("Ground Weight $", cost_ground) """


# Premium Ground Shipping
premium_ground_cost = 125

print ("Ground Shipping Premium $", premium_ground_cost)

# Drone Shipping
if weight <= 2:
  drone_shipping = weight * 4.5

if weight <= 6:
  drone_shipping = weight * 9

if weight <= 10:
  drone_shipping = weight * 12

else:
  drone_shipping = weight * 14.25

print ("Drone Shiping $", drone_shipping)

#Testing drone shipping
"""weight = 1.5
if weight == 1.5:
  drone_shipping = weight * 4.5

print ("Drone Shiping $", drone_shipping)
"""

# Cheapest method if weight 4.8, between the three the Ground Weight shipping is cheapest method
weight = 4.8
if weight == 4.8:
  cost_ground = weight * 3 + 20
print("Ground Weight $", cost_ground)

if weight == 4.8:
  drone_shipping = weight * 9
print ("Drone Shiping $", drone_shipping)

# flat rate: Ground Shipping Premium $ 125.0

