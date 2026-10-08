
while True:
    distance = input("\n1. Kilometers to Meters \n2. Meters to cm \n3. cm to mm \n4. Exit \nChoose an option between 1-4: ")

    if distance == "1":
        km = int(input("How many kilimeters: "))
        ans = km*1000
        print(ans)

    elif distance == "2":
            m = int(input("How many meters: "))
            ans = m*100
            print(ans)

    elif distance == "3":
            cm = int(input("How many cm: "))
            ans = cm*10
            print(ans)

    elif distance == "4":
          print("Bye you have exitied the app")
          break

    else:
        print("Please enter something that is vaild")

