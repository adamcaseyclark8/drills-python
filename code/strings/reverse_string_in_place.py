# Function to reverse string in place using two-pointer technique
def reverse_string_in_place(string):
    # Convert string to list to mutate it
    char_array = list(string)
    left = 0
    right = len(char_array) - 1

    # Swap characters until the pointers meet in the middle
    while left < right:
        # Swap characters at left and right pointers
        char_array[left], char_array[right] = char_array[right], char_array[left]
        # Move the pointers towards the middle
        left += 1
        right -= 1

    # Convert list back to string
    return ''.join(char_array)
