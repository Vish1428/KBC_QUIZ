# This is  Python script is for like KBC QUIZ. It is just for Fun
# Create List for Questions
questions = [
    ['Who won the first ever World Cup?', "India", "West Indies", "South Africa", "Australia", 1],
    ['Who is the current Captain of the Indian Cricket Team?', "Virat Kohli", "Rohit Sharma", "MS Dhoni", "Rishabh", 1],
    ['Which is Samsung\'s latest mobile?', "Samsung Galaxy S22", "Samsung Galaxy S23", "Samsung Galaxy S24",
     "Samsung Galaxy S25", 2],
    ['Which is the first car to break the speed barrier?', "supersonic car", "Tesla", "Nissan", 'Toyota', 0],
    ['The International Literacy Day is observed on', "Sep 8", "Nov 28", "May 2", "Sep 22", 0],
    ['The language of Lakshadweep. a Union Territory of India, is', 'Tamil', 'Hindi', 'Malayalam', 'Telugu', 2],
    ['In which group of places the Kumbha Mela is held every twelve years?', 'Ujjain. Purl; Prayag. Haridwar',
     'Prayag. Haridwar, Ujjain,. Nasik', 'Rameshwaram. Purl, Badrinath. Dwarika', 'Chittakoot, Ujjain, Prayag,Haridwar',
     1],
    ['Bahubali festival is related to', 'Islam', 'Hinduism', 'Buddhism', 'Jainism', 3],
    ["Which day is observed as the World Standards  Day?", 'June 26', 'Oct 14', 'Nov 15', 'Dec 2', 1],
    ['Which of the following was the theme of the World Red Cross and Red Crescent Day?',
     'Dignity for all - focus on women', 'Dignity for all - focus on Children', 'Focus on health for all',
     'Nourishment for all-focus on children', 1],
    ['Spetmber 27 is celebrated every year as', 'Teachers Day', 'National Integration Day', 'World Tourism day',
     'International Literacy Day', 2],
    ["Who is Author of 'Manas Ka-Hans'?", 'Khushwant Singh', 'Prem Chand', 'Jayashankar Prasad', 'Amrit Lal Nagar', 3],
    ["The death anniversary of which of the following leaders is observed as Martyrs' Day?", 'Smt. Indira Gandhi',
     'PI. Jawaharlal Nehru', 'Mahatma Gandhi', 'Lal Bahadur Shastri', 2],
]
# Create List for cash price
price = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 5000000, 10000000]
money = 0   # Firstly your money will be 0.
for i in range(0, len(questions)):      # For loop for asking questions
    question = questions[i]
    print(f"Question for Rs. {price[i]} is {question[:-1]}")
    print(f"0.{question[1]}")
    print(f"1.{question[2]}")
    print(f"2.{question[3]}")
    print(f"3.{question[4]}")
    reply = int(input("Enter your answers (0-3): "))
    if reply == question[-1]:
        print(f"Correct answer, you have won Rs. {price[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print(f"Wrong answer!")
        break
print(f"Your Cash Price is {money}")
