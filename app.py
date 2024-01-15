from flask import Flask, render_template, request, jsonify, session
from Crypto.Hash import SHA512 as sha512
import random
import hashlib
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)

def mod_inverse(a, m):
    d, x, _ = extended_gcd(a, m)
    if d != 1:
        raise ValueError("Inverse does not exist")
    return x % m

def generate_key_pair(bits=8):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 65537  # commonly used value for e
    d = mod_inverse(e, phi_n)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def is_prime_miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        # Ensure the number is odd
        num |= 1
        if is_prime_miller_rabin(num):
            return num

def sign_message(message, private_key):
    n, d = private_key
    hash_value = int.from_bytes(hashlib.sha512(message).digest(), byteorder='big')
    signature = pow(hash_value, d, n)
    print("The Private key is:",private_key)
    print('In Sign Message: The Hashed value is',hash_value)
    print("The Signature Generated is:",signature)
    return signature

def verify_signature(message, signature, public_key):
    n, e = public_key
    print("In Verify Signature Function:",signature,type(signature))
    print("The Public key in Verify is:",public_key)
    hash_value = int.from_bytes(hashlib.sha512(message).digest(), byteorder='big')
    hash_from_signature = pow(signature,e,n)
    print('In Verify Signature: The Hashed value is',hash_value)
    print('In Verify Signature: The Hashed value from signature is',hash_from_signature)
    return hash_value == hash_from_signature

@app.route('/')
def index():
    return render_template('index.html')

def generate_or_get_key_pair():
    if 'key_pair' not in session:
        session['key_pair'] = generate_key_pair()
    return session['key_pair']

@app.route('/generate_signature', methods=['POST'])
def generate_signature():
    message = request.form.get('message')
    _, private_key = generate_or_get_key_pair()
    signature = sign_message(message.encode('utf-8'), private_key)
    return jsonify({'signature': signature})

@app.route('/verify_signature', methods=['POST'])
def verify_signature_route():
    message = request.form.get('message')
    signature_str = request.form.get('signature')
    
    print('Received Message:', message)
    print('Signature Recieved:', signature_str)
    if not signature_str:
        return jsonify({'error': 'Signature is empty'})

    try:
        print("Captured Signature is:",signature_str,type(signature_str))
        signature = int(signature_str)
        print("Converted Signature is:",signature,type(signature))
    except ValueError:
        return jsonify({'error': 'Invalid signature format'})

    public_key, _ = generate_or_get_key_pair()
    is_valid = verify_signature(message.encode('utf-8'), signature, public_key)
    return jsonify({'is_valid': is_valid})


if __name__ == "__main__":
    app.run(debug=True)
