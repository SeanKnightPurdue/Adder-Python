# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main entry function to call the add_numbers function
def main():
    # Example usage
    num1 = 5
    num2 = 3
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

# Unit test for the add_numbers function
def test_add_numbers():
    assert add_numbers(2, 3) == 5, "Test Case 1 Failed"
    assert add_numbers(-1, 1) == 0, "Test Case 2 Failed"
    assert add_numbers(0, 0) == 0, "Test Case 3 Failed"
    assert add_numbers(100, 200) == 300, "Test Case 4 Failed"
    print("All test cases passed")

if __name__ == "__main__":
    main()
    test_add_numbers()
