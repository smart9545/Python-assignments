def read_solution(filename):
    try:
        with open(filename,'r') as f:
            content= f.read()
            content_list = content.split("\n")
            lab_test=[]
            for item in content_list:
                lab = item[0:4]
                result =item[5:]
                result = result.split(',')
                solution = '{l}: answer: {ls}'.format(l=lab,ls=result)
                lab_test.append(solution)
            return lab_test
        
    except FileNotFoundError:
         print("File out.txt could not be opened")


lab_list = read_solution('solution.txt')
for lab in lab_list:
    print(lab)
