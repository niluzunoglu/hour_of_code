import textwrap

# HackerRank Python Practice - String - Text Wrap problem

def wrap(string, max_width):
    
    string_part = string[0:max_width]
    string_left = string[max_width:]
     
    if len(string_left)<max_width:
        return string_part+"\n"+string_left
    
    return string_part+"\n"+wrap(string_left,max_width)

        
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
