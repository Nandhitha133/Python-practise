Mark1=int(input("Enter Num:"))
Mark2=int(input("Enter Num:"))
Mark3=int(input("Enter Num:"))
Mark4=int(input("Enter Num:"))
Mark5=int(input("Enter Num:"))
Mark6=int(input("Enter Num:"))
Total_Marks=(Mark1+Mark2+Mark3+Mark4+Mark5+Mark6)
print(Total_Marks)
Margin_Marks=240
Max_Range=600
if(Total_Marks>Margin_Marks):
    print("The Mark is pass")
if(Total_Marks<Max_Range):
    if(Max_Range>Total_Marks and Total_Marks>=550):
        print("You got a o grade ") 
    elif(Max_Range>Total_Marks and Total_Marks>=500):
        print("you got a A grade")
    elif(Max_Range>Total_Marks and Total_Marks>=400):
        print("you got a B grade")
    elif(Max_Range>Total_Marks and Total_Marks>=350):
        print("You got a C grade")  
    else:
        print("You got a Fail")          