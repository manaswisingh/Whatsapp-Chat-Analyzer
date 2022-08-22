e = input("apna email bata")
if '@' in e:
    p = input("apna password bhi bata")

    if e == "adarsh@gmail.com" and p == "1234":
        print("Welcome")
    elif e == "adarsh@gmail.com" and p!= "1234":
        print("Password Incorrect")
        p = input("password fir se bol")
        if p == "1234":
            print("Finally Correct")
        else:
            print("Still Incorrect")

    else:
        print("Incorrect credentials")
else:
    print("Email galat hai sahi likho")
