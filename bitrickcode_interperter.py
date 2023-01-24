'''
When I was in preschool I wanted a language that stems from mores code so I came up with this and it still works just fine 🙂 almost like Linux but this little written language is almost 20 years old now and yet I did it before I even talked 
Also if you want the basics 

(: is at the end of a word :)

X = _

I = .

'''

#bitrickcode_interperter by Jamous Bitrick
#Version 1.0, 1/24/2023
#English to Bitrickcode: python bitrickcode_interperter I am Jamous
#Bitrickcode to English example: python .\bitrickcode_interperter "(:II:)(:IX:XX:)(:IXXX:IX:XX:XXX:IIX:III:)"

#handle imports
import sys

#Create dictionaries
english_to_bitrickcode = { 'a':'IX', 'b':'XIII', 'c':'XIXI', 'd':'XII', 'e':'I', 'f':'IIXI', 'g':'XXI', 'h':'IIII', 'i':'II', 'j':'IXXX', 'k':'XIX', 'l':'IXII', 'm':'XX', 'n':'XI', 'o':'XXX', 'p':'IXXI', 'q':'XXIX', 'r':'IXI', 's':'III', 't':'X', 'u':'IIX', 'v':'IIIX', 'w':'IXX', 'x':'XIIX', 'y':'XIXX', 'z':'XXII',
                    '1':'IXXXX', '2':'IIXXX', '3':'IIIXX', '4':'IIIIX', '5':'IIIII', '6':'XIIII', '7':'XXIII', '8':'XXXII', '9':'XXXXI', '0':'XXXXX', 
                    ', ':'XXIIXX', 'I':'IXIXIX', '?':'IIXXII', '/':'XIIXI', 'X':'XIIIIX', '(':'XIXXI', ')':'XIXXIX',
                    ' ': ')',
}
bitrickcode_to_english = dict([(value, key) for key, value in english_to_bitrickcode.items()])

input_string = ""
output_string = ""
print(sys.argv)
for element in sys.argv[1:]:
    input_string += element + " "

#If input is blank, terminate program
if input_string == "":
    exit()

#If bitrickcode, convert to english
elif input_string[0:2] == "(:":
  #Make input string upercase
  input_string = input_string.upper()
  
    while input_string != "" and input_string != " ":
        #Define and find word
        word_start_pos = input_string.index("(")
        word_end_pos = input_string.index(')')
        word = input_string[word_start_pos + 2 :word_end_pos] # +2 to accomodate for '(:'
        
        #Translate new word
        current_char = ""
        for char in word:
            #Calculate letter
            if char != ":":
                current_char += char
            #Do work if full letter
            else:
                output_string += bitrickcode_to_english[current_char] + ""
                current_char = ""

        #Insert space after current word
        output_string += " "
        #Remove current word from input_string
        input_string = input_string[word_end_pos+1:]

#Assume english, convert to bitrickcode
else:
    #Make input string lowercase
    input_string = input_string.lower()

    #Open bracket for word start
    output_string += "(:"

    for char in input_string:
        #Handle end of words
        if char == ' ':
            output_string += ")(:"
        #Parse word values
        elif char in english_to_bitrickcode:
            output_string += str(english_to_bitrickcode[char]) + ":"

    #The above loop appends '(:' to everything. lets strip that out
    output_string = output_string[:len(output_string)-2]

print(output_string)
