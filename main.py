import os
import time


while True:
  print("REPORT BUILDER v1.0")
  print()
  print("Would you like to write a report or veiw one?")
  choice = input("[enter 'w' to write a report, and 'v' to veiw one]: ")

  if choice == "w":
    print("Enter the name of the student")
    name = input("[enter the name here]: ")
    print()
    print("Enter the topic")
    topic = input("[enter here]: ")
    print()
    print("Enter the topic test percentage (without the percentage sign)")
    score = input("[enter the score here]: ")
    print()
    print("Enter the students ATL")
    atl = input("[enter the number here]: ")
    print()
    print("Enter what the student did well")
    didWell = input("[enter here]: ")
    print()
    print("Enter what the student can improve on")
    improve = input("[enter here]: ")
    print()
    os.system('clear')
    print("REPORT:")
    report = (f'''
  |  Name: {name}
  |  Topic: {topic}    Test Result: {score}%
  |
  |  ATL: {atl}
  |
  |
  |  What {name} did well:
  |  {didWell}
  |
  |
  |  What {name} could improve:
  |  {improve}
    ''')
    print(report)
    print()
    file = open(f"Reports/{topic.upper()} - {name.lower()}", "w")
    file.write(report)
    file.close()
    input("[press enter to continue]")
    os.system('clear')
  elif choice == "v":
    print("Enter the name of the student")
    name = input("[enter the name here]: ").lower()
    print()
    print("Enter the subject the report was on.")
    subject = input("[enter the subject here]: ").upper()
    print()
    try:
      file = open(f"Reports/{subject} - {name}", "r")
      report = file.read()
      file.close()
      os.system('clear')
      print("Report:")
      print(report)
      input("[press enter to continue]")
      os.system('clear')
    except:
      print("You have not made a report for this student in this subject yet!")
      print()
      input("[press enter to continue]")
      os.system('clear')
    