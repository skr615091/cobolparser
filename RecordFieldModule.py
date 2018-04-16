#
#------------------------------ C L A S S : RecordField -----------------------------#
#


class RecordField:
    fieldLevel = 0
    fieldName = ""
    fieldLength = 0
    fieldType = "" # other options are "numeric","record-structure"
    fieldRedefines = False

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

                #countLeft = str(t_type).count("(")
                #countRight = str(t_type).count(")")

                #if countLeft > 1 or countRight > 1:
                # add code to check for fractional numeric numbers
                
                self.fieldLength = t_type[firstLeft+1:firstRight]

            except ValueError:
                # left parenthesis not found, count the number of X
                num9 = str(t_type).count("9")
                self.fieldLength = num9

            



    def __init__(self, t_level, t_name, t_type="group",t_redef=False):
        self.fieldLevel = t_level
        self.fieldName = t_name.replace(".","")
        
        # call class method to parse the field type
        self.calculateType(t_type)
        
        self.fieldRedefines = t_redef



    def printFields(self):
        print("Field = ",self.fieldLevel, self.fieldName, self.fieldType, self.fieldLength)


    def describe(self):
        indentationAmount = ' ' * int(self.fieldLevel)

        
        #print(indentationAmount,'{\"element\":{\"level\":',self.fieldLevel,',\"name\":',self.fieldName,',\"type\":',self.fieldType,',\"length\":',self.fieldLength,'}')
        print(indentationAmount,str.format('element > level:{0}, name:{1}, type={2}, length={3}',self.fieldLevel,self.fieldName,self.fieldType,self.fieldLength))
            # {"element":{"level":10,
            #             "name":customer,
            #             "type":text,
            #             "length":20}
            # }


        return(("Field",self.fieldLevel,self.fieldName))


    def getLength(self):
        return(int(self.fieldLength))

    
    def getClass(self):
        return("element")
