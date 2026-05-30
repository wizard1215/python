"""information= {
    "name": "Ritik:",
    "course": "B.TECH",
    "Roll no": 2204980100046,
    "mobile_no":9759858503,
    "is_adult": True,
    "Price": 25.2,
    "job":None
}
information["name"]="RAVI"
print(information)
information["mob_no"]=7457895709
print(information)
"""

"""library={
    "name":"Ritik",
    "mobile_no.":9759858503,
    "gmail":"ritikupadhyay814@gmail.com",
    "seat_no.":36,
    "is_adult":True,
    "Date_addmission":7.5/2025,
    "next_seat":37,
    "learning":"python"
}
print(library)
library["name"]="Kunal sharma"
print(library)
library["mobile_no."]=7457895709
print(library)
print(type(library))"""

"""college ={
   "name":("Ritik_upadhay","tushar_mittal","Aakash_gupta","umesh_kumar","reshu_thakur"),
    "course":"B.tech",
    "branch":"computer_science",
    "knowledege":"fresher",
    "fees":30000,
}
print(college)
college["name"]="abhishek_khatana"
print(college)"""


#nested condition in dict:
"""college={
    "name":"Ritik_upadhyay",
    "subject_score":
    {
        "physics":67,
        "chemistry":56,
        "math":78,
        "data_structure":43
    }
}
print(college)"""

"""school = {
    "students_name":"Ritik_upadhyay",
    "data_students":{
    
        "course":"B.tech",
        "Branch":"computer_science",
        "mobile_no.":9759858503,
        "gmail_id":"ritikupadhyay814@gmail.com",
        "subject_students":{
            "subj1":"physics",
            "subj2":"math",
            "subj3":"python",
            "subj4":"chemistry",
            "subj5":"soft skiil",
            "subject_score":{
                "python":78,
                "chemistry":56,
                "soft skill":76,
                "math":45,
                "physics":67,
            }
    
    }   
        }
    

}
print(type(school))
school["name"]="Rahul_kumar"
print(school)
school["branch"]="machenical"
print(school)"""
    


"""college={
    "name": "DIET",
    "students": "ritik_upadhyay",
    "students_privacy":{
        "mobile": "9759858503",
        "email_id" :"ritikupadhyay@gmail.com",
        "branch":"computer_science",
        "subjects":{
            "subj1":"python",
            "subj2":"java",
            "sub3":"c langage",
            "sub4":"soft skill",
            "sub5":"coa",
            "subject_score":{
                "python": 68,
                "java": 56,
                "c lanuage": 53,
                "coa": 74,
                "soft skill": 64
            }
        }
    }
}
print(college)"""

"""students={
    "name":"Ritik_upadhyay",
    "marks":96
}
students["marks"]=70
students["name"]="ravi_upadhyay"
if students ["marks"]>=90:
    if students ["marks"]<=100:
        print(students["name"],"topper")
elif students["marks"]>=60:
    if students["marks"]<90:
        print(students["name"]," =  GOOD")
elif students ["marks"]>=33:
    print(students["name"]," = pass")
else:
    print(students["name"],"fail")

print(students)
print(type(students))"""


"""college={
    " COLLEGE_Name":"DIET MEERUT",
    "course":"B.tech",
    "students":{
        "names":["Ritik","tushar mittal","reshu soam","ajay..."],
        "college_fees":{
            "Ritik":"29000 P/A",
            "tushar mittal":"35000 P/A",
            "reshu soam":"35000 P/A",
            "ajay":"40000 P/A"
        }

    }
    
}
print(college)"""

"""empty_set=set()
print(type(empty_set))"""


"""from functools import reduce
nums=[12,3,4,50,75]
print(reduce(lambda a,b: a if a>b  else b, nums))"""



# what happen in this following code:
"""car={"brand":"Toyota.."}
car["colour"]="Red.."
print(car)"""

# find the output of this code:
"""data={"a":1,"b":2}
print(data.get("d",0))""" # by default =0:



"""college={
    "college_name":"DIET",
    "Address":"Meeerut Ghat Mode",
    "Courses":{
        "cousre1":"B.tech",
        "course2":"polytechic",
        "cousre3":"BCA",
        "course4":"BBA",
        "students":{
            "students_name":"Ritik_upadhyay",
            "students_privacey":{
                "course":"B.tech",
                "Branch":"CS/IT",
                "address":"village shafipur Town Budhana Dist muzaffarnagar",
                "mob_no":9759858503

            }
        }
    }
}
college["Courses"]["students"]["students_name"]="Ravi upadhyay"
print(college.get("Courses").get("students").get("students_privacey").get("mob_no"))"""


'''students={

    "college_name":"diet",
    "courses":  {
        "course 1":"B.tech",
        "course 2":"B_CA",
        "course 3": "BBA",
        "course 4": "Polyetchnic",
        "Students_course":"B.tech",
        "students_Information":  {
            "students_name":"Ritik_upadhyay",
            "Stu_id" : 251309,
         "Students_Mob_NO.":"9759858503",
         "students_sub":{
             "sub1":"Python",
             "sub2":"JAVA",
             "sub3":"C language",
             "sub4":"Physics",
             "sub5":"Chemistry"
         }
    
        }
    
    }


}
students["courses"]["students_Information"]["students_name"]="Ravi_upadhyay"
print(students)'''

# Use dict comprehension to create a dict mapping names to salaries > 70,000 only.
"""employees = [
    {'name': 'Alice', 'salary': 75000},
    {'name': 'Bob', 'salary': 95000}, 
    {'name': 'Charlie', 'salary': 65000}
]

high_earners={emp["name"]:emp["salary"] for emp in employees if emp["salary"]>70000}
print(high_earners)"""