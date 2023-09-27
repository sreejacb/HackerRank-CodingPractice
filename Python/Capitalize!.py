
def capitalize(s):
  line= list(s.split(" "))                    # splitting the string into a list of words
  for i in line:
    if i.isalpha() == True:                   # checking if the word is alphabetic
        line[line.index(i)] = i.capitalize()  # if the i is a alphabet, capitalizing the word and replacing it in the list
  return(" ".join(line))                      # joining the list into a string and returning it

if __name__ == '__main__':                    
    s = input()                               # input from the user 
    result = capitalize(s)                    # calling the function                  
    print(result)                             # printing the result

    
''''''