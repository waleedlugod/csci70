### Scanner program
# Running the program will prompt for a file name which contains the input character stream
# Input file name must have the word "input" and be a .txt file

# global variables
inputfile = input(
    "File name: "
)  # input file name; should be a .txt file with the word "input" in the name
if "input" not in inputfile or not inputfile.endswith(".txt"):
    exit()
state = "A"  # current DFA state
input_stream = ""  # list of character inputs
index = 0  # index of the current char in the input stream
lexeme_build = ""  # variable to build the final lexeme


# proceeds to the next state
def runState():
    global index
    global state
    global lexeme_build
    lexeme = ""  # final lexeme string
    token_id = ""
    char = input_stream[index]

    # if/else chain for each DFA path
    if state == "A":
        if char == "+":
            token_id = "PLUS"
            lexeme = "+"
        elif char == "-":
            token_id = "MINUS"
            lexeme = "-"
        elif char == "=":
            state = "E"
        elif char.isdigit():
            lexeme_build = char
            state = "B"
        elif char.isspace():
            state = "A"
        else:
            state = "ERROR"
    elif state == "B":
        if char.isdigit():
            lexeme_build += char
            state = "B"
    elif state == "E":
        if char == "=":
            token_id = "ASSIGN"
            lexeme = "=="
            state = "A"
        else:
            state = "ERROR"

    # pushback for NUM token
    if state == "B" and (
        index + 1 >= len(input_stream)  # there is no next char
        or not input_stream[index + 1].isdigit()  # next char is not a digit
    ):
        token_id = "NUM"
        lexeme = lexeme_build
        state = "A"

    index += 1
    return {"ID": token_id, "lexeme": lexeme}


input_stream = open(inputfile).readline()  # get input stream from file
open(inputfile.replace("input", "output"), "w").close()  # clear output file
output = open(  # prepare to write to output file
    inputfile.replace("input", "output"), "a"
)

# process each char in input stream
for char in input_stream:
    q = runState()
    # valid token is found
    if state != "ERROR" and q["lexeme"] != "":
        output.write(q["ID"] + "\t" + q["lexeme"] + "\n")
    # error
    elif state == "ERROR":
        output.write(
            'Lexical Error reading character "' + input_stream[index - 1] + '"\n'
        )
        exit()
