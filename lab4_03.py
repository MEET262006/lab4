def count_alphabets_digits(input_string):
    alphabet_count = sum(c.isalpha() for c in input_string)
    digit_count = sum(c.isdigit() for c in input_string)
    
    return alphabet_count, digit_count

