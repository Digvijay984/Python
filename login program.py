#Email=nxtlvl@gmail.com
#pass=1234

email = input("Tera email dal:")
if '@' in email:
    password = input("Tera password bhi dal:")

    if email == "nxtlvl@gmail.com" and password == "1234":
        print("Welocme")
    elif email == "nxtlvl@gmail.com" and password != "1234":
        print("Incorrect password")
        password = input("Password firse dal:")
        if password == "1234":
            print("Finally correct")
        else:
            print("Still incorrect")
    else:
        print("Incorrect cridential")
else:
    print("Email galat hain sahi likho")