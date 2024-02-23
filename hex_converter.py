from base64 import b64encode, b64decode

# convert hex value into base64 to complete crypto challenge 1:
def hex_to_base64(hex_value):
    b64_value = b64encode(bytes.fromhex(hex_value)).decode()
    print('hex value in base64:', b64_value)
    return b64_value

# check the converted value is correct
def value_compare(converted_value, key_value):
    if converted_value == key_value:
        print("conversion correct")
    else:
        print("incorrect conversion")

# bonus conversion from base64 to hex
def base64_to_hex(b64_value):
    hex_value = b64decode(b64_value.encode()).hex()
    print(b64_value, 'in hex is:', hex_value)
    return hex_value

# Bonus bonus: converting any string to base64
def string_to_base64(string_value):
    b64_value = b64encode(bytes(string_value, 'utf-8')) # convert string to bytes
    #base64_str = b64_value.decode('utf-8') # convert bytes to string
    print(string_value, "in base64 is:", b64_value)

# Bonus bonus: converting any string to hex
def string_to_hex(string_value):
    hex_value = string_value.encode("utf-8").hex()
    print(string_value, "in hex is:", hex_value)

# allow for user input of their own string
def user_input_converter():
    print("do you want to convert something else?")
    print("yes = 1, no = 0")
    user_input = input()
    if user_input == "1":
        print("What do you want to convert?")
        value_to_convert = input()  # how do I Identify what type of value this is?
        print("what do you want this to be converted to?")
        print("hex = 1, base64 = 0")
        convert_type = input()
        if convert_type == "1":
            #convert to hex
            string_to_hex(value_to_convert)
        if convert_type == "0":
            #convert to base64
            string_to_base64(value_to_convert)
        #else:
            #exit

def main():
    # Convert hex to base64
    # The string:

    # 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
    # Should produce:

    # SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
    # So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

    # Cryptopals Rule
    # Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
    
    # Convert hex value to base64
    b64_value = hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    key_value = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    value_compare(b64_value, key_value)

    #convert base64 back to hex
    key_value = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    hex_value = base64_to_hex(b64_value)
    value_compare(hex_value, key_value)

    user_input_converter()
if __name__ == "__main__":
    main()