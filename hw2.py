sample_dict = {
   "class_a":{ 
      "student":{ 
         "name":"Misha",
         "marks":{ 
            "math":90,
            "history":85
         }
      }
   }
}
print(sample_dict["class_a"]['student']['name'])
print(sample_dict["class_a"]['student']['marks']['history'])
student1 = {'student1':{'name': 'Nazar', 'marks': {'math': 60, 'history': 55}}}
sample_dict["class_a"].update(student1)
print(sample_dict)
class_b = {'class_b': {'student': {'name': 'Teo', 'marks': {'math': 90, 'history': 85}}, 'student1': {'name': 'Max', 'marks': {'math': 60, 'history': 55}}}}
sample_dict.update(class_b)
print(sample_dict)
sample_dict["class_a"]['student']['marks']['phisics'] = 100
sample_dict["class_a"]['student1']['marks']['phisics'] = 90
sample_dict["class_b"]['student']['marks']['phisics'] = 80
sample_dict["class_b"]['student1']['marks']['phisics'] = 70
print(sample_dict)
s = len(sample_dict["class_a"]['student']['marks'])
k = round(sum(sample_dict["class_a"]['student']['marks'].values())/s, 2)
t = round(sum(sample_dict["class_a"]['student1']['marks'].values())/s, 2)
u = round(sum(sample_dict["class_b"]['student']['marks'].values())/s, 2)
l = round(sum(sample_dict["class_b"]['student1']['marks'].values())/s, 2)
print(k, t, u, l)
all_avarage = {sample_dict["class_a"]['student']['name']:k,
               sample_dict["class_a"]['student1']['name']:t,
               sample_dict["class_b"]['student']['name']:u,
               sample_dict["class_b"]['student1']['name']:l}
print(all_avarage)
best_stud = max(all_avarage.values())
print(best_stud)
best_stud = list(all_avarage.keys())[list(all_avarage.values()).index(best_stud)]
print(best_stud)
s = len(sample_dict["class_a"])
r = round((k+t)/s, 2)
g = round((u+l)/s, 2)
print(r, g)
class_avarage ={list(sample_dict)[0]:r, list(sample_dict)[1]:g}
print(class_avarage)
best_class = list(class_avarage.keys())[list(class_avarage.values()).index(max(class_avarage.values()))]
print(best_class)
