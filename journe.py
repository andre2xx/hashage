import hashlib
import random
import time
from datetime import datetime, date
from opcode import haslocal

maintenant = datetime.now()
hash_maint = hashlib.sha256((str(maintenant)).encode()).hexdigest()
print(hash_maint)

maintenant = datetime.now()
hash_maint = hashlib.sha256((str(maintenant)).encode()).hexdigest()
print(hash_maint)
time.sleep(1)

maintenant = datetime.now()
hash_maint = hashlib.sha256((str(maintenant)).encode()).hexdigest()
print(hash_maint)
#mdofier la variable

password = input("Entrez votre mot de passe : ")
temps= datetime.now().strftime("%d/%m%/y")
hash_password = hashlib.sha256((password + temps)).hexdigest()
print(hash_password)