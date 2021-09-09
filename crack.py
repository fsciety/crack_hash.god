import hashlib
print("""                                           
 _                                         
| |_ ___ ___ ___ ___ ___             _ _ _ 
|   | .'|  _| . | -_|  _|           | | | |
|_|_|__,|_| |  _|___|_|  _____ _____|_____|
            |_|         |_____|_____|      """)
hash_ = input("Enter the hash: ")
file_pass = input("Enter the file: ")
print("")
counter = 1


with open(file_pass) as f:
    for i in f:
        line = i.strip()
        code = eval("b'"+line+"'")

        if (hashlib.md5(code)).hexdigest() == hash_:

            print("__hash Cracked: <<",line,">> the hash: (",hashlib.md5(code).hexdigest(),")")
            print("<< Hash Cracked in",counter,"counter >>")
            break

        else:
            print(counter,".test: <<",line,">> the hash: (",hashlib.md5(code).hexdigest(),")")
            counter = counter+1