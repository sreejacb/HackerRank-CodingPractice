def mutate_string(string, position, character):
  line= list(string)                    
  for i in range(len(line)):
    if i == position:                   
        line[position] = character  
  return("".join(line)) 

if __name__ == '__main__':
    s =  input("Enter a string: ")
    i, c = input("Enter the position & character: ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)