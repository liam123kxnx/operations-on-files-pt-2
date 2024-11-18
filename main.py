
file = bankai
x = open (bankai, access_mode)
#open a file

o = open ('nl.txt') 
o = open ('nl_txt', w) #it will open the file for writing

#read a file

nl = open('nl.txt','r') # it will open the file in read mode
nl.readline() # it will read the first line of the file
nl.read(10) # it will read the first 10 charcter of the file
nl.read() # it will return the whole text
#create a file

nl = open ('nl.txt', 'x') # it will create a new empty file but will throw an error if the same file name exists
nl = open ('nl.txt', 'w') # it will create a file but if the same file name exist it will overwrite
# write into an existing file

with open('nl.txt','w') as nl:
    nl.write('This is the first line\n')
    nl.write('This is the second line\n')
    nl.write('this is the third line')

    nl = open('nl.txt', w)

#it allows to write all the line in one go
nl.writelines('This is the first line\n', 'This is the second line\n', 'This is the third line')
nl.close()
