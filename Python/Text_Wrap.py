import textwrap

def wrap(string, max_width):
  count = max_width
  list_ = list(string)                          # converting the string into a list
  for _ in range(0,len(list_)):                 # looping through the list 
      list_.insert(count, '\n')                 # inserting a new line character '\n' at the position 'count'
      count+= (max_width+1)                     # incrementing the 'count' by max_width+1
  paragraph = "".join(list_)                    # joining the list into a string
  return (paragraph)                            # returning the string

if __name__ == '__main__':
    string, max_width = input(), int(input())   # taking string and max_width as input from the user
    result = wrap(string, max_width)            # calling the function 'wrap'
    print(result)                               # printing the result


'''You are given a string S and width w .
Your task is to wrap the string into a paragraph of width w.'''    