#
#------------------------------ C L A S S : RecordStructure -----------------------------#
#

class RecordStructure:
    recordStructureName = ""
    recordStructureLevel = 0
    fieldArray = []
    recordLength = 0
    
    def getClass(self):
        return("group")

    def describe(self):
        indentationAmount = ' ' * int(self.recordStructureLevel)

        objectDescription = ["Record",self.recordStructureLevel,self.recordStructureName]
        #print(indentationAmount,'{\"group\":{\"level\":', self.recordStructureLevel,',\"name\":',self.recordStructureName,'}')
        print(indentationAmount,str.format('group > level:{0}, name:{1}',self.recordStructureLevel,self.recordStructureName))
        # {"group":{"level":10,
        #           "name":salary}
        
        # }
        for indx in range(len(self.fieldArray)):
            # print(self.fieldArray[indx].describe())
            objectDescription.append(self.fieldArray[indx].describe())

        #print(indentationAmount,"}")
        return(tuple(objectDescription))

        
    def addField(self,cpyFieldObj):
        self.fieldArray.append(cpyFieldObj)
        
        
        

    def printFields(self):
        
        # print(self.fieldArray[0].fieldName,self.fieldArray[0].__class__)
        # print(self.fieldArray[1].fieldName,self.fieldArray[1].__class__)
        # print(self.fieldArray[2].fieldName,self.fieldArray[2].__class__)
        # print(self.fieldArray[3].fieldName,self.fieldArray[3].__class__)
        # print(self.fieldArray[4].recordStructureName,self.fieldArray[4].__class__)
        # print(self.fieldArray[5].fieldName,self.fieldArray[5].__class__)
        # print(self.fieldArray[6].fieldName,self.fieldArray[6].__class__)
        # print(self.fieldArray[7].fieldName,self.fieldArray[7].__class__)
        

        # for indx in range(len(self.fieldArray)):
        #     print(self.fieldArray[indx].__class__)
        #     if "Field" in str(self.fieldArray[indx].__class__):
        #         print(self.fieldArray[indx].fieldName)
        #     else:
        #         print(self.fieldArray[indx].recordStructureName)
        pass


    
    def __init__(self,structureName="root", structureLevel=0):
        self.recordStructureName = structureName
        self.recordStructureLevel = structureLevel
        self.fieldArray = []
        self.recordLength = 0

    def getLength(self):
        return(int(self.calculateRecordLength()))

    def calculateRecordLength(self):

        tempRecLength = 0

        for indx in range(len(self.fieldArray)):
            tempRecLength = tempRecLength + int(self.fieldArray[indx].getLength())

        self.recordLength = tempRecLength

        return(self.recordLength)

    
    def printPositionalOffsets(self,initPos = 0):

        cursor = initPos

        for indx in range(len(self.fieldArray)):
            if self.fieldArray[indx].getClass() == "element":
                print(self.fieldArray[indx].fieldName, cursor + 1,cursor + int(self.fieldArray[indx].fieldLength))
                cursor = cursor + int(self.fieldArray[indx].fieldLength)
            else:
                cursor = self.fieldArray[indx].printPositionalOffsets(cursor)

        return(cursor)


    
    
    def createJSONStructure(self):
        pass
