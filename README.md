# Cryptography Project: Digital Signature with RSA and SHA-512

## Overview

This cryptography project implements digital signatures using the RSA (Rivest–Shamir–Adleman) algorithm for key generation and signing, along with the SHA-512 (Secure Hash Algorithm 512-bit) for message hashing. Digital signatures provide a secure way to verify the authenticity and integrity of digital messages or documents.

## Features

- **RSA Algorithm**: Utilizes RSA for key generation and digital signature creation.
- **SHA-512 Hashing**: Implements SHA-512 for secure and efficient message hashing.
- **Signature Verification**: Provides a mechanism to verify the authenticity and integrity of digitally signed messages.
- **Command-Line Interface (CLI)**: Enables easy interaction with the tool through a simple command-line interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/cryptography-rsa-digital-signature.git
    cd cryptography-rsa-digital-signature
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Generate RSA key pair:

    ```bash
    python main.py generate_key
    ```

2. Sign a message:

    ```bash
    python main.py sign --private_key private.pem --message "Your message here"
    ```

3. Verify a signature:

    ```bash
    python main.py verify --public_key public.pem --message "Your message here" --signature signature.txt
    ```

## Example

1. Generate RSA key pair:

    ```bash
    python main.py generate_key
    ```

2. Sign a message:

    ```bash
    python main.py sign --private_key private.pem --message "Hello, world!"
    ```

3. Verify the signature:

    ```bash
    python main.py verify --public_key public.pem --message "Hello, world!" --signature signature.txt
    ```

## Contributors

- Your Name (@your-username)
- Contributor 1 (@contributor-1)
- Contributor 2 (@contributor-2)

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code.
