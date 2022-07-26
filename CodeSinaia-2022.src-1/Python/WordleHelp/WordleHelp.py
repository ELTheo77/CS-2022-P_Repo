###
# Main code for WordleHelper program
# Implements the command loop and uses a CmdProcessor
# object to process each of the supported commands

Dict = {}
with open('words.txt') as f:
    lines = f.readlines()
for line in lines:
    res=line.split()
    Dict[res[0]]=int(res[1])
f.close()
print(Dict)

import CmdProcessor as cp

if __name__ == "__main__":
    print("This is Wordle helper!")
    #cmdProcessor = cp.CmdProcessor()
    cmdProcessor = None
    line = input("Command?> ").lower()
    while(line != "quit" and line != "exit"):
        if line == "?" or line == "help":
            cmdProcessor.processHelp()
        elif line.startswith("add"):
            cmdProcessor.processAdd(line)
        elif line.startswith("match"):
            cmdProcessor.processMatch(line)
        elif line.startswith("reset"):
            cmdProcessor.processReset(line)
        elif line.startswith("stats"):
            cmdProcessor.processStats(line)
        elif line.startswith("config"):
            cmdProcessor.processConfig(line)
        elif line.strip():
            # Anything else which is not an empty string
            # is a command which is not supported
            print("#Error: Command not recognized")
        line = input("Command?> ").lower()
    print("Goodbye!")
