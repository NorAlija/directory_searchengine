

directory = ["A", "B", "C", "D", "E", "F"]

def read_and_search_from_files():
    prompt = input("Word: ").lower()
    for folder in directory:
        for file in range(0,51):
            with open(f"{folder}/{file}.txt", "r") as readfile:
                if prompt in readfile.read():
                    print(f"{folder}/{file}.txt")
                     
   
                



    