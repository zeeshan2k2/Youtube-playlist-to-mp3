n = ["asf", "afasf", "af", "12", "13", "14", "gyret"]
length = len(n)
sed = input("do you want to download all or some songs at the end or some at the start:")
der = int(input("how many?:"))

if sed.lower() == "all":
    exit()
elif sed.lower() == "end":
    for i in n[length-der:]:
        print(i)
elif sed.lower() == "start":
    for i in n[:length-der-1]:
        print(i)

