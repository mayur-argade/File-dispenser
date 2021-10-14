import os


myfile=open("hello.txt", "wt")

print("i am so happy", file=myfile)
myfile.close()


# if you created file with the module name it will give you an error

# making folder
os.makedirs('fol1/fol2')

# delete folder
os.rmdir('fol1/fol2')  # can remove empty folders



# learning paths

# to search file exists or not
print(os.path.exists("hello.txt"))

# can check it is folder or file
# folder is also a file representing which files exist inside it
print(os.path.isdir("myf"))
