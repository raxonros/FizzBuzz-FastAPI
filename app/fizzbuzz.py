# If number is a multiple of three, set it to “Fizz”, for multiples of five set it to “Buzz”. 
# For numbers which are multiples of both three and five set it to “FizzBuzz”.
# For numbers which satisfy neither of these, set it to null / None.
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return None