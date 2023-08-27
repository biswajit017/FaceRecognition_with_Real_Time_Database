import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendance-realtime-df344-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
    {
     
     "name":"Murtaz Hassan",
     "major" :"Robotics",
     "starting_year":2017,
     "total_attendance": 6,
     "standing":"G",
     "year":4,
     "last_attendance_time":"May 28, 2023  00:54:34"
    },
    "852741":
    {
     
     "name":"Emly Blunt",
     "major" :"Artificial Inteligence",
     "starting_year":2018,
     "total_attendance": 10,
     "standing":"E",
     "year":4,
     "last_attendance_time":"May 28, 2023  00:54:34"
    },
    "963852":
    {
     
     "name":"Elon Musk",
     "major" :"Machine Learning",
     "starting_year":2019,
     "total_attendance": 12,
     "standing":"M",
     "year":4,
     "last_attendance_time":"May 28, 2023  00:54:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)