from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

uuid_key = "d8975c4d-19f9-4182-9794-ddea001be5a5"

secret_key = hashlib.sha256(uuid_key.encode()).digest()

with open("FLAG.txt.ryk", "rb") as f:
    encrypted = f.read()

iv = b"\x00" * 16

cipher = AES.new(secret_key, AES.MODE_CBC, iv)

try:
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    print("DECRYPTION SUCCESS:", decrypted.decode(errors="ignore"))

except Exception as e:
    print("DECRYPTION FAIL:", e)
