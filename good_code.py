"""
A well-typed Python module for calculating statistics from a list of numbers.
"""
from typing import List, Tuple


def calculate_statistics(numbers: List[float]) -> Tuple[float, float, float]:
    """
    Calculate basic statistics from a list of numbers.
    
    Args:
        numbers: A list of numerical values
    
    Returns:
        A tuple containing (mean, minimum, maximum) of the input numbers
        
    Raises:
        ValueError: If the input list is empty or contains no valid numbers
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    try:
        mean_value = sum(numbers) / len(numbers)
        min_value = min(numbers)
        max_value = max(numbers)
        
        return (mean_value, min_value, max_value)
    except TypeError as e:
        raise ValueError(f"All elements must be numerical values: {e}")


def validate_input_data(numbers: List[float]) -> bool:
    """
    Validate that all inputs are valid numbers.
    
    Args:
        numbers: List of numbers to validate
        
    Returns:
        True if all elements are numerical, False otherwise
    """
    for num in numbers:
        if not isinstance(num, (int, float)):
            return False
    return True