formatter = "{} {} {} {}" #This line create 4 placeholders for strings formatting to be stored in the variable formatter

print(formatter.format(1, 2, 3, 4)) # Distributes the four arguments in the format function into formatter above
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, "True"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
