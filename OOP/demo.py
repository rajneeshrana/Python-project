a_String = "this is\nstring split\t\tand tabbed"
print(a_String)

raw_String = r"this is\nstring ssplit\t\tand tabbed"
print(raw_String)

b_String = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_String)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

error_string = r"this string ends with \\"
print(error_string)
