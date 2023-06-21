def funkcja(arg1, arg2 = "World", *args, **kwargs):
    print(arg1, arg2, args, len(args), kwargs)
    for x in args:
        print(x)
    for x in kwargs.values():
        print(x)

funkcja("Hello")
funkcja("Hi", "Youtube")
funkcja("Hi", "Youtube", "!", ":-)", autor="Sebastian", rok=2020)

print(1, 2, 3, 4, 5)
