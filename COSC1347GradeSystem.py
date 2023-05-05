import csv

# UHCOSC1437BiedigerSpring2023_assignment_report_MW_2023-05-05_0013.csv
# UHCOSC1437BiedigerSpring2023_assignment_report_TR_2023-05-05_0048.csv

# ask for which csv file to open
filename = str(input("Enter the exact csv file name to open: "))
print()

with open(filename, 'r') as file:
    csvreader = csv.reader(file)
    heading = next(csvreader) # get the header of the csv file

    # initialize all lists based on assignments/labs/readings/exams with the amount of pts associated with them
    readings = []
    readingpts = []

    labs = []
    labpts = []

    exams = []
    exampts = []

    midterm = []
    midtermpts = []

    final = []
    finalpts = []

    project = []
    projectpts = []

    eclab = []
    eclabpts = []

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
            project.append(pos)
            projectpts.append(pts)

        elif "Additional" in item:
            eclab.append(pos)
            eclabpts.append(pts)

        elif "Lab" in item:
            labs.append(pos)
            labpts.append(pts)

        elif "Exam" in item:
            exams.append(pos)
            exampts.append(pts)

        elif "Midterm" in item:
            midterm.append(pos)
            midtermpts.append(pts)

        elif "Topic" in item:
            readings.append(pos)
            readingpts.append(pts)

        pos += 1

    # find the avg of all grades
    # iterate through the rest of the file
    for row in csvreader:

        # calculate reading average
        avgReads = 0.0
        for i in range(len(readings)):
            avgReads += (float(row[readings[i]])*readingpts[i])
        
        # calculate lab average
        avgLabs = 0.0
        for i in range(len(labs)):
            avgLabs += (float(row[labs[i]])*labpts[i])    
        
        # calculate project 1 grade
        project1 = (float(row[project[0]])/projectpts[0])*100

        # calculate exam average 

        #calculate midterm grade

        #calculate final grade

        print(f"{row[0]}, {row[1]} - Readings: {avgReads:.2f}, Labs: {avgLabs:.2f}, Project 1: {project1:.2f}")