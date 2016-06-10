#import lexicons
LEXICON_OPTIONS = open("lexicon_options.txt")
lexicons = LEXICON_OPTIONS.read();
print("loding these lexicons: \n"+str(lexicons.replace("use ","")))
lexicons = lexicons.splitlines()
lexicon_temp = []
for lexicon in lexicons:
    if lexicon.startswith("use "):
        lexicon12 = lexicon[4:];
        lexicon_file = open(lexicon12);
        lexicon_temp.append(lexicon_file.read())
lexicons = lexicon_temp
#print("lexicons: "+str(lexicons))

default_message = "I'm not quite sure what you mean..."; #this is the message shown whenever the answer is not found in a lexicon

def findInPhrase(option,phrase, message):
    message = message.strip()
    message = message.lower()
    phrase = phrase.lower()
    
    if option == "c":
        if message.find(phrase) > -1:
            return True
        else:
            return False
    elif option == "v":
        if message == phrase:
            return True
        else:
            return False
    elif option == "s":
        if message.startswith(phrase):
            return True
        else:
            return False
    elif option == "e":
        if message.endswith(phrase):
            return True
        else:
            return False
    else:
        return False
def executeCommand(command):
    command = command.strip()
    if command.lower().startswith("say"):
        speech = command.replace("say ","")
        speech = speech.strip()
        speech = speech.strip("\"")
        return speech
    else:
        return default_message

def decode(message):
    for lexicon in lexicons:
        lexiconRules = lexicon.splitlines()
        for rule in lexiconRules:
            if rule.startswith("#") == False:
                index1 = rule.find("==")
                index2 = rule.find(">")
                option = rule[0:index2]
                phrase = rule[index2+1:index1]
                phrase = phrase.strip()
                isInMessage = findInPhrase(option, phrase, message)
                command = rule[index1+2:]
                command = command.strip()
                if isInMessage:
                    return executeCommand(command)   
    return default_message

if __name__ == "__main__":
    test = decode("hello, how are you")
    print(test)