file = open("listOfStudentHeight.txt", 'a')
name = input("Enter new student name:")
height = input("Enter student height in meters:")
file.write("\n"+name + "\t" + height)
file.close()
class CalUtils():
    def __init__(self):
        self.names = ""
        self.heights = 0
        self.totalStudentHeight = []
        self.totalStudentCount = 0

    def calAvgHeight(self):
        file = open("listOfStudentHeight.txt", 'r')
        for line in file:
            fields = line.split('\t')
            self.names = fields[0]
            heights = fields[1].replace("\n", "")
            self.totalStudentHeight.append(float(heights))
        avg = sum(self.totalStudentHeight) / len(self.totalStudentHeight)
        print(avg)

call = CalUtils()
call.calAvgHeight()
