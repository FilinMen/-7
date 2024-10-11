input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
if a > b > c:
    more = a
elif b > a > c:
    more = b
elif c > a > b:
    more = c
more = str(more)
output_data = open("output.txt","w")
output_data.write(more)
input_data.close()
output_data.close()