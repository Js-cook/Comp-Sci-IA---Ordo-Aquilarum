from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Question, CustomUser
from django.contrib.auth.decorators import permission_required, login_required
import random

# Create your views here.
def index(request):
  if request.user.is_authenticated:
    logged_in = request.user
    actual = CustomUser.objects.get(user = logged_in)
    total = actual.correct + actual.incorrect
    if total < 100:
      title = "Novice"
    elif total in range(100,999):
      title = "Intermediate"
    elif total in range (1000,4999):
      title = "Advanced"
    elif total >= 5000:
      title = "Master"
    if request.user.is_superuser:
      title = "DEV"
    
  else:
    actual = None
    title = None
  
  return render(request, "user_app/index.html", { 'userr': actual, 'title': title })

@login_required
def question(request):
  # type = random.randint(1,2)
  type = 1 
  outcome = ""
  if type == 1:
    objects = []
    possible = []
    for object in Question.objects.all():
      objects.append(object)
    selection = random.choice(objects)
    name = request.user
    usern = CustomUser.objects.get(user=name)
    (usern.previous_question)
    # usern.previous_question = selection
    # usern.save()
    if request.method == "POST":
      # (request.user)
      
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        # usern.save()
        if previous_q.id in range(1,590):
          current_bon_incorrect = usern.first_bon_incor
          usern.first_bon_incor = current_bon_incorrect+1
          ("added to first bon")
          usern.save()
        elif previous_q.id in range(591, 1440):
          current_bon_incorrect = usern.second_bon_incor
          usern.second_bon_incor = current_bon_incorrect +1
          ("added to second bon")
          usern.save()
        elif previous_q.id in range(1441,2980):
          current_bon_incorrect = usern.third_bon_incor
          usern.third_bon_incor = current_bon_incorrect +1
          ("added to third bon")
          usern.save()
        elif previous_q.id in range(2981, 3170):
          current_bon_incorrect = usern.fourth_bon_incor
          usern.fourth_bon_incor = current_bon_incorrect +1
          ("added to fourth bon")
          usern.save()
        elif previous_q.id in range(3171, 3240):
          current_bon_incorrect = usern.fifth_bon_incor
          usern.fifth_bon_incor = current_bon_incorrect +1
          ("added to fifth bon")
          usern.save()
        elif previous_q.id in range(3241,3830):
          current_trist_incorrect = usern.first_tris_incor
          usern.first_tris_incor = current_trist_incorrect + 1
          ("added to first trist")
          usern.save()
        elif previous_q.id in range(3831, 4680):
          current_trist_incorrect = usern.second_tris_incor
          usern.second_tris_incor = current_trist_incorrect + 1
          ("added to second trist")
          usern.save()
        elif previous_q.id in range(4681, 6220):
          current_trist_incorrect = usern.third_tris_incor
          usern.third_tris_incor = current_trist_incorrect + 1
          ("added to third trist")
          usern.save()
        elif previous_q.id in range(6221, 6410):
          current_trist_incorrect = usern.fourth_tris_incor
          usern.fourth_tris_incor = current_trist_incorrect + 1
          ("added to fourth trist")
          usern.save()
        else:
          current_trist_incorrect = usern.fifth_tris_incor
          usern.fifth_tris_incor = current_trist_incorrect + 1
          ("added to fifth trist")
          usern.save()
          
      (request.POST["result"])
    else:
      (f"id: {selection.id}")
      usern.previous_question = selection
      usern.save()
      
    (selection.noun)
    for object in objects:
      if object.noun == selection.noun:
        possible.append(object)
    return render(request, "user_app/question.html", { 'term': selection, 'possible': possible, 'outcome': outcome, 'stats': usern})
  else:
    # name = request.user
    # usern = CustomUser.objects.get(user=name)
    objects = []
    possible = []
    for object in Question.objects.all():
      objects.append(object)
    selection = random.choice(objects)
    name = request.user
    usern = CustomUser.objects.get(user=name)
    # usern.previous_question = selection
    # usern.save()
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        # usern.save()
        if previous_q.id in range(1,590):
          current_bon_incorrect = usern.first_bon_incor
          usern.first_bon_incor = current_bon_incorrect+1
          usern.save()
        elif previous_q.id in range(591, 1440):
          current_bon_incorrect = usern.second_bon_incor
          usern.second_bon_incor = current_bon_incorrect +1
          usern.save()
        elif previous_q.id in range(1441,2980):
          current_bon_incorrect = usern.third_bon_incor
          usern.third_bon_incor = current_bon_incorrect +1
          usern.save()
        elif previous_q.id in range(2981, 3170):
          current_bon_incorrect = usern.fourth_bon_incor
          usern.fourth_bon_incor = current_bon_incorrect +1
          usern.save()
        elif previous_q.id in range(3171, 3240):
          current_bon_incorrect = usern.fifth_bon_incor
          usern.fifth_bon_incor = current_bon_incorrect +1
          usern.save()
        elif previous_q.id in range(3241,3830):
          current_trist_incorrect = usern.first_tris_incor
          usern.first_tris_incor = current_trist_incorrect + 1
          usern.save()
        elif previous_q.id in range(3831, 4680):
          current_trist_incorrect = usern.second_tris_incor
          usern.second_tris_incor = current_trist_incorrect + 1
          usern.save()
        elif previous_q.id in range(4681, 6220):
          current_trist_incorrect = usern.third_tris_incor
          usern.third_tris_incor = current_trist_incorrect + 1
          usern.save()
        elif previous_q.id in range(6221, 6410):
          current_trist_incorrect = usern.fourth_tris_incor
          usern.fourth_tris_incor = current_trist_incorrect + 1
          usern.save()
        else:
          current_trist_incorrect = usern.fifth_tris_incor
          usern.fifth_tris_incor = current_trist_incorrect + 1
          usern.save()
    else:
      usern.previous_question = selection
      usern.save()
    # objects = []
    # for object in Question.objects.all():
    #   objects.append(object)
    # selection = random.choice(objects)
    objects.remove(selection)
    term = selection.noun.split()
    
    incorrect1 = random.choice(objects)
    (incorrect1.id)
    objects.remove(incorrect1)
    incorrect1_l = incorrect1.noun.split()
    while incorrect1.case == selection.case and incorrect1.gender == selection.gender:
      if incorrect1_l[-1] == term[-1]:
        incorrect1 = random.choice(objects)
        objects.remove(incorrect1)
        incorrect1_l = incorrect1.noun.split()

    incorrect2 = random.choice(objects)
    incorrect2_l = incorrect2.noun.split()
    
    while incorrect1.case == incorrect2.case and incorrect1.gender == incorrect2.gender and incorrect1.case == selection.case and incorrect2.case == selection.case and incorrect1.gender == selection.gender and incorrect2.gender == selection.gender:
      if incorrect2_l[-1] == incorrect1_l[-1] or incorrect2_l[-1] == term[-1] or term[-1] == incorrect1_l[-1]:
        continue
      incorrect2 = random.choice(objects)
      incorrect2_l = incorrect2.noun.split()
    # previous.append(term[-1])
    location = random.randint(1,3)
    return render(request, "user_app/adj_question.html", { 'term': term[0], 'outcome': outcome, 'correct': term[-1], 'incorrect1': incorrect1_l[-1], 'incorrect2': incorrect2_l[-1], 'location': location, 'stats': usern})

@login_required
def first(request):
  # type = random.randint(1,2)
  type = 1
  outcome = ""
  objects = []
  possible = []
  adjs = list(range(1,590))
  adjs.extend(range(3241,3830))
  for i in adjs:
    objects.append(Question.objects.get(id=i))
  selection = random.choice(objects)
  name = request.user
  usern = CustomUser.objects.get(user=name)
  if type == 1:
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(1, 590):
          current_bon_incorrect = usern.first_bon_incor
          usern.first_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.first_tris_incor
          usern.first_tris_incor = current_tris_incorrect + 1
          usern.save()
      # (request.POST["result"])
    # (selection.noun)
    for object in objects:
      if object.noun == selection.noun:
        possible.append(object)
    return render(request, "user_app/question.html", { 'term': selection, 'possible': possible, 'outcome': outcome, })
  else:
    objects.remove(selection)
    term = selection.noun.split()
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
        # previous = []
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(1, 590):
          current_bon_incorrect = usern.first_bon_incor
          usern.first_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.first_tris_incor
          usern.first_tris_incor = current_tris_incorrect + 1
          usern.save()
    incorrect1 = random.choice(objects)
    # (incorrect1.id)
    objects.remove(incorrect1)
    incorrect1_l = incorrect1.noun.split()
    while incorrect1.case == selection.case and incorrect1.gender == selection.gender:
      if incorrect1_l[-1] == term[-1]:
        incorrect1 = random.choice(objects)
        objects.remove(incorrect1)
        incorrect1_l = incorrect1.noun.split()

    incorrect2 = random.choice(objects)
    incorrect2_l = incorrect2.noun.split()
    
    while incorrect1.case == incorrect2.case and incorrect1.gender == incorrect2.gender and incorrect1.case == selection.case and incorrect2.case == selection.case and incorrect1.gender == selection.gender and incorrect2.gender == selection.gender:
      if incorrect2_l[-1] == incorrect1_l[-1] or incorrect2_l[-1] == term[-1] or term[-1] == incorrect1_l[-1]:
        continue
      incorrect2 = random.choice(objects)
      incorrect2_l = incorrect2.noun.split()
    # previous.append(term[-1])
    location = random.randint(1,3)
    return render(request, "user_app/adj_question.html", { 'term': term[0], 'outcome': outcome, 'correct': term[-1], 'incorrect1': incorrect1_l[-1], 'incorrect2': incorrect2_l[-1], 'location': location })

@login_required
def second(request):
  type = random.randint(1,2)
  outcome = ""
  # global previous
  if type == 1:
    objects = []
    possible = []
    adjs = list(range(591, 1440))
    adjs.extend(range(3831, 4680))
    for i in adjs:
      objects.append(Question.objects.get(id=i))
    selection = random.choice(objects)
    name = request.user
    usern = CustomUser.objects.get(user=name)
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
        # previous = []
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(591, 1440):
          current_bon_incorrect = usern.second_bon_incor
          usern.second_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.second_tris_incor
          usern.second_tris_incor = current_tris_incorrect + 1
          usern.save()
        
      # (request.POST["result"])
    # previous.append(selection)
    # (selection.noun)
    for object in objects:
      if object.noun == selection.noun:
        possible.append(object)
    # term = Question.objects.get(id=1)
    # (len(Question.objects.all()))
    return render(request, "user_app/question.html", { 'term': selection, 'possible': possible, 'outcome': outcome, })
  else:
    objects = []
    adjs = list(range(591, 1440))
    adjs.extend(range(3831, 4680))
    for i in adjs:
      objects.append(Question.objects.get(id=i))
    selection = random.choice(objects)
    objects.remove(selection)
    term = selection.noun.split()
    name = request.user
    usern = CustomUser.objects.get(user=name)
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
        # previous = []
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(591, 1440):
          current_bon_incorrect = usern.second_bon_incor
          usern.second_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.second_tris_incor
          usern.second_tris_incor = current_tris_incorrect + 1
          usern.save()
    
    incorrect1 = random.choice(objects)
    # (incorrect1.id)
    objects.remove(incorrect1)
    incorrect1_l = incorrect1.noun.split()
    while incorrect1.case == selection.case and incorrect1.gender == selection.gender:
      if incorrect1_l[-1] == term[-1]:
        incorrect1 = random.choice(objects)
        objects.remove(incorrect1)
        incorrect1_l = incorrect1.noun.split()

    incorrect2 = random.choice(objects)
    incorrect2_l = incorrect2.noun.split()
    
    while incorrect1.case == incorrect2.case and incorrect1.gender == incorrect2.gender and incorrect1.case == selection.case and incorrect2.case == selection.case and incorrect1.gender == selection.gender and incorrect2.gender == selection.gender:
      if incorrect2_l[-1] == incorrect1_l[-1] or incorrect2_l[-1] == term[-1] or term[-1] == incorrect1_l[-1]:
        continue
      incorrect2 = random.choice(objects)
      incorrect2_l = incorrect2.noun.split()
    # previous.append(term[-1])
    location = random.randint(1,3)
    return render(request, "user_app/adj_question.html", { 'term': term[0], 'outcome': outcome, 'correct': term[-1], 'incorrect1': incorrect1_l[-1], 'incorrect2': incorrect2_l[-1], 'location': location })

@login_required
def third(request):
  type = random.randint(1,2)
  outcome = ""
  # global previous
  if type == 1:
    objects = []
    possible = []
    adjs = list(range(1441,2980))
    adjs.extend(range(4681, 6220))
    for i in adjs:
      objects.append(Question.objects.get(id=i))
    selection = random.choice(objects)
    name = request.user
    usern = CustomUser.objects.get(user=name)
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.save()
        # previous = []
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(1441, 2980):
          current_bon_incorrect = usern.third_bon_incor
          usern.third_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.third_tris_incor
          usern.third_tris_incor = current_tris_incorrect + 1
          usern.save()
      # (request.POST["result"])
    # (selection.noun)
    for object in objects:
      if object.noun == selection.noun:
        possible.append(object)
    return render(request, "user_app/question.html", { 'term': selection, 'possible': possible, 'outcome': outcome, })
  else:
    objects = []
    # for i in range(1441, 2980):
    adjs = list(range(1441,2980))
    adjs.extend(range(4681, 6220))
    for i in adjs:
      objects.append(Question.objects.get(id=i))
    selection = random.choice(objects)
    objects.remove(selection)
    term = selection.noun.split()
    name = request.user
    usern = CustomUser.objects.get(user=name)
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
        # previous = []
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(1441, 2980):
          current_bon_incorrect = usern.third_bon_incor
          usern.third_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.third_tris_incor
          usern.third_tris_incor = current_tris_incorrect + 1
          usern.save()
    
    incorrect1 = random.choice(objects)
    (incorrect1.id)
    objects.remove(incorrect1)
    incorrect1_l = incorrect1.noun.split()
    while incorrect1.case == selection.case and incorrect1.gender == selection.gender:
      if incorrect1_l[-1] == term[-1]:
        incorrect1 = random.choice(objects)
        objects.remove(incorrect1)
        incorrect1_l = incorrect1.noun.split()

    incorrect2 = random.choice(objects)
    incorrect2_l = incorrect2.noun.split()
    
    while incorrect1.case == incorrect2.case and incorrect1.gender == incorrect2.gender and incorrect1.case == selection.case and incorrect2.case == selection.case and incorrect1.gender == selection.gender and incorrect2.gender == selection.gender:
      if incorrect2_l[-1] == incorrect1_l[-1] or incorrect2_l[-1] == term[-1] or term[-1] == incorrect1_l[-1]:
        continue
      incorrect2 = random.choice(objects)
      incorrect2_l = incorrect2.noun.split()
    # previous.append(term[-1])
    location = random.randint(1,3)
    return render(request, "user_app/adj_question.html", { 'term': term[0], 'outcome': outcome, 'correct': term[-1], 'incorrect1': incorrect1_l[-1], 'incorrect2': incorrect2_l[-1], 'location': location })

@login_required
def fourth(request):
  type = random.randint(1,2)
  outcome = ""
  if type == 1:
    objects = []
    possible = []
    # for object in Question.objects.all():
    #   objects.append(object)
    adjs = list(range(2981, 3170))
    adjs.extend(range(6221, 6410))
    for i in adjs:
      objects.append(Question.objects.get(id=i))
    selection = random.choice(objects)
    name = request.user
    usern = CustomUser.objects.get(user=name)
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
        # previous = []
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(2981, 3170):
          current_bon_incorrect = usern.fourth_bon_incor
          usern.fourth_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.fourth_tris_incor
          usern.fourth_tris_incor = current_tris_incorrect + 1
          usern.save()
      (request.POST["result"])
    # previous.append(selection)
    (selection.noun)
    for object in objects:
      if object.noun == selection.noun:
        possible.append(object)
    # term = Question.objects.get(id=1)
    # (len(Question.objects.all()))
    return render(request, "user_app/question.html", { 'term': selection, 'possible': possible, 'outcome': outcome, })
  else:
    objects = []
    # for i in range(2981, 3170):
    adjs = list(range(2981, 3170))
    adjs.extend(range(6221, 6410))
    for i in adjs:
      objects.append(Question.objects.get(id=i))
    selection = random.choice(objects)
    name = request.user
    usern = CustomUser.objects.get(user=name)
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
        # previous = []
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(2981, 3170):
          current_bon_incorrect = usern.third_bon_incor
          usern.third_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.third_tris_incor
          usern.third_tris_incor = current_tris_incorrect + 1
          usern.save()
    objects.remove(selection)
    term = selection.noun.split()
    
    incorrect1 = random.choice(objects)
    (incorrect1.id)
    objects.remove(incorrect1)
    incorrect1_l = incorrect1.noun.split()
    while incorrect1.case == selection.case and incorrect1.gender == selection.gender:
      if incorrect1_l[-1] == term[-1]:
        incorrect1 = random.choice(objects)
        objects.remove(incorrect1)
        incorrect1_l = incorrect1.noun.split()

    incorrect2 = random.choice(objects)
    incorrect2_l = incorrect2.noun.split()
    
    while incorrect1.case == incorrect2.case and incorrect1.gender == incorrect2.gender and incorrect1.case == selection.case and incorrect2.case == selection.case and incorrect1.gender == selection.gender and incorrect2.gender == selection.gender:
      if incorrect2_l[-1] == incorrect1_l[-1] or incorrect2_l[-1] == term[-1] or term[-1] == incorrect1_l[-1]:
        continue
      incorrect2 = random.choice(objects)
      incorrect2_l = incorrect2.noun.split()
    # previous.append(term[-1])
    location = random.randint(1,3)
    return render(request, "user_app/adj_question.html", { 'term': term[0], 'outcome': outcome, 'correct': term[-1], 'incorrect1': incorrect1_l[-1], 'incorrect2': incorrect2_l[-1], 'location': location })

@login_required
def fifth(request):
  type = random.randint(1,2)
  outcome = ""
  # global previous
  if type == 1:
    objects = []
    possible = []
    adjs = list(range(3171, 3240))
    adjs.extend(range(6411, 6480))
    for i in adjs:
      objects.append(Question.objects.get(id=i))
    selection = random.choice(objects)
    name = request.user
    usern = CustomUser.objects.get(user=name)
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
        # previous = []
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(3171, 3240):
          current_bon_incorrect = usern.fifth_bon_incor
          usern.fifth_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.fifth_tris_incor
          usern.fifth_tris_incor = current_tris_incorrect + 1
          usern.save()
      (request.POST["result"])
    
    # previous.append(selection)
    (selection.noun)
    for object in objects:
      if object.noun == selection.noun:
        possible.append(object)
    # term = Question.objects.get(id=1)
    # (len(Question.objects.all()))
    return render(request, "user_app/question.html", { 'term': selection, 'possible': possible, 'outcome': outcome, })
  else:
    objects = []
    adjs = list(range(3171, 3240))
    adjs.extend(range(6411, 6480))
    for i in adjs:
      objects.append(Question.objects.get(id=i))
    selection = random.choice(objects)
    name = request.user
    usern = CustomUser.objects.get(user=name)
    if request.method == "POST":
      if request.POST["result"] == "correct":
        outcome = "correct"
        current_correct = usern.correct
        usern.correct = current_correct + 1
        usern.save()
        # previous = []
      else:
        outcome = "incorrect"
        previous_q = usern.previous_question
        current_incorrect = usern.incorrect
        usern.incorrect = current_incorrect + 1
        usern.previous_question = selection
        usern.save()
        if previous_q.id in range(3171, 3240):
          current_bon_incorrect = usern.fifth_bon_incor
          usern.fifth_bon_incor = current_bon_incorrect+1
          usern.save()
        else:
          current_tris_incorrect = usern.fifth_tris_incor
          usern.fifth_tris_incor = current_tris_incorrect + 1
          usern.save()
    
    objects.remove(selection)
    term = selection.noun.split()
    
    incorrect1 = random.choice(objects)
    (incorrect1.id)
    objects.remove(incorrect1)
    incorrect1_l = incorrect1.noun.split()
    while incorrect1.case == selection.case and incorrect1.gender == selection.gender:
      if incorrect1_l[-1] == term[-1]:
        incorrect1 = random.choice(objects)
        objects.remove(incorrect1)
        incorrect1_l = incorrect1.noun.split()

    incorrect2 = random.choice(objects)
    incorrect2_l = incorrect2.noun.split()
    
    while incorrect1.case == incorrect2.case and incorrect1.gender == incorrect2.gender and incorrect1.case == selection.case and incorrect2.case == selection.case and incorrect1.gender == selection.gender and incorrect2.gender == selection.gender:
      if incorrect2_l[-1] == incorrect1_l[-1] or incorrect2_l[-1] == term[-1] or term[-1] == incorrect1_l[-1]:
        continue
      incorrect2 = random.choice(objects)
      incorrect2_l = incorrect2.noun.split()
    # previous.append(term[-1])
    location = random.randint(1,3)
    return render(request, "user_app/adj_question.html", { 'term': term[0], 'outcome': outcome, 'correct': term[-1], 'incorrect1': incorrect1_l[-1], 'incorrect2': incorrect2_l[-1], 'location': location })

def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password1"]
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect("index")
  else:
    form = UserCreationForm()
  context = {"form": form}
  return render(request, "registration/register.html", context)

def notes(request):
  return render(request, "user_app/notes.html")

def logout_request(request):
  logout(request)
  return redirect("index")

@permission_required("user_app.check_students")
def student_stats(request):
  all = []
  totals = []
  first_bon_incorrect = 0
  second_bon_incorrect = 0
  third_bon_incorrect = 0
  fourth_bon_incorrect = 0
  fifth_bon_incorrect = 0

  first_tri_incorrect = 0
  second_tri_incorrect = 0
  third_tri_incorrect = 0
  fourth_tri_incorrect = 0
  fifth_tri_incorrect = 0
  for user in CustomUser.objects.all():
    all.append(user)
    first_bon_incorrect += user.first_bon_incor
    second_bon_incorrect += user.second_bon_incor
    third_bon_incorrect += user.third_bon_incor 
    fourth_bon_incorrect += user.fourth_bon_incor 
    fifth_bon_incorrect += user.fifth_bon_incor 
  
    first_tri_incorrect += user.first_tris_incor 
    second_tri_incorrect += user.second_tris_incor 
    third_tri_incorrect += user.third_tris_incor
    fourth_tri_incorrect += user.fourth_tris_incor 
    fifth_tri_incorrect += user.fifth_tris_incor

  totals.append(second_bon_incorrect)
  totals.append(third_bon_incorrect)
  totals.append(fourth_bon_incorrect)
  totals.append(fifth_bon_incorrect)
  totals.append(first_tri_incorrect)
  totals.append(second_tri_incorrect)
  totals.append(third_tri_incorrect)
  totals.append(fourth_tri_incorrect)
  totals.append(fifth_tri_incorrect)

  greatest = max(totals)
  ind = totals.index(greatest)
  if ind == 0:
    struggle = "First declension nouns with first/second declension adjectives"
    total_incor = first_bon_incorrect
  elif ind == 1:
    struggle = "Second declension nouns with first/second declension adjectives"
    total_incor = second_bon_incorrect
  elif ind == 2:
    struggle = "Third declension nouns with first/second declension adjectives"
    total_incor = third_bon_incorrect
  elif ind == 3:
    struggle = "Fourth declension nouns with first/second declension adjectives"
    total_incor = fourth_bon_incorrect
  elif ind == 4:
    struggle = "Fifth declension nouns with first/second declension adjectives"
    total_incor = fifth_bon_incorrect
  elif ind == 5:
    struggle = "First declension nouns with third declension adjectives"
    total_incor = first_tri_incorrect
  elif ind == 6:
    struggle = "Second declension nouns with third declension adjectives"
    total_incor = second_tri_incorrect
  elif ind == 7:
    struggle = "Third declension nouns with third declension adjectives"
    total_incor = third_tri_incorrect
  elif ind == 8:
    struggle = "Fourth declension nouns with third declension adjectives"
    total_incor = fourth_tri_incorrect
  elif ind == 9:
    struggle = "Fifth declension nouns with third declension adjectives"
    total_incor = fifth_tri_incorrect
    
  return render(request, "user_app/student_stats.html", { 'users': all, 'range': range(0, len(all)), 'struggle': struggle, 'total_incorrect': total_incor, 'first_bon': first_bon_incorrect, 'second_bon': second_bon_incorrect, 'third_bon': third_bon_incorrect, 'fourth_bon': fourth_bon_incorrect, 'fifth_bon': fifth_bon_incorrect, 'first_tris': first_tri_incorrect, 'second_tris': second_tri_incorrect, 'third_tris': third_tri_incorrect, 'fourth_tris': fourth_tri_incorrect, 'fifth_tris': fifth_tri_incorrect })

@login_required
def awards(request):
  return render(request, "user_app/awards.html")