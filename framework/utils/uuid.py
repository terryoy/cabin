import random

# used to generate readable UUID
UUID_SOURCE_STR = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# generate UUID strings with specific length
def generate_uuid(count):
    i = count
    strings = []
    while i > 0:
        strings.append(random.choice(UUID_SOURCE_STR))
        i-=1

    return "".join(strings)

# define a UUID of long length
def uuid_tiny():
    return generate_uuid(4)

def uuid_short():
    return generate_uuid(8)

def uuid_normal():
    return generate_uuid(16)

def uuid_long():
    return generate_uuid(32)
