import random
import string

def generate_random_id(length=10):
    characters = string.ascii_lowercase + string.digits
    random_id = ''.join(random.choice(characters) for i in range(length)) 
    return random_id