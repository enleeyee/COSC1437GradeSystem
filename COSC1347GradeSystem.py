import csv

# UHCOSC1437BiedigerSpring2023_assignment_report_MW_2023-05-05_0013.csv
# UHCOSC1437BiedigerSpring2023_assignment_report_TR_2023-05-05_0048.csv

# Grading for Dan\UHCOSC1437BiedigerSpring2023_assignment_report_MW_2023-05-05_0013.csv
# Grading for Dan\UHCOSC1437BiedigerSpring2023_assignment_report_TR_2023-05-05_0048.csv

# ask for which csv file to open
filename = str(input("Enter the exact csv file name to open: "))
print()

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

    # find the avg of all grades
    # iterate through the rest of the file
    for row in csvreader:

        # calculate reading average
        avgReads = 0.0
        for index in readings:
            avgReads += (float(row[index])*readings[index])
        
        # calculate lab average
        avgLabs = 0.0
        for index in labs:
            avgLabs += (float(row[index])*labs[index])  
        
        # calculate project 1 grade
        for index in project:
            project1 = (float(row[index])/33.33)*100

        # calculate exam average 

        #calculate midterm grade

        #calculate final grade

        print(f"{row[0]}, {row[1]} - Readings: {avgReads:.2f}, Labs: {avgLabs:.2f}, Project 1: {project1:.2f}")
