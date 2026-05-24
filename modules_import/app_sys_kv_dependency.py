from .KV_Files.Main_KV import Main_KV
from .KV_Files.Student_Screen_KV import Student_Screen
from .KV_Files.Past_Student_KV import Past_Student_Screen
from .KV_Files.Teacher_Screen_KV import Teacher_Screen
from .KV_Files.Past_Teacher_Screen_KV import Past_Teacher_Screen
from .KV_Files.Course_Screen_KV import Course_Screen
from .KV_Files.Grade_Screen_KV import Grade_Screen

KV_Routes = [
    Main_KV,
    Student_Screen,
    Past_Student_Screen,
    Teacher_Screen,
    Past_Teacher_Screen,
    Course_Screen,
    Grade_Screen
]

kv_holder = ''' '''

for routes in KV_Routes:
    kv_holder += routes

kv = kv_holder



