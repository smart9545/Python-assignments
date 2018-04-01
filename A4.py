def read_classlist(filename):
    try:
        with open(filename,'r') as f:
            content= f.read()
            content_list = content.split("\n")
            student_list = []
            for item in content_list:
                ilist = item.split(',')
                student = '{id}: {name},{email},marks:{l}'.format(id=ilist[1],name=ilist[0],email =ilist[2],l=[])
                student_list.append(student)
            return student_list
        
    except FileNotFoundError:
         print("File out.txt could not be opened")


class_list = read_classlist('classlist.txt')
for s in class_list:
    print(s)
