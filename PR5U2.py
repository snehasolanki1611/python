import academicmodule as record
record.add_course("MCA", 4, 3.5)
record.add_course("BCA", 3, 4.0)
record.print_record()
print("\nCurrent CGPA:  ",record.calculate_cgpa())
record.drop_course("MCA")
record.print_record()
print("Current CGPA: {}".format(record.calculate_cgpa()))