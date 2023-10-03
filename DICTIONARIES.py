music = {
    'vocals': 'Plant',
    'Guitar': 'Page'        # we can use this method for dictinary concept 
}
 

music1 = dict(voclas='Plant', Guitar='Page')      # USE KEYWORD "dict" for the dictionary concept 
print(music1)

# ACCESS ITEMS IN TWO WAYS
print(music1['voclas'])
print(music1.get('Guitar'))

#LIST KEYS - It WILL TELLS WHAT TYPE OF KEYS USING
print(music1.keys())

# CHANGE VALUES FOR KEYS
music1.update({'bass': "BOAT"})
print(music1)

#REMOVE ITEMS FROM THE KEY 
print(music1.pop('bass'))
print(music1)

#DELETE AND CLEAR 
music1.update({'bass': "BOAT"})
print(music1)

del music1['Guitar']
print(music1)
 

#COPY DICTIONARIES 

music1 =music.copy()
print(music)

# NESTED DICTIONARIES 
 
person ={
  'name': 'Kanna',
  'Role': 'Scientist'
 }

person1= {
 'name':'Madu',
 'Role': 'Developer'
}

music={
 'person' : person,
 'person1' : person1
}
print(music)
