# Ben Woodfield
# Use Pickle to save to a text (or .py file)
import pickle
# Create and save to the file
dict = {'one': 1, 'two': 2}
file = open('saved_data.txt', 'w') # Change filename here - for python file change .txt to .py
pickle.dump(dict, file)
file.close()

# To re-open the file - although I have not used this yet
file = open('saved_data.txt', 'r')  # Also change .txt to .py here for Python file use
dict = pickle.load(file)
