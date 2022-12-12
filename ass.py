import hashlib

def sign(private_key, message):
  # Use the SHA-256 hash function to produce a digest of the message
  digest = hashlib.sha256(message.encode('utf-8')).hexdigest()
  
  # Sign the digest using the private key
  # (In a real implementation, the private key would be used to perform 
some
  # cryptographic operation on the digest, such as encrypting it with the 
RSA
  # algorithm. For the purposes of this example, we will just assume that 
the
  # private key is used to "sign" the digest by appending it to the end of 
the
  # message.)
  signature = digest + private_key
  
  return signature

def verify(public_key, message, signature):
  # Use the SHA-256 hash function to produce a digest of the message
  digest = hashlib.sha256(message.encode('utf-8')).hexdigest()
  
  # Verify the signature by checking if it matches the expected value
  # (In a real implementation, the public key would be used to perform 
some
  # cryptographic operation on the signature, such as decrypting it with 
the RSA
  # algorithm. For the purposes of this example, we will just assume that 
the
  # public key is used to "verify" the signature by checking if it matches 
the
  # expected value.)
  return signature == digest + public_key

# Example usage
private_key = 'SECRET_KEY'
public_key = 'PUBLIC_KEY'
message = 'HELLO WORLD'
signature = sign(private_key, message)

print('Signature:', signature)

# The verification should return True if the signature is valid
is_valid = verify(public_key, message, signature)
print('Signature is valid:', is_valid)

