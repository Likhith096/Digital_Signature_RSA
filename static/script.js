function generateSignature() {
    var message = document.getElementById('message').value;
    console.log(message);
    fetch('/generate_signature', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('signatureResult').innerText = 'Signature: ' + data.signature;
    });
}

function verifySignature() {
    var message = document.getElementById('message').value;
    console.log(message);
    var signature = parseInt(prompt('Enter the signature (as a number):'));
    console.log(signature);

    if (isNaN(signature)) {
        alert('Invalid signature format. Please enter a valid number.');
        return;
    }

    fetch('/verify_signature', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ message: message, signature: signature }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('verificationResult').innerText = 'Signature valid: ' + data.is_valid;
    });
}