name = 'Ahmad Ibn Idris'
age = 20
age_in_days = 20 * 356

height = 74 # In inches
height_in_meters = (74 * 0.0254) # converting inches to meters
height_in_meters = round(height_in_meters)

weight = 180 # lbs
weight_in_kg = (180 * 0.453592) # converting weigt to kilogram
weight_in_kg = round(weight_in_kg)

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall which is equivalent to {height_in_meters} meters.")
print(f"He's {weight} pounds heavy and in kilograms, he is {weight_in_kg} kg.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
