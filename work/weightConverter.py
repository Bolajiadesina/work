weight = input("Weight:  ")
weight_type = input ("(K)g or (L)bs: ")


if weight_type == "K" or weight_type == "k":
    new_weight = float(weight) * float(2.20462262)
    print("Weight in Kg: "+ str(new_weight))
elif weight_type == "L" or weight_type == "l":
    new_weight = float (weight) / float(2.20462262)
    print ("Weight in Lbs: " + str(new_weight))
else:
    print("Invalid parameter")
