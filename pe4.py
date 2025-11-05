import wikipedia

result = wikipedia.search("generative artificial intelligence")
print (result)

import wikipedia
import time

start_time = time.perf_counter()

topics = wikipedia.search('generative artificial intelligence')
for topic in topics:
    page = wikipedia.page(topic, auto_suggest=False)
    title = page.title
    references = page.references
    filename = title.replace(' ', '_') + '.txt'
    with open(filename, 'w') as f:
        for reference in references:
            f.write(reference + '\n')



end_time = time.perf_counter()
print(f"Time taken: {end_time - start_time} seconds")

from concurrent.futures import ThreadPoolExecutor

def wiki_dl_and_save(topic):
 
    page = wikipedia.page(topic, auto_suggest=False)
    title = page.title
    references = page.references
   
    filename = title.replace(' ', '_') + '.txt'
    with open(filename, 'w') as f:
        for reference in references:
            f.write(reference + '\n')
    return True
 
def main():
   
    start_time = time.perf_counter()
    topics = wikipedia.search("generative artificial intelligence")
   
    with ThreadPoolExecutor() as executor:
        results = executor.map(wiki_dl_and_save, topics)
 
    end_time = time.perf_counter()
    print("For concurrent,")
    print(f"Time taken: {end_time - start_time} seconds")
 

if __name__ == "__main__":
    main()





