

# create a function (generalMark) which recieves 3 numbers from a dictionary
def generalMark(average):
    average_mark = (marks["sem_1"] + marks["sem_2"]+ marks["exam"])/3
    marks["average"] = average_mark #adds to the dictionary a new key and value
    return average

marks = {
        "sem_1": 9.0,
        "sem_2": 8.0,
        "exam" : 9.0,    
    }

print(generalMark(marks))

'''
           marks .......{ }
              |         /
              v        /
generalMark(general)  /
              |      /
              v     /
            general/
              |
              v
         average_mark ---> read
              |
              v   
              (marks["sem_1"] + marks["sem_2"]+ marks["exam"])/3  
              |
              V
         marks["average"] = average_mark
              ^
              |
               -------------write - 8.66
'''
