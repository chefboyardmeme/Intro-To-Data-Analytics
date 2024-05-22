def paintRoom(length, width, height, num_of_doors, num_of_windows):
    # Calculate total area to be painted
    total_area = 2 * (length * height + width * height) - (num_of_doors * 25 + num_of_windows * 10)
    
    # Calculate gallons of paint needed
    gallons_needed = total_area / 315
    
    return gallons_needed

def bmiFormula(userHeight, userWeight):
    # Convert height to meters
    height_meters = userHeight * 0.0254
    
    # Convert weight to kilograms
    weight_kg = userWeight * 0.453592
    
    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    
    # Determine classification
    if bmi < 18.5:
        classification = "Underweight"
    elif bmi < 24.9:
        classification = "Normal"
    elif bmi < 29.9:
        classification = "Overweight"
    else:
        classification = "Obese"
    
    return bmi, classification

def minPayment(balance):
    min_payment = max(10, balance * 0.021)
    return min_payment if min_payment < balance else balance

def charCount(text):
    frequencies = {}
    for char in text.lower().replace(" ", ""):
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

def stringCal(names):
    longest_string = max(names, key=len)
    count = sum(1 for name in names if len(name) > 5)
    j_names = [name for name in names if name.startswith('J') and len(name) <= 5]
    return longest_string, count, j_names

# Main program
while True:
    print("1. Calculate Gallons of Paint Needed")
    print("2. Calculate Body Mass Index (BMI)")
    print("3. Calculate Minimum Payment for Credit Card")
    print("4. Calculate Frequency of Characters in a Text")
    print("5. Calculate String Information")
    print("6. Quit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        length = float(input("Enter the length of the room: "))
        width = float(input("Enter the width of the room: "))
        height = float(input("Enter the height of the room: "))
        num_of_doors = int(input("Enter the number of doors: "))
        num_of_windows = int(input("Enter the number of windows: "))
        
        gallons_needed = paintRoom(length, width, height, num_of_doors, num_of_windows)
        print("Gallons of paint needed:", gallons_needed)
    elif choice == '2':
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
        
        bmi, classification = bmiFormula(height, weight)
        print("BMI:", bmi)
        print("Classification:", classification)
    elif choice == '3':
        balance = float(input("Enter your balance: "))
        min_payment = minPayment(balance)
        print("Minimum payment:", min_payment)
    elif choice == '4':
        text = input("Enter the text: ")
        frequencies = charCount(text)
        print("Character frequencies:", frequencies)
    elif choice == '5':
        names = input("Enter a list of names separated by commas: ").split(',')
        names = [name.strip() for name in names]
        info = stringCal(names)
        print("Longest string:", info[0])
        print("Count of strings with length > 5:", info[1])
        print("Names starting with 'J' and length <= 5:", info[2])
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
