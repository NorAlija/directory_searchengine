import string
#Directories from A-F
directory = ["A", "B", "C", "D", "E", "F"]
prompt = input("Word: ").lower()

def read_and_search_from_files():
    get_index = {}
    test = {}
    #Loop through the directorys
    for folder in directory:
        #Loop through the files 0-50.txt
        for file in range(0,51):
            #Open the files in read mode
            with open(f"{folder}/{file}.txt", "r") as readfile:
                #Read the files
                reading = readfile.read()
                #Split the words into list for tokenization
                words = reading.split()
                #Check if the word is in the words list
                if prompt in words:
                    #Get the index of the keyword
                    index_try = [i for i,x in enumerate(words) if x == prompt]
                    #Save the information to a dictionary in memory index
                    get_index[prompt] = [(f"Folder:{folder}",f"File:{file}", f"Index:{index_try}")]
                    print(get_index)
                    #Count how many time userds word is in the file
                    x = words.count(prompt)
                    #Adding path as a key and x as a count for
                    #how many times a word occurs in a file
                    test[f"{folder}/{file}"] = x
    
   #Sorting the dictionary by highest to lowest
    sorted_dict = dict(sorted(test.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
                    
    
    
        


                    
                

                    

                    
                
    
                    
                    

    
                     
   
                



    