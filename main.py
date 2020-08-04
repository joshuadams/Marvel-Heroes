People ={
  'AAA' : 'John',
  'ABA' : 'Matthew',
  'ABB' : 'Joesph',
}
  
quit = 'Y'
while quit == 'Y':
  q1 = input('Do you like Minecraft? \nA) Yes \nB) No \n')
  q2 = input('Favorite Sport? \nA) Soccer \nB) Baseball \n')
  q3 = input('Favorite Movie? \nA) Harry Potter and the Goblet of Fire \nB) Avengers: Endgame \n')
  
  code = q1 + q2 + q3
  if code in People:
   guess = input('You must be  ' + People.get(code) + ' (Y/N)')
   if guess == 'N':
     who = input('Who is this person? ')
     People[code] = who
  else:
    who = input('Who is this person?')
    People[code] = who
    print('Ok, we added' , who, 'to People')

  quit = input('Do you want to continue? (Y/N)')

for person in People.keys():
  print('\''+ person + '\' : \'' + People.get(person) + '\'')