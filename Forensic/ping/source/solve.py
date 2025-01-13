# tshark -r ping.pcapng -T fields -e icmp.type > data.txt

def binary_to_ascii(binary_str):
    ascii_text = ''.join([chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)])
    return ascii_text

with open("data.txt", "r") as file:
    content = file.read().split()

binary_result = ""
for num in content:
    if num == '49':
        binary_result += '1'
    elif num == '48':
        binary_result += '0'

ascii_result = binary_to_ascii(binary_result)

print("Binary Result:", binary_result)
print("ASCII Text:", ascii_result)
