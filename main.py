import random
import string

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# alttaki komut ile rastgele şifrelerinizi oluşturabilirsiniz...

strong_password = generate_strong_password()
print("Oluşturulan Güçlü Şifre:", strong_password)
