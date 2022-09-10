print ("     HI WELCOME TO KIDNESS CHRISTIAN CENTER KCC ❤")
print ( "              Please input your name" )
Full_name = input ("Fullname: " )
print ("Welcome " +  Full_name)
print ("YOUR SPIRITAUL WELFARE IS OUR CONCERN ")
print ("         We have Three services a week")
print("1. Sunday Worship Service: 8am(07:00 GMT)")
print ("2. Monday Bible Study: 6pm(18:00GMT)")
print ("3. Thursday Revival And Evagelical Service 6pm(18:00GMT)")

print ()
print ("Thanks for contacting KCC how can we be of help to you: ")
print("Press 1, To know more about us")
print("Press 2, To fill visitors slip")
print("Press 3, To contact us")
command = ""
while True:
    command = input ("> ").lower()
    if command == "1":
        print ("We are a Bible believing Church under the DEEPER LIFE BIBLE CHURCH. We are located at 13 Ikota Shopping Complex Near VGC Ajah  ")
        print ("We nuture Teens and Children in the right way of God ")
        print ("            JESUS ONLY IS OUR MESSAGE  🎤 📄 ")
        print ()
        print (" Beloved, when I gave all diligence to write unto you of the common salvation, it was needful for me to write unto you, and exhort you that ye should earnestly contend for the faith which was once delivered unto the saints: JUDE 1:3 ")
        print () 
        print ("PRESS 4: To go back to the MAIN MENU ")
        print ("Press 5: If you want to QUIT ")
    elif command == "2":
        num1 = input ("Enter full name; ")
        num2 = input ("Enter Age: ")
        num4 = input ("Home Address: ")
        num5 = input ("Sex: Male or Female: ")
        num6 = input ("Phone number: ")
        num7 = input ("Whatsapp number: ")
        num8 = input("State of origin: ")
        num9 = input("Preffered language: ")
        ans = input ("Please confirm your consent to use your personal data to contact you for the purpose of helping you further in your new faith: (yes/no) ")
        if ans.lower() == "yes":
            print("Thanks")
        else:
               print ("Incorrect")
               break
               
               
        print ("NAME:" + num1)
        print ("AGE: " + num2 )
        print ("HOME ADDRESS: " + num4)
        print("SEX: " + num5)
        print ("PHONE NUMBER: " + num6)
        print ("WHATSAPP NUMBER: " + num7)
        print ("STATE OF ORIGIN: " + num8)
        print ("PREFFERED LANGUAGE: " + num9)
        print ("Thanks for filling the form")
        print ("PRESS 4: To go back to the MAIN MENU")
        print ("Press 5: If you want to QUIT")
      
       
         
        
    elif command == "3":
        print ( "You can contact us  ")
        print (" Website: www.kcc.org ")
        print ("Telephone: +2348150777776")
        print (" Email: kcc@gmail.com ")
        print ("PRESS 4: To go to the MAIN MENU")
        print ("PRESS 5: If you want to QUIT ")
    elif command == "4":
        print ("YOUR SPIRITAUL WELFARE IS OUR CONCERN ")
        print ("         We have Three services a week")
        print("1. Sunday Worship Service: 8am(07:00 GMT)")
        print ("2. Monday Bible Study: 6pm(18:00GMT)")
        print ("3. Thursday Evangelical and Training Service (18:00GMT) ")
        print ()
        print ("Thanks for contacting KCC how can we be of help to you: ")
        print("Press 1, To know more about us")
        print("Press 2, To fill visitors slip")
        print("Press 3, To contact us")
    elif command == "5":
        break
    else:
        print ("SORRY I DONT UNDERSTAND ")
        print ("PRESS 4: To go back to the MAIN MENU")
        print ("PRESS 5: If you want to quit")