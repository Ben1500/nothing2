import random
import time

names= ['Ben','Bob','Tom','Mike',"John"]
majors=['math','english','russian','history']
# def person_list(people_number):
#     result = []

#     for i in range(people_number):
#         person={
#             'id':i,
#             'name':random.choice(names),
#             'major':random.choice(majors)
#         }
#         result.append(person)
#     return result
def person_generator(person_number):
    for i in range(person_number):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        yield person

time1=time.time()
people_list = person_generator(1000000)
time2=time.time()
print(time2-time1)
