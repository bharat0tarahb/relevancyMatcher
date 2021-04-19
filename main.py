#Import neccessary libraries
import spellMatch #custom built spelling match algorithm
import csv #package which helps to load csv file
import argparse #package which helps to fetch inputs from comand line arguments

#this function helps in iterating over list items and find relevant match to input string 
def lookoutforMatch(input_string, data):
    dataList = data.split()
    result = [matcherInstance.findMatch(input_string.lower(), word.lower()) for word in dataList]
    return any(result)

#this function loads the file parses the csv file and ouputs a list of row items
def loadDatafromCSV(file):
    with open(file) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        return [x[0] for x in data]

if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser() 
    ap.add_argument("-i", "--input_string", required=True, help="Input String to Search With") # i is an argument which denoted input string
    ap.add_argument("-f", "--file", required=True, help="Corpus File") # f is another argument that denotes file name of csv file
    args = vars(ap.parse_args()) 
    
    #initiate Spell Matcher instance with distance threshold
    matcherInstance = spellMatch.matcher(0.4)

    #Now lets find match
    corpus = loadDatafromCSV(args["file"]) #contents of the file have been contained in a list object and stored as corpus
    output_list = [item for item in corpus if lookoutforMatch(args["input_string"], item) is True] #using list comprehension to iterate over corpus and find relevant match 
    if len(output_list) != 0:
        print(f'We found {len(output_list)} match(s) for the entered word - {args["input_string"]}')
        for output in output_list:
            print(output)
    else:
        print(f'Sorry, no matches were Found for the entered word - {args["input_string"]}. Please try again!')