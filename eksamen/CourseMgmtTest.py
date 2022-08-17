
from CourseMgmt import Course, Teacher, Student

def main():
    allTheCourses = []
    allTheCourses.append(Course(11600,"TEK-1507 Matematikk 1", 10, 2022, 1))
    allTheCourses.append (Course(11601,"TEK-1516 Matematikk 2", 10, 2023, 1))
    allTheCourses.append(Course(11900,"DTE-2511 Videregående Programmering", 10, 2022, 1))
    allTheCourses.append(Course(11806,"DTE-2507 Datakomm og sikkerhet", 10, 2022, 2))
    allTheCourses.append(Course(11809,"DTE-2604 Systemutvikling", 10, 2023, 1))
# Lager noen lærere
    matteLaerer = Teacher("Mattelærer 1", "Realfagsgata 1");
    dataLaerer =  Teacher("Datalærer 1", "Programmeringslunden 15");
# UTSKRIFT: Påkaller toString metoden for en lærer
    print(dataLaerer);
# Knytter kurs til lærere
    matteLaerer.addCourse(allTheCourses[0])
    matteLaerer.addCourse(allTheCourses[1])
    dataLaerer.addCourse(allTheCourses[2])
    dataLaerer.addCourse(allTheCourses[3])
    dataLaerer.addCourse(allTheCourses[4])
# UTSKRIFT: Skriver ut kurs som en lærer har
    dataLaerer.printCourses()
# Lager noen studenter
    flink = Student(10005, "Flink Student", "AltLevertIGodTidgata 1");
    laidback = Student(10006, "Laidback Gamer", "Skippertaksgata 99");
# UTSKRIFT: Skriver ut en student
    print("")
    print(flink)

# Oppretter noen resultater på studentene
    flink.addCourseIdAndGrade(11600, 'A');
    flink.addCourseIdAndGrade(11601, 'A');
    flink.addCourseIdAndGrade(11900, 'B');
    flink.addCourseIdAndGrade(11809, 'A');
    laidback.addCourseIdAndGrade(11600, 'C');
    laidback.addCourseIdAndGrade(11900, 'E');
    laidback.addCourseIdAndGrade(11806, 'C');
# UTSKRIFT: Skriver ut kurs id som en student har, med karakter
    flink.printIdAndGrades()
    print(f"Gjennomsnittskarakter:   {flink.getAverageGrade()}")

main()