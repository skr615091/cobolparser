from RecordFieldModule import RecordField
from RecordStructureModule import RecordStructure
from ascii_packed import asciiEbcdicConversion

import pickle
import json



# this program parses a cobol copybook
MESSAGES = True
JSON = False
TREE = True


if MESSAGES: print(">>>> Cobol Copybook Parser <<<<<")

# Constants
FILE_NAME = r"C:\Atanu\Projects\Python\CobolCopybookParser\data\SampleCobol.dat"
JSON_FILE = r"C:\Atanu\Projects\Python\CobolCopybookParser\data\Cobol.json"






#
#------------------------------ Global Function -----------------------------#
#

def createFields(copybookLine):

    
    copybookLineFields = copybookLine.split()

    

    if 'redefines' in copybookLineFields:
        print('redefines found')
        print(copybookLineFields)
    


    if len(copybookLineFields) < 5:
        return RecordField(copybookLineFields[1], copybookLineFields[2])
    else:
        return RecordField(copybookLineFields[1], copybookLineFields[2], copybookLineFields[4])

    # end of createFields

def createStructure(recName,recLevel):
        
    global cpyLine

    objRecordStructure = RecordStructure(recName,recLevel)    
    
    while (cpyLine != ""):

        
        objField = createFields(cpyLine)
        
        if objField.fieldType == "group":
            # create a new sub-record structure
    
            cpyLine = str(cpyFile.readline()) # read the next line
            
            subRecordStructure = createStructure(objField.fieldName,objField.fieldLevel)
            
            objRecordStructure.addField(subRecordStructure)

        elif int(objField.fieldLevel) <= int(objRecordStructure.recordStructureLevel):
            break
        else:
            objRecordStructure.addField(objField)
            cpyLine = str(cpyFile.readline()) # read the next line

        # end of while

       
    return(objRecordStructure)


    # if objField.fieldType == "group":
    #     #create a new sub-record structure
    #     objTempRecordStructure = RecordStructure(objField.fieldName)
    #     while (): #same level is not reached, keep exploding

    


#
#------------------------------ M A I N    P R O G R A M -----------------------------#
#

def main():
    global cpyFile
    global cpyLine

    cpyFile = open(FILE_NAME, mode = "r")

    cpyLine = str(cpyFile.readline())

    rootRecordStructure = createStructure("root",0)

    rootRecordStructure.describe()

    print(rootRecordStructure.getLength())

    rootRecordStructure.printPositionalOffsets()

    # asciiConverter = asciiEbcdicConversion()
    
    # print(asciiConverter.getNumberPair('a'))

    
    
    # end of main


# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

