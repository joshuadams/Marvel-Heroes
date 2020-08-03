People ={
  'BAA' : 'John',
  'AAA' : 'Matthew',
  'BBB' : 'Joesph',
  'ABA' : 'Michael'
}
  
quit = 'Y'
while quit == 'Y':
  q1 = input('Do you like Minecraft? \nA) Yes \nB) No \n')
  q2 = input('Favorite Sport? \nA) Soccer \nB) Baseball \n')
  q3 = input('Favorite Movie? \nA) Harry Potter and the Goblet of Fire \nB) Avengers: Endgame \n')
  
  code = q1 + q2 + q3
  if code in People:
   print('You must be  ' + People.get(code))

  quit = input('Do you want to continue? (Y/N)')