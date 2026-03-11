def get_even_numbers():
    
    print("Enter integers (one per line).")
    print("Press Enter twice or type 'done' when finished.\n")
    
    numbers = []
    
    while True:
        user_input = input("Number: ").strip()
        
        if user_input.lower() in ('', 'done'):
            break
            
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("That's not a valid integer. Try again.\n")
    
    # Filter even numbers
    even_numbers = [n for n in numbers if n % 2 == 0]
    
    print("\nYou entered:", numbers)
    print("Even numbers:", even_numbers)
    
    return even_numbers


# Run the function
if __name__ == "__main__":
    get_even_numbers()
