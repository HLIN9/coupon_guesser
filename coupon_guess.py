'''
Saw this at the beginning of coding career; giving it a try
Thought process:
- Have a limit on the lenght of said 'password' - user input or preset value?
- Mix and match - like counting, but instead of base 10, will be like base 'x', with x being the amount of keys people commonly use
- Count until a match is found - in this case, the password, although you'd probably get shut out by the system before you reach the right password;
- So... More of a coupon machine
'''
def product(s, repeat):
    """Generates all possible combinations of the elements in s of length repeat"""
    if repeat == 1:
        # Base case: return the elements of s as individual tuples
        return [(e,) for e in s]
    else:
        # Recursive case: generate all possible combinations of length repeat-1
        # and append each element of s to create longer combinations
        result = []
        subproducts = product(s, repeat-1)
        for p in subproducts:
            for e in s:
                result.append(p + (e,))
        return result
    
def cartesian_product(s, n:int):
    """Generates all Cartesian products of the set s up to length n"""
    for i in range(1, n+1):
        # Generate all possible combinations of length i
        for c in product(s, repeat=i):
            print(''.join(c))

def main():
    print("Welcome to the Coupon guesser!")
    length_limit = int(input("Please enter the length of the password you wish to generate:"))
    elements = []
    for i in range(32, 127):
        elements.append(chr(i))
    cartesian_product(elements, length_limit)

if __name__ == '__main__':
    main()