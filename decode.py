def find_most_common():
    filename = input("filename: ")
    file = open(filename, 'r')
    paragraph = file.read()
    letters_list = [0] * 26
    for letter in paragraph:
        # print(f"Start: '{letter}'")
        if letter == "'" or letter == "." or letter == "," or letter == "-":
            continue
        elif ord(letter) > 125:
            continue
        elif letter.isalpha():
            current_letter = letter.lower()
            # print(f"Letter: {current_letter}")
            current_letter_list_val = letters_list[ord(current_letter)-97]
            # print(f"value: {current_letter_list_val}")
            letters_list[ord(current_letter)-97] = current_letter_list_val+1
            # print(f"current_letter_list_val: {current_letter_list_val+1}\n")
        else:
            continue
    max = 0
    for spot in letters_list:
        if spot > max:
            max = spot
    file.close()
    
    print_max = chr(max+97)
    print(f"Most common letter: {print_max}\n")
    # letters_list.sort()
    print(letters_list)
    
    
def replace_letter():
    filename = input("filename: ")
    file = open(filename, 'r')
    replace_this = input("What letter would you like to BE replaced? ")
    replacement_letter = input("What letter would you like to replace it with? ")
    paragraph = file.read()
    replaced_paragraph = ""
    for letter in paragraph:
        if letter == replace_this:
            replaced_paragraph = replaced_paragraph + replacement_letter
        else:
            replaced_paragraph = replaced_paragraph + letter
            
    outfilename = input("Where would you like the output to be stored? ")
    outfile = open(outfilename, 'x')
    outfile.write(replaced_paragraph)
    
        
    

def main():
    print("Hello :)")
    # find_most_common()
    replace_letter()
    print("Exited Successfully. Quitting Program...")
    exit()
    
    
    

if __name__ == '__main__':
    main()