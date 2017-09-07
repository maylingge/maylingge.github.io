# Unicode & Encoding 
    a Unicode string is a sequence of code points, which are numbers from 0 to 0x10ffff. 
    This sequence needs to be represented as a set of bytes (meaning, values from 0–255) in memory. 
    The rules for translating a Unicode string into a sequence of bytes are called an encoding.


## Encoding
### UTF-8
### ASCII encoding
    If the code point is < 128, each byte is the same as the value of the code point.
    If the code point is 128 or greater, the Unicode string can’t be represented in this encoding. (Python raises a UnicodeEncodeError exception in this case.)
