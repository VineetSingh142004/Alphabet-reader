from playsound import playsound
d={"a":'A.wav',
   "b":'B.wav',
   "c":'C.wav'
    }
line_org=input("Enter Line :")
line=line_org.lower()
for i in line:
    if i in d :
        playsound(d)
