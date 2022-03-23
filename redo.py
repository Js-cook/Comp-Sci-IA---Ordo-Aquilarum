import csv
from user_app.models import Question

def create():
  with open("additions.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    for row in csv_reader:
      question = Question(noun=row[0], case=row[1], number=row[2], gender=row[3])
      question.save()