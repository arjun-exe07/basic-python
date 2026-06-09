import pickle
names = ['Alice', 'Bob', 'Charlie']
marks = [85, 92, 78]

pickel_file = open('data.dat' ,"wb")
#wb stands for write binary mode, which is necessary when working with pickle files
pickle.dump(names, pickel_file)
pickle.dump(marks,pickel_file)
pickel_file.close()