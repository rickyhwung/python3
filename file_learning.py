import os

with open('handWriting_OCR.txt') as file_object:
    contents = file_object.readline()
    for i in range(0,len(contents)):
        print(contents)
