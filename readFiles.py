import string

directory = ["A", "B", "C", "D", "E", "F"]
prompt = input("Word: ").lower()

def read_and_search_from_files():
    
    get_index = {}
    file_count = {}
    count_words = []
    count = 0
    for folder in directory:
        for file in range(0,51):
            with open(f"{folder}/{file}.txt", "r") as readfile:
                reading = readfile.read()
                words = reading.split()
                if prompt in words:
                    index_try = [i for i,x in enumerate(words) if x == prompt]
                    get_index[prompt] = [(f"Folder:{folder}",f"File:{file}", f"Index:{index_try}")]
                    x = words.count(prompt)
                    count_words.append(x)
    count_words.sort(reverse=True)
    print(count_words)
                    #print(count_words)
                    #list_for_count = [x]
                    #print(list_for_count)
                    #test = count_words.sort(reverse=True)
                    #print(test)
                    
                    #path[f"{folder}/{file}"] = count
                    #print(path)
                    
                

                    

                    
                
    
                    
                    

    
                     
   
                



    