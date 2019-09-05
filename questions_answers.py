questions= open('questions.txt' , 'r')
questions_list = [line.strip() for line in questions.readlines()]
questions.close()

score = 0
total = len(questions_list)
for line in questions_list:
    q,a = line.split('=')
    ans = input('{}='.format(q))
    if a== ans:
        score+=1
result = open('answers.txt','w')
result.write('your final score is {} / {}'.format(score,total))
result.close()


