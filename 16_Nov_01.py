'''
QUESTION SOURCED FROM CODE WARS

Make a program that filters a list of strings 
and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
Otherwise, you can be sure he's not...

EXAMPLE CASE
Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]
'''

Names = ["Ryan","Kieran","Jason","Yours","Rafi","Qiqi","Joy","Marco","Kathy"]

#Create Function 

def My_friend(names):
    my_friends = []
    for placeholder in Names:
        if len(placeholder) == 4:
            my_friends.append(placeholder)
    print(my_friends)

#Call the function 
My_friend(Names)