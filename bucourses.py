import urllib.request
import sys
from bs4 import BeautifulSoup

                        ######################## ANLAM EYLEMLE VUKU BULUR! #############################


class Department:                   # class declaration for department
    def __init__(self, code, name):
        self.code = code             # department code
        self.name = name             # department name


class Course:
    def __init__(self, code, name, instructor, course_semester):        # class declaration for courses
        self.instructors = []                   # list of course instructors
        self.semesters = []                     # list of semester the course has opened
        self.code = code                        # course code
        self.name = name                        # course name
        self.instructors.append(instructor)
        self.semesters.append(course_semester)


department_list = []              #list of departments from 2019-Spring semester
department_list.append(Department("ASIA", "ASIAN STUDIES"))
department_list.append(Department("ASIA", "ASIAN STUDIES WITH THESIS"))
department_list.append(Department("ATA", "ATATURK INSTITUTE FOR MODERN TURKISH HISTORY"))
department_list.append(Department("AUTO", "AUTOMOTIVE ENGINEERING"))
department_list.append(Department("BM", "BIOMEDICAL ENGINEERING"))
department_list.append(Department("BIS", "BUSINESS INFORMATION SYSTEMS"))
department_list.append(Department("CHE", "CHEMICAL ENGINEERING"))
department_list.append(Department("CHEM", "CHEMISTRY"))
department_list.append(Department("CE", "CIVIL ENGINEERING"))
department_list.append(Department("CSE", "COGNITIVE SCIENCE"))
department_list.append(Department("COGS", "COMPUTATIONAL SCIENCE & ENGINEERING"))
department_list.append(Department("CET", "COMPUTER EDUCATION & EDUCATIONAL TECHNOLOGY"))
department_list.append(Department("CMPE", "COMPUTER ENGINEERING"))
department_list.append(Department("INT", "CONFERENCE INTERPRETING"))
department_list.append(Department("CEM", "CONSTRUCTION ENGINEERING AND MANAGEMENT"))
department_list.append(Department("CCS", "CRITICAL AND CULTURAL STUDIES"))
department_list.append(Department("EQE", "EARTHQUAKE ENGINEERING"))
department_list.append(Department("EC", "ECONOMICS"))
department_list.append(Department("EF", "ECONOMICS AND FINANCE"))
department_list.append(Department("ED", "EDUCATIONAL SCIENCES"))
department_list.append(Department("CET", "EDUCATIONAL TECHNOLOGY"))
department_list.append(Department("EE", "ELECTRICAL & ELECTRONICS ENGINEERING"))
department_list.append(Department("ETM", "ENGINEERING AND TECHNOLOGY MANAGEMENT"))
department_list.append(Department("ENV", "ENVIRONMENTAL SCIENCES"))
department_list.append(Department("ENVT", "ENVIRONMENTAL TECHNOLOGY"))
department_list.append(Department("XMBA", "EXECUTIVE MBA"))
department_list.append(Department("FE", "FINANCIAL ENGINEERING"))
department_list.append(Department("PA", "FINE ARTS"))
department_list.append(Department("FLED", "FOREIGN LANGUAGE EDUCATION"))
department_list.append(Department("GED", "GEODESY"))
department_list.append(Department("GPH", "GEOPHYSICS"))
department_list.append(Department("GUID", "GUIDANCE & PSYCHOLOGICAL COUNSELING"))
department_list.append(Department("HISTORY", "HISTORY"))
department_list.append(Department("HUM", "HUMANITIES COURSES COORDINATOR"))
department_list.append(Department("IE", "INDUSTRIAL ENGINEERING"))
department_list.append(Department("INCT", "INTERNATIONAL COMPETITION AND TRADE"))
department_list.append(Department("MIR", "INTERNATIONAL RELATIONS:TURKEY,EUROPE AND THE MIDDLE EAST"))
department_list.append(Department("MIR", "INTERNATIONAL RELATIONS:TURKEY,EUROPE AND THE MIDDLE EAST WITH THESIS"))
department_list.append(Department("INTT", "INTERNATIONAL TRADE"))
department_list.append(Department("INTT", "INTERNATIONAL TRADE MANAGEMENT"))
department_list.append(Department("LS", "LEARNING SCIENCES"))
department_list.append(Department("LING", "LINGUISTICS"))
department_list.append(Department("AD", "MANAGEMENT"))
department_list.append(Department("MIS", "MANAGEMENT INFORMATION SYSTEMS"))
department_list.append(Department("MATH", "MATHEMATICS"))
department_list.append(Department("SCED", "MATHEMATICS AND SCIENCE EDUCATION"))
department_list.append(Department("ME", "MECHANICAL ENGINEERING"))
department_list.append(Department("MECA", "MECHATRONICS ENGINEERING"))
department_list.append(Department("BIO", "MOLECULAR BIOLOGY & GENETICS"))
department_list.append(Department("PHIL", "PHILOSOPHY"))
department_list.append(Department("PE", "PHYSICAL EDUCATION"))
department_list.append(Department("PHYS", "PHYSICS"))
department_list.append(Department("POLS", "POLITICAL SCIENCE&INTERNATIONAL RELATIONS"))
department_list.append(Department("PRED", "PRIMARY EDUCATION"))
department_list.append(Department("PSY", "PSYCHOLOGY"))
department_list.append(Department("YADYOK", "SCHOOL OF FOREIGN LANGUAGES"))
department_list.append(Department("SCED", "SECONDARY SCHOOL SCIENCE AND MATHEMATICS EDUCATION"))
department_list.append(Department("SPL", "SOCIAL POLICY WITH THESIS"))
department_list.append(Department("SOC", "SOCIOLOGY"))
department_list.append(Department("SWE", "SOFTWARE ENGINEERING"))
department_list.append(Department("SWE", "SOFTWARE ENGINEERING WITH THESIS"))
department_list.append(Department("TRM", "SUSTAINABLE TOURISM MANAGEMENT"))
department_list.append(Department("SCO", "SYSTEMS & CONTROL ENGINEERING"))
department_list.append(Department("TRM", "TOURISM ADMINISTRATION"))
department_list.append(Department("WTR", "TRANSLATION"))
department_list.append(Department("TR", "TRANSLATION AND INTERPRETING STUDIES"))
department_list.append(Department("TK", "TURKISH COURSES COORDINATOR"))
department_list.append(Department("TKL", "TURKISH LANGUAGE & LITERATURE"))
department_list.append(Department("LL", "WESTERN LANGUAGES & LITERATURES"))

department_list.sort(key=lambda x: x.code)      # sort departments by department code


def arg_to_semester_converter(arg):          # converts given arguments to semesters compatible for links
    year = int(arg[:4])                      # takes first four index of the argument and converts to integer which is year of semester
    term = arg[5:]                           # takes last four index of the argument as semester term(Fall, Spring, Summer)
    if term == 'Spring':                     # if term is spring term number is 2
        term_number = 2
        year -= 1                            # if term is spring, year = year - 1 ; because if 2019-Spring is given link should be 2018/2019-2
    elif term == 'Summer':                   # if term is summer term number is 3
        term_number = 3
        year -= 1
    else:
        term_number = 1
    year2 = year + 1
    semester_given = str(year)+"/"+str(year2)+"-"+str(term_number)      # creates semester by concenating variables
    return semester_given


def semester_to_arg_converter(semester):      # converts semesters in links to arguments for output table
    if semester[10] == '1':                    # if last index of semester is 1 it is 'Fall'
        arg_term = "Fall"
        arg_year = semester[:4]                 # if argument term is 'fall' take year from first 4 index of argument

    elif semester[10] == '2':
        arg_term = "Spring"                     # if argument term is 'spring' take year from index [5,9]
        arg_year = semester[5:9]                # for example if semester is 2018/2019-2, it converts to 2019-Spring

    else:
        arg_term = "Summer"                     # if argument term is 'summer' it has same logic with 'spring'
        arg_year = semester[5:9]
    arg_given = arg_year + "-" + str(arg_term)  # argument string is created by concenating variables
    return arg_given


start_semester = arg_to_semester_converter(sys.argv[1])     # start semester compatible to registration link
end_semester = arg_to_semester_converter(sys.argv[2])       # end semester compatible to registration link

semester_list = [start_semester]            # semester_list contains the semester that will be visited

curr_semester = start_semester              # start semester is the current semester at first

while curr_semester != end_semester:        # iterates semesters between start_semester and end_semester, then appends them to lsit named 'semester_list'
    if int(curr_semester[:4]) < int(end_semester[:4]):
        if int(curr_semester[10]) == 3:
            next_semester_year = int(curr_semester[:4]) + 1
            next_semester_year2 = int(curr_semester[5:9]) + 1
            next_semester_term_no = 1
            next_semester = str(next_semester_year) + "/" + str(next_semester_year2) + "-" + str(next_semester_term_no)
        else:
            next_semester_year = int(curr_semester[:4])
            next_semester_year2 = int(curr_semester[5:9])
            next_semester_term_no = int(curr_semester[10]) + 1
            next_semester = str(next_semester_year) + "/" + str(next_semester_year2) + "-" + str(next_semester_term_no)

    elif int(curr_semester[:4]) == int(end_semester[:4]):
        if int(curr_semester[10]) < int(end_semester[10]):
            next_semester_year = int(curr_semester[:4])
            next_semester_year2 = int(curr_semester[5:9])
            next_semester_term_no = int(curr_semester[10]) + 1
            next_semester = str(next_semester_year) + "/" + str(next_semester_year2) + "-" + str(next_semester_term_no)
    semester_list.append(next_semester)         # semester_list contains all semester program should crawl
    curr_semester = next_semester

output_str = "Dept./Prog. (name) Course, Code, CourseName,"         # output_str is the string that program will output in console at the end
for semester in semester_list:          # adds all semesters to first line of output_str in argument format
    output_str += " " + semester_to_arg_converter(semester) + ","
output_str += " Total Offerings \n"     # first line of output_str is created here

for department in department_list:       # visits each department from department_list
    department_name = department.name
    department_name = department_name.replace(" ", "+")
    department_name = department_name.replace("&", "%26")
    department_name = department_name.replace(":", "%3a")
    department_name = department_name.replace(",", "%2c")       # department_name variable is link compatible form of department names
    courses_in_given_semester_range = []        # list of courses in given semester range
    huge_list = []      # huge_list contains undergraduate, graduate and instructor count data for all courses in all departments and semesters
    # print(huge_list)
    coursess = []       #
    for semester in semester_list:        # visits all semester of the current course
        #link of current department in current semester
        link = "https://registration.boun.edu.tr/scripts/sch.asp?donem=" + semester +"&kisaadi=" + department.code + "&bolum=" + department_name + ""

        with urllib.request.urlopen(link) as response:      # opens current link as response
            data = response.read().decode("ISO-8859-9")     # decode for turkish characters
            soup = BeautifulSoup(data, "html5lib")          # read data with BeautifulSoup
            course_name = ""
            course_code = ""
            course_instructor = ""
            tmpCourse: Course

            for table in soup.find_all('table', border="1"):    # find table with border = "1
                count = 0
                course_count = 0
                for tr in table.find_all('tr', class_=['schtd', 'schtd2']):     # find <tr> tags with classes 'schtd' or 'schtd2' in table(rows of table)
                    if 'labps' not in tr.attrs["class"]:                        # exclude rows with class="labps"
                        for td in tr.find_all('td'):            # find columns in each row
                            if count == 0:
                                index_space = td.text.index(".")
                                course_code = td.text[:index_space]     # course code is first column
                            elif count == 2:
                                course_name = td.text                   # course name is 3.column
                            elif count == 5:
                                course_instructor = td.text  # course_instructor is 6.column
                            count += 1
                            if count == 13:                             # when count is 13 its done with the row
                                count = 0
                                isCourseExists = False

                                for course in courses_in_given_semester_range:
                                    if course.code == course_code:
                                        isCourseExists = True       # if course exists in the list, take that course as variable
                                        tmpIns = course.instructors
                                        break
                                if isCourseExists is True:
                                    for i in tmpIns:
                                        if i == tmpIns:
                                            tag = False
                                            break
                                    tag = True
                                    if tag:         # if instructor is not in instructor list of current course then append to the list
                                        course.instructors.append(course_instructor[:-1])
                                        course.semesters.append(semester)
                                        course.instructors = list(dict.fromkeys(course.instructors))
                                        course.semesters = list(dict.fromkeys(course.semesters))
                                else:               # if course is not in course list then create new course
                                    courses_in_given_semester_range.append(Course(course_code, course_name, course_instructor[:-1], semester))
                                    course_count += 1
                und_count = 0       # undergrad course count for current department for all semesters
                grad_count = 0      # grad course count for current department for all semesters
                instr_count = 0     # unique instructor count for current department for all semesters
                ins = []            # list of unique instructors for current department for all semesters
                for c in courses_in_given_semester_range:
                    coursess.append(c)
                    course_data_list = []
                    if ord(c.code[-3]) < 65:
                        if int(c.code[-3]) <= 4:        # if first number of course code is less than 5 then increment und_count
                            und_count += 1
                        elif int(c.code[-3]) >= 5:      # if first number of course code is less than 5 then increment grad_count
                            grad_count += 1
                    ins += c.instructors

                ins = list(dict.fromkeys(ins))
                instr_count = len(ins)
                course_data_list.append(und_count)      # undergrad course count in current semester of current course
                course_data_list.append(grad_count)     # grad course count in current semester of current course
                course_data_list.append(instr_count)    # unique instructors count in current semester of current course
        huge_list.append(course_data_list)           # append current course data to huge_list
        und_count = 0
        grad_count = 0
        instr_count = 0
        coursess = list(dict.fromkeys(coursess))
        for c in coursess:
            if ord(c.code[-3]) < 65:
                if int(c.code[-3]) <= 4:        # if course code is smaller or equal than 4xx then increment und_count
                    und_count += 1
                elif int(c.code[-3]) >= 5:      # if course code is larger than 4xx then increment grad_count
                    grad_count += 1
    # first line of department info
    output_str += department.name + ","         # append department name to output_str
    output_str += "U" + str(und_count) + " G" + str(grad_count) + ","       #append undergrad count and grad count output_str
    output_str += "-,"
    tempU = 0
    tempG = 0
    tempI = 0
    for i in huge_list:         # print info for each course
        output_str += "U" + str(i[0]) + " "         # concatenate und_count in current semester of current course
        output_str += "G" + str(i[1]) + " "         # concatenate grad_count in current semester of current course
        output_str += "I" + str(i[2]) + ","         # concatenate unique instructor count in current semester of current course
        tempU += i[0]
        tempG += i[1]
        tempI += i[2]
    output_str += "U" + str(tempU) + " "
    output_str += "G" + str(tempG) + " "
    output_str += "I" + str(tempI) + "\n"

    y = 0
    coursess.sort(key=lambda x: x.code)         # sort course according to course code
    for cd in coursess:
        x = 0       #  x/y represents #/# under total offerings column
        output_str += ","
        output_str += cd.code + ","
        output_str += cd.name + ","
        cd.instructors = list(dict.fromkeys(cd.instructors))
        y = len(cd.instructors)
        for sm in semester_list:
            if sm in cd.semesters:
                x += 1                  # if semester is in current course's semester list then increment x
                output_str += "X,"      # if semester is in current course's semester list then concatenate 'X' to output_str
            else:
                output_str += " ,"
        output_str += str(x) + "/" + str(y)     # concatenate total offerings column to output_str
        output_str += "\n"

print(output_str)






