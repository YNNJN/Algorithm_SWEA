import base64
t = int(input())
for i in range(1, t + 1):

    string = input()
    string_byte = string.encode('ASCII')
    decoded_string = base64.b64decode(string_byte)
    message = decoded_string.decode('ASCII')
    result = f'#{i} {message}'
    print(result)