import pickle
dict = {'one': 1, 'two': 2}
file = open('saved_data.txt', 'w')
pickle.dump(dict, file)
file.close()

file = open('saved_data.txt', 'r') 
dict = pickle.load(file)
