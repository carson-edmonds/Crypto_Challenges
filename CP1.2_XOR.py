import hex_converter
import operator
import base64
# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it 
# the string: 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and 
#when XOR'd against: 686974207468652062756c6c277320657965
# ... should produce: 746865206b696420646f6e277420706c6179

def b64_to_bytes(str):
    bytes = base64.b64decode(str)
    return bytes 

def xor_strings(str1, str2):
    #result = ""
    XOR_val = bytes([x ^ y for x, y in zip(str1, str2)])
    result = base64.b64encode(XOR_val)

    return result.decode()

def xor_check(result, key):
    if result == key:
        print('values match')
    else:
        print('Values don\'t match')


def main():
    x = "1c0111001f010100061a024b53535009181c"
    y = "686974207468652062756c6c277320657965"
    key = "746865206b696420646f6e277420706c6179"

    #convert hex to base64
    b64_value = hex_converter.hex_to_base64(x, locals())
    y_b64 = hex_converter.hex_to_base64(y, locals())

    #convert b64 to bytes
    bytes1 = b64_to_bytes(b64_value) # x
    bytes2 = b64_to_bytes(y_b64) # y
    result = xor_strings(bytes1, bytes2) # x, y
    
    #encode result as b64
    

    #compare actual result with expected result
    key_b64 = hex_converter.hex_to_base64(key, locals())
    print('result is:', result)
    xor_check(result, key_b64)

if __name__ == "__main__":
    main()


