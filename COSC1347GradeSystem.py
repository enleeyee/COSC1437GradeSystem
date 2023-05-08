import csv

def totalPoints(dictionaryPTS):
    total = 0
    for key in dictionaryPTS:
        total += (dictionaryPTS[key] * 100)
    return total

def calculateGrade(dictionaryPTS, average, row):
    average = 0
    for index in dictionaryPTS:
            average += (float(row[index])*dictionaryPTS[index])
    return average

# ask for which csv file to open
filename = str(input("Enter the exact csv file name to open: "))
print()

individualCheck = str(input("Do you wan to find a certain student (Yes or No): "))
if individualCheck == 'Yes':
    whichStudent = str(input("Which student are you looking for (last name, first name): "))

with open(filename, 'r') as file:
    csvreader = csv.reader(file)
    heading = next(csvreader) # get the header of the csv file

    # initialize all dictionaries based on assignments/labs/readings/exams with the amount of pts associated with them

    readings = {}
    labs = {}
    exams = {}
    midterm = {}
    final = {}
    project = {}
    extraCredit = {}

    # initialize the number of points to -1 and the position of every item to 0
    pts = -1.0
    pos = 0

    # iterate through the header
    for item in heading:

        # find the number of points and only convert if points exist in the file
        parentheses1 = item.find("(")
        parentheses2 = item.find(")")
        if parentheses1 > -1 or parentheses1 > -1:
            parentheses1 += 1
            pts = float(item[parentheses1: parentheses2]) / 100

        # find key terms in the file and associate the position and points based on the key term
        if "Project" in item:
            project[pos] = pts

        elif "Additional" in item:
            extraCredit[pos] = pts

        elif "Lab" in item:
            labs[pos] = pts

        elif "Exam" in item:
            exams[pos] = pts

        elif "Midterm" in item:
            midterm[pos] = pts

        elif "Topic" in item:
            readings[pos] = pts

        pos += 1
    
    # find the total number of points for each section
    totalLabs = totalPoints(labs)
    totalReading = totalPoints(readings)
    totalExam = totalPoints(exams)

    # find the avg of all grades
    # iterate through the rest of the file
    count = 0
    for row in csvreader:
        count += 1
        # calculate reading average
        avgReads = 0
        avgReads = calculateGrade(readings, avgReads, row)
        
        # calculate lab average
        avgLabs = 0
        avgLabs = calculateGrade(labs, avgLabs, row) 
        avgLabs += calculateGrade(extraCredit, avgLabs, row) 
        
        # calculate project 1 grade
        for index in project:
            project1 = (float(row[index])/33.33)*100

        # calculate exam average 
        avgExams = {}
        num = 1
        for index in exams:
            if row[index] != 'N/A':
                avgExams[num] = (float(row[index])*exams[index])
                num += 1

        #calculate midterm grade
        midtermGrade = 0
        midtermGrade = calculateGrade(midterm, midtermGrade, row)

        if avgLabs > 2400:
            avgLabs = 2400

        if individualCheck == 'No':
            print(f"{row[0]}, {row[1]}, {row[4]} - Readings: {avgReads:.2f}, Labs: {avgLabs:.2f}, Project 1: {project1:.2f}")
            examGrade = 0
            for key in avgExams:
                print(f"Exam {key}: {avgExams[key]:.2f}")
                examGrade += avgExams[key]
            
            #calculate final grade letter
            finalGrade = (avgLabs/totalLabs)*15 + ((midtermGrade+examGrade+400)/totalExam)*40 + (avgReads/totalReading)*10 + (project1/200)*20
            finalGrade += (("""Manually input quiz :(""") / 6) * 15
            print(f"Final grade: {finalGrade}%")
            print(input("Press Enter to continue."))

        else:
            if whichStudent == f"{row[0]}, {row[1]}":
                print(f"{row[0]}, {row[1]}, {row[4]} - Readings: {avgReads:.2f}, Labs: {avgLabs:.2f}, Project 1: {project1:.2f}")
                examGrade = 0
                for key in avgExams:
                    print(f"Exam {key}: {avgExams[key]:.2f}")
                    examGrade += avgExams[key]

                #calculate final grade letter
                finalGrade = (avgLabs/totalLabs)*15 + ((midtermGrade+examGrade+400)/totalExam)*40 + (avgReads/totalReading)*10 + (project1/200)*20
                finalGrade += (("""Manually input quiz :(""") / 6) * 15
                print(f"Final grade: {finalGrade}%")

                print(input("Press Enter to continue."))

