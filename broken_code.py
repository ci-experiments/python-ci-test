"""
A Python module for calculating statistics - intentionally broken with type errors.
"""

# Missing proper imports and type hints
def calculate_statistics(numbers):
    # No type annotations, no proper error handling
    mean_value = sum(numbers) / len(numbers)
    min_value = min(numbers)
    max_value = max(numbers)
    
    return mean_value, min_value, max_value  # Returning tuple without proper typing

def validate_input_data(numbers):
    # This function has a logical error - returns True for empty lists
    if not numbers:
        return True  # Wrong! Should return False for empty input
    
    for num in numbers:
        if type(num) == int or type(num) == float:  # Bad practice: using identity instead of isinstance
            continue
        else:
            return False
    
    return True