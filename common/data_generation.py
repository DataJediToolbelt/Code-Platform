import random
import rstr
from RegexGenerator import RegexGenerator
import exrex

def generate_regexp(random_string) ->str:
    pattern = fr'{random_string}'
    #random_string: str = rstr.xeger(pattern)
    random_string: str = exrex.getone(random_string)
    return random_string

if __name__ == '__main__':
    #random_string ='^4[0-9]{12}(?:[0-9]{3})?$'
    #random_string ='^(?!(000|666|9))\d{3}-(?!00)\d{2}-(?!0000)\d{4}$|^(?!(000|666|9))\d{3}(?!00)/\d{2}(?!0000)\d{4}$'
    # SSN
    #random_string ='^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$'
    # Phone Number
    # random_string='^\\d{3}-\\d{4}$'
    # DOB
    #random_string='^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/((19[2-9][4-9]|200[0-9]|201[0-9]|202[0-5]))$'
    # EIN
    #random_string ='^\\d{2}-\\d{7}$'
    # DLN - CA
    # CA - ^[A-Z]{1}[0-9]{8}$
    # IA - ^[A-Z]{3}[0-9]{2}[A-Z]{4}$
    # NV - ^[0-9]{12}$
    random_string ='^[0-9]{12}$'

    returned_data = generate_regexp(random_string)

    print(f"Random String: {returned_data}")