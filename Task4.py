Mark1=int(input("Enter mark:"))
Mark2=int(input("Enter mark:"))
Mark3=int(input("Enter mark:"))
Mark4=int(input("Enter mark:"))
Mark5=int(input("Enter mark:"))
Mark6=int(input("Enter mark:"))
Margin_Mark=40
Maximum_range=100
#max Mark
if(Mark1>Mark2 and Mark1>Mark3 and Mark1>Mark4 and Mark1>Mark5 and Mark1>Mark6):
    print("The Max Value is:",Mark1)
elif(Mark2>Mark3 and Mark2>Mark4 and Mark2>Mark5 and Mark2>Mark6):
    print("The Max Value is:",Mark2)
elif(Mark3>Mark4 and Mark3>Mark5 and Mark3>Mark6):
    print("The Max Value is:",Mark3)
elif(Mark4>Mark5 and Mark4>Mark6):
    print("The Max Value is:",Mark4)
elif(Mark5>Mark6):
    print("The Max Value is:",Mark5) 
else:
    print("The Max Value is:",Mark6) 

 #Min Mark
if(Mark1<Mark2 and Mark1<Mark3 and Mark1<Mark4 and Mark1<Mark5 and Mark1<Mark6):
    print("The Min Value is:",Mark1)
elif(Mark2<Mark3 and Mark2<Mark4 and Mark2<Mark5 and Mark2<Mark6):
    print("The Min Value is:",Mark2)
elif(Mark3<Mark4 and Mark3<Mark5 and Mark3<Mark6):
    print("The Min Value is:",Mark3) 
elif(Mark4<Mark5 and Mark4<Mark6):
    print("The Min Value is:",Mark4)
elif(Mark5<Mark6):
    print("The Min Value is:",Mark5)
else:
    print("The Min Value is:",Mark6)                            
                         

