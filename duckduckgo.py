import urllib
import json

def getResult(query):
    duckduckgo = urllib.urlopen("http://api.duckduckgo.com/?q="+query+"&format=json&pretty=1");
    result = json.load(duckduckgo)
    return result

if __name__ == "__main__":
    query = input("query? (put in quotes) >")
    
    duckduckgo = urllib.urlopen("http://api.duckduckgo.com/?q="+query+"&format=json&pretty=1");
    
    result = json.load(duckduckgo);

    print("Heading: "+result['Heading']);

    print("Response type: "+result['Type']);

    if result['Type'] == 'A':
        print("this is a topic summary")
        print("Definition: "+result['Abstract']);
    elif result['Type'] == 'B':
        print("WHAT??")
    elif result['Type'] == 'C':
        print("this is a category")
    elif result['Type'] == 'D':
        print("This is a disambiguation")
    elif result['Type'] == 'E':
        print("this is a bang redirect, essentially linking to the search function of another website");

