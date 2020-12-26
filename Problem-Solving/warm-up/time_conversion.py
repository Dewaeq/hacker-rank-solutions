s = input()

if "PM" in s:
    s = s.replace("PM", '')
    t = s.split(':')
    if t[0] != "12":
        t[0] = str(int(t[0]) + 12)
    else:
        t[0] = "12"
    print(":".join(t))

else:
    s = s.replace("AM", '')
    t = s.split(':')
    if t[0] == "12":
        t[0] = "00"
    print(":".join(t))
