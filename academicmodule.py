courses = {}
def add_course(course_name, credits, earned_points):
       
        if credits <= 0:
            print("Credits must be a positive number.")
        elif earned_points < 0:
            print("Earned points cannot be negative.")
        else:
            courses[course_name] = {"credits": credits, "points": earned_points}
            print("\nCourse {} added with {} credits and {} earned points.".format(course_name,credits,earned_points))
            print(courses)

def drop_course(course_name):
     
        if course_name in courses:
            del courses[course_name]
            print("\nCourse '{}' has been dropped.".format(course_name))
        else:
            print("\nCourse '{}' not found.".format(course_name))
def print_record():
        if not courses:
            print("No courses in the record.")
            return
        print("Academic Record:")
        print(courses)
        for course, details in courses.items():
            print("\nCourse: {}, Credits: {}, Earned Points: {}".format(course,details['credits'],details['points']))

def calculate_cgpa():
        total_credits=0
        total_points=0
        for c,d in courses.items():
            total_credits=total_credits+d['credits']
            total_points =total_points+d["credits"] * d["points"]

        print("Total creadits : ",total_credits)
        print("Total Points : ",total_points)
        if total_credits == 0:
            return 0.0
        cgpa = total_points / total_credits
        return cgpa





