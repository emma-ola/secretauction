# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the
# names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary
# called student_grades that should contain student names for keys and their grades for values

student_scores = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Draco': 74,
    'Neville': 62,
    'Manny': 54,
    'Martha': 91,
    'Grace': 99,
    'Molly': 89,
}

# Create an empty dictionary called student_grades.
student_grades = {}

#  Loop Through each item in the Student Scores Dict.
for student in student_scores:

    # Set the variable score to be the value of each of the student score from the dict.
    score = student_scores[student]

    # Check Some Conditions. If they are met, then add an Entry to the student_grades Dict.
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = 'Fail'

# print(student_grades)


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_
# log.


def add_new_country(country_visited, num_of_visits, cities_visited):
    new_country = {'country': country_visited, 'visits': num_of_visits, 'cities': cities_visited}
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country('UK', 5, ['London', 'Manchester', 'Birmingham', 'Leicester', 'Stockport', 'Oldham', 'Salford'])
print(travel_log)
