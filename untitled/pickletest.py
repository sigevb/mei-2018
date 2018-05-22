import pickle

dict1 = {'a':100,
         'b':200}

print(dict1)

output = open('save1.pkl', 'wb')
pickle.dump(dict1, output)
output.close()

print("--------------------")

inputFile = open('save1.pkl','rb')
dict1 = pickle.load(inputFile)

inputFile.close()