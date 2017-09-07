# Unicode & Encoding 
    a Unicode string is a sequence of code points, which are numbers from 0 to 0x10ffff. 
    This sequence needs to be represented as a set of bytes (meaning, values from 0–255) in memory. 
    The rules for translating a Unicode string into a sequence of bytes are called an encoding.


## Encoding
### UTF-8
    UTF-8 uses the following rules:

    If the code point is <128, it’s represented by the corresponding byte value.
    If the code point is between 128 and 0x7ff, it’s turned into two byte values between 128 and 255.
    Code points >0x7ff are turned into three- or four-byte sequences, where each byte of the sequence is between 128 and 255.

    UTF-8 has several convenient properties:

    It can handle any Unicode code point.
    A Unicode string is turned into a string of bytes containing no embedded zero bytes. This avoids byte-ordering issues, and means UTF-8 strings can be processed by C functions such as strcpy() and sent through protocols that can’t handle zero bytes.
    A string of ASCII text is also valid UTF-8 text.
    UTF-8 is fairly compact; the majority of code points are turned into two bytes, and values less than 128 occupy only a single byte.
    If bytes are corrupted or lost, it’s possible to determine the start of the next UTF-8-encoded code point and resynchronize. It’s also unlikely that random 8-bit data will look like valid UTF-8.

### ASCII encoding
    If the code point is < 128, each byte is the same as the value of the code point.
    If the code point is 128 or greater, the Unicode string can’t be represented in this encoding. (Python raises a UnicodeEncodeError exception in this case.)


# Unicode In Python
    In Python source code, Unicode literals are written as strings prefixed with the ‘u’ or ‘U’ character: u'abcdefghijk'. Specific code points can be written using the \u escape sequence, which is followed by four hex digits giving the code point. The \U escape sequence is similar, but expects 8 hex digits, not 4.
    Python supports writing Unicode literals in any encoding, but you have to declare the encoding being used. This is done by including a special comment as either the first or second line of the source file:
    # -*- coding: latin-1 -*-
    the default encoding used will be ASCII.
    
