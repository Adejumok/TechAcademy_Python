f = open("abc.txt", 'w')
print("File name: ", f.name)
print("File mode: ", f.mode)
print("is file readable: ", f.readable())
print("is file writeable: ", f.writable())
print("is file closed: ", f.closed)
f.close()
print("is file closed: ", f.closed)
