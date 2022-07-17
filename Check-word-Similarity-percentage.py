file1 = open("file1.txt")
file2 = open("file2.txt")
file1_words=(file1.read()).split(" ")
file2_words=(file2.read()).split(" ")
same_words = (set(file1_words)).intersection(file2_words)
similar_words_percentage = len(same_words)/((len(set(file1_words))+len(set(file2_words)))/2)*100
print("The percentage of similar words is ",similar_words_percentage)
