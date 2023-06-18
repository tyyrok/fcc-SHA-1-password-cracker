import hashlib

def crack_sha1_hash(hash, use_salts=False):
    password = ''

    f = open('./top-10000-passwords.txt', encoding='cp1252')
    passwords = f.read().split('\n')
    f.close()

    f = open('./known-salts.txt')
    salts = f.read().split('\n')
    f.close()

    if use_salts:
        
        for i in range(len(passwords)):
            for j in range(len(salts)):

                saltedBefore = salts[j] + passwords[i]
                saltedAfter = passwords[i] + salts[j]

                guessBefore = hashlib.sha1(saltedBefore.encode('utf-8')).hexdigest()
                guessAfter = hashlib.sha1(saltedAfter.encode('utf-8')).hexdigest()


                if guessBefore == hash:
                    password = passwords[i]
                    return password
                
                if guessAfter == hash:
                    password = passwords[i]
                    return password
            
    else:

        for i in range(len(passwords) - 1):
            guess = hashlib.sha1(passwords[i].encode('cp1251')).hexdigest()

            if guess == hash:
                password = passwords[i]
                return password

    if password == '':
        return('PASSWORD NOT IN DATABASE')
    else:
        return password
   