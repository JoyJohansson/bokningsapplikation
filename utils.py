import base64
import random
from datetime import datetime


def generate_random_code():
    return random.randint(100000, 999999)

def generate_booking_reference():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_string = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    booking_reference = f'{timestamp}{random_string}'
    return booking_reference

