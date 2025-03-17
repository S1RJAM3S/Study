import pickle
from shutil import copyfile
copyfile('student_info.pkl', 'updated_info.pkl')
def add_student_info(new_student):
    if 'id' not in new_student:
        return
    
    try:
        with open('updated_info.pkl', 'rb') as f:
            student_info = pickle.load(f)
        f.close()
    except:
        student_info = []
    found = False
    
    for i, student in enumerate(student_info):
        if (student['id'] == new_student['id']):
            student_info[i] = new_student
            found = True
            break
    if not found:
        student_info.append(new_student)
    with open('updated_info.pkl', 'wb') as f:
        pickle.dump(student_info, f)