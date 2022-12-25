"""
Estimate: 25 minutes
Actual:   35 minutes
"""
import datetime
from prac_07.project import Project

MENU = "- (L)oad projects \n" \
       "- (S)ave projects  \n" \
       "- (D)isplay projects \n" \
       "- (F)ilter projects by date \n" \
       "- (A)dd new project  \n" \
       "- (U)pdate project \n" \
       "- (Q)uit"
projects = []
completed_projects = []
incomplete_projects = []

print(MENU)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "l":
        filename = input("Enter file name to load: ")
        in_file = open(filename, "r")
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
        in_file.close()

    elif choice == "s":
        filename = input("Enter the file name to save: ")
        for i in projects:
            print(f"{i.name}\t{i.start_date}\t{i.priority}\t{i.cost}\t{i.completion}", file=filename)

    elif choice == "d":
        for j in projects:
            if j.completion == 100:
                completed_projects.append(j)
            else:
                incomplete_projects.append(j)

        completed_projects.sort(reverse=True)
        incomplete_projects.sort(reverse=True)
        print("Completed projects: ")
        for k in completed_projects:
            print(k)
        print("Incomplete projects: ")
        for l in incomplete_projects:
            print(l)
    elif choice == "f":
        date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        print(f"That day is/was {date.strftime('%A')}")
        print(date.strftime("%d/%m/%Y"))

    elif choice == "a":
        project_name = input("Enter new project name: ")
        project_date = input("Start date (dd/mm/yy):")
        project_priority = input("Priority: ")
        project_cost = input("Cost estimate: $")
        project_complete = input("Percent complete: ")
        new_project = Project(project_name, project_date, project_priority, project_cost, project_complete)
        projects.append(new_project)

    elif choice == "u":
        for i, project in enumerate(projects, 0):
            print(f"{i} {project}")
        number_choice = int(input("Project choice: "))
        print(projects[number_choice])
        new_percentage = int(input("New Percentage: "))
        new_priority = int(input("New Priority: "))
        projects[number_choice] = Project(projects[number_choice].name, projects[number_choice].start_date,
                                          new_priority, projects[number_choice].cost, new_percentage)

    else:
        print("Invalid input")

    print(MENU)
    choice = input(">>> ").lower()