import webbrowser
lives = int(3)
multi = int(0)
ans = str('nil')
num = 0
while ans == str('nil') or str('y'):
 print('==================================================')
 print('      Welcome to the number learning program!     ')
 print('      This program will help you learn how to')
 print('      do your times tables. Take note that you')
 print('      only have 3 lives. If you get a question')
 print('      wrong, you lose a life. If you lose all ')
 print('      lives, you lose ')
 print('==================================================')
 num = input('What times tables do you want to do? ')
 if int(num) >= 12:
  print('Sorry that is not a times table that I can do :(')
 elif str(num) == str('whatdoesthefoxsay?'):
   webbrowser.open("https://goo.gl/kyQxYN")
 else:
   print('Times table accepted. Loading times table of ', (num))
   while (lives >= int(1) and lives <= int(3) and multi != int(12)) :
      multi = (multi) + int(1)
      resulta = str(multi * num)
      resultb = input(str(num)+' X '+str(multi)+ ' = ')
      print(str(resulta)
      print((resultb)
      print(multi)
      print(num)
      if resulta == resultb:  
        print('Correct!')
      elif resulta != resultb:
       lives = (lives) - 1
       print('You lost one life!  You only have '+  str(lives) + ' lives left!')
      
if (lives == 0):
  print('Game Over :( You lost all lives')
  ans = str(input('Do you want to play again? (y,n) '))

if (lives != 0):
  print('Congrats!!! You did the '+str(num)+' times tables!!!')
  ans = str(input('Do you want to play again? (y,n) '))
