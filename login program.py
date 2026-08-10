#Email=nxtlvl@gmail.com
#pass=1234

email = input("Tera email dal:")
password = input("password bhi dal:")

if email == "nxtlvl@gmail.com" and password == "1234":
    print("welcome")
elif email == "nxtlvl@gmail.com" and password != "1234":
        print("Incorrect password")
        input("password firse bol:")
else:
    print("incorrect credintial")

