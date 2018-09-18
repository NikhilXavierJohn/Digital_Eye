import pyrebase

config={
	"apiKey": "AIzaSyABJKCA7f_o6Nvm3LD_ziHwR_8A0ZAmork",
    "authDomain": "digital-eye-7d626.firebaseapp.com",
    "databaseURL": "https://digital-eye-7d626.firebaseio.com",
    "projectId": "digital-eye-7d626",
    "storageBucket": "digital-eye-7d626.appspot.com",
    "messagingSenderId": "555085346642"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
details = db.child("users").get()
print(details.val())
st=firebase.storage()
st.child("database").download()
