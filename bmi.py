# BMI Calculator Function

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).
    
    Parameters:
    weight_kg (float): Weight in kilograms
    height_m (float): Height in meters
    
    Returns:
    float: BMI value rounded to 2 decimal places
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0")

    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)



bmi_result = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi_result}")
