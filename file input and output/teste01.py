output_file = open("hello.txt", "w")

lines_to_write = [
    "This is my file.",
    "\nThere are many like it,",
    "\nbut this one is mine."
    ]

output_file.writelines(lines_to_write)
output_file = open("hello.txt", "a")
output_file.writelines("\nNON SEQUITUR")

output_file.close() #a variavel output_file armazena o endereço do arquivo de texto na memória. 

# input_file = open("hello.txt", "r")

# for line in input_file.readlines(): #the .readline() method return a     single line
#     print(line, end="")

# input_file.close()

with open("hello.txt", "r") as source, open("goodbye.txt", "w") as dest:
    for line in source.readlines():
        dest.write(line)
