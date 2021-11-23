def fizzbuzz(number):
    """
    >>> fizzbuzz(4)
    '4'
    >>> fizzbuzz(6)
    'Fizz'
    >>> fizzbuzz(10)
    'Buzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    """
    match number % 3, number % 5:
        case 0, 0: return "FizzBuzz"
        case 0, _: return "Fizz"
        case _, 0: return "Buzz"
        case _, _: return str(number)
