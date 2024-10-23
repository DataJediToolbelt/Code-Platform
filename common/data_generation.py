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
    random_string ='^4[0-9]{12}(?:[0-9]{3})?$'
    returned_data = generate_regexp(random_string)

    print(f"Random String: {returned_data}")