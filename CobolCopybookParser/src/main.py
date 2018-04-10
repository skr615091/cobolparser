
# this program parses a cobol copybook
print(">>>> Cobol Copybook Parser <<<<<")

# Constants
FILE_NAME = "SampleCobol.cpy"

#
#------------------------------ C L A S S : RecordField -----------------------------#
#


class RecordField:
    fieldLevel = 0
    fieldName = ""
    fieldStart = 0
    fieldLength = 0
    fieldEnd = 0
    fieldType = "" # other options are "numeric","record-structure"

    def calculateType(self,t_type):
            
        self.fieldLength = 0
        if t_type == "group":
            self.fieldType = t_type
            self.fieldLength = 0

        elif t_type[0] in ('x','X'):
            # alpha numeric type
            
            self.fieldType = "text"
                        
            try:
                firstLeft = int(str(t_type).index("("))
                firstRight = int(str(t_type).index(")"))
                
                self.fieldLength = t_type[firstLeft+1:firstRight]

            except ValueError:
                # left parenthesis not found, count the number of X
                numx = str(t_type).count("x")
                numX = str(t_type).count("X")
                self.fieldLength = numx + numX
        else:
            # numeric type

            self.fieldType = "numeric"
            
            try:
                firstLeft = int(str(t_type).index("("))
                firstRight = int(str(t_type).index(")"))

                countLeft = str(t_type).count("(")
                countRight = str(t_type).count(")")

                #if countLeft > 1 or countRight > 1:
                # add code to check for fractional numeric numbers
                
                self.fieldLength = t_type[firstLeft+1:firstRight]

            except ValueError:
                # left parenthesis not found, count the number of X
                num9 = str(t_type).count("9")
                self.fieldLength = num9

            



    def __init__(self, t_level, t_name, t_type="group"):
        self.fieldLevel = t_level
        self.fieldName = t_name.replace(".","")
        
        # call class method to parse the field type
        self.calculateType(t_type)



    def printFields(self):
        print(self.fieldLevel, self.fieldName, self.fieldType, self.fieldLength)

#
#------------------------------ C L A S S : RecordStructure -----------------------------#
#

class RecordStructure:
    recordStructureName = ""
    fieldArray = []

    def addField(self,cpyFieldObj):
        self.fieldArray.append(cpyFieldObj)


    def printFields(self):
        for indx in range(len(self.fieldArray)):
            self.fieldArray[indx].printFields()


    def reorganize(self):
        for indx in range(len(self.fieldArray)):
            if self.fieldArray[indx].fieldType == "group":
                subRecord = RecordStructure(self.fieldArray[indx].fieldName)
                level = self.fieldArray[indx].fieldLevel

                subIndx = 1
                while  self.fieldArray[indx+subIndx].fieldLevel > level:
                    subRecord.addField(self.fieldArray[indx+subIndx])
                    subIndx = subIndx + 1
                



    def __init__(self,structureName):
        self.recordStructureName = structureName


#
#------------------------------ Global Function -----------------------------#
#

def createFields(copybookLine):

    copybookLineFields = copybookLine.split()
    
    if len(copybookLineFields) < 5:
        return RecordField(copybookLineFields[1], copybookLineFields[2])
    else:
        return RecordField(copybookLineFields[1], copybookLineFields[2], copybookLineFields[4])

    # end of createFields

def createStructure():
    pass


#
#------------------------------ M A I N    P R O G R A M -----------------------------#
#

cpyFile = open(FILE_NAME, mode = "r")


cpyLine = str(cpyFile.readline())
firstLine = True


#objRecordStructure = RecordStructure("")


while (cpyLine != ""):  # continue the loop till there are lines available in the copybook

    objField = createFields(cpyLine)
    
    if firstLine:
        if objField.fieldType == "group":
            masterRecordStructure = RecordStructure(objField.fieldName)
        else:
            masterRecordStructure = RecordStructure("root")
        firstLine = False
        
    objRecordStructure.addField(objField)
    
    cpyLine = str(cpyFile.readline()) # read the next line

    # end while loop

objRecordStructure.printFields()

#dataBytes = bytes("Atanu","ascii")
#print(dataBytes[0])




    
     



