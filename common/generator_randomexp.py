import rstr

def generate_regexp(randon_string = None) ->str:
    pattern = r'{regex_string}'
    random_string: str = rstr.rstr(pattern)
    return randon_string

if __name__ == '__main__':
    generate_regexp(randon_string='abc')