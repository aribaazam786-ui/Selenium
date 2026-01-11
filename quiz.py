satisfied_count=0
neutral_count=0
dissatisfied_count=0
for ratings in range(1, 11):
        ratings = input('enter rating of customers from (1-5): ')
        if ratings == '4'or ratings == '5':
            satisfied_count = satisfied_count + 1
        elif ratings == '3':
            neutral_count = neutral_count + 1
        else:
            dissatisfied_count = dissatisfied_count + 1
print('count of Satisfied customer',satisfied_count)
print('count of Neutral customer',neutral_count)
print('count of dissatisfied customer',dissatisfied_count)