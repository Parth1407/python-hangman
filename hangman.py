import random

#--- hangmanwords.txt ---

f=open('hangmanwords.txt','r')
s=f.readlines()
wordlist=[]
for lines in s:
    words=lines.split()
    wordlist+=words
#---------

diagram=[
    """
    - - - - - - - -
     |         |
     |         |
     |                
     |           
     |         
     |        
     |
    ===

    """,
    """
    - - - - - - - -
     |         |
     |         |
     |         O       
     |           
     |         
     |        
     |
    ===

    """,
    """
    - - - - - - - -
     |         |
     |         |
     |         O       
     |         |   
     |         
     |        
     |
    ===

    """,
    """
    - - - - - - - -
     |         |
     |         |
     |         O       
     |        \|  
     |         
     |        
     |
    ===

    """,
    """
    - - - - - - - -
     |         |
     |         |
     |         O       
     |        \|/   
     |         
     |        
     |
    ===

    """,
    """
    - - - - - - - -
     |         |
     |         |
     |         O       
     |        \|/   
     |         |
     |        
     |
    ===

    """,
    """
    - - - - - - - -
     |         |
     |         |
     |         O       
     |        \|/   
     |         |
     |        / 
     |
    ===

    """,
    """
    - - - - - - - -
     |         |
     |         |
     |         O       
     |        \|/   
     |         |
     |        / \\
     |
    ===

    """]
#---------
def playgame(x,y):
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    n=random.randint(0,len(wordlist)-1)
    diagramno=0
    word=wordlist[n]
    word1=''
    for i in word:
        s=i+' '
        word1+=s
    space='_ '*len(word)
    print('\nI am thinking of a',len(word),'letter word')
    print(diagram[diagramno])
    print('\nWord:',space)
    print('\nAvailable letters: ')
    for i in letters:
        print(i,end='')
    print('\n')
    while True:
        choose=input('\nGuess a letter/word: ')
        if len(choose)==1:
            if choose in word:
                print('Good guess!!')
                print(diagram[diagramno])
                for j in range(len(word)):
                    if word[j]==choose:
                        space=space[:j*2]+word[j]+' '+space[(j+1)*2:]
                        if word[j] in letters:
                            letters.remove(word[j])
                if '_' not in space:
                    print(space)
                    print('Congratulations! you guessed the word.')
                    print('You won :)')
                    break
                print(space)
                print('\nAvailable letters: ')
                for i in letters:
                    print(i,end='')
                print('\n')
            else:
                print('Oops wrong guess!')
                diagramno+=1
                print(diagram[diagramno])
                print(space)
                print('\nAvailable letters: ')
                for i in letters:
                    print(i,end='')
                print('\n')
                if diagramno==7:
                    print('Oops wrong guess!!')
                    print('The word was',word)
                    print('You lost :(')
                    break
        elif choose==word:
            print('Congratulations! you guessed the word.')
            print('You won :)')
            break
        else:
            print('Oops wrong guess!')
            diagramno+=1
            print(diagram[diagramno])
            print(space)
            print('\nAvailable letters: ')
            for i in letters:
                print(i,end='')
            print('\n')
            if diagramno!=7:
                print('Oops wrong guess!')
            else:
                print('Oops wrong guess!')
                print('The word was',word)
                print('You lost :(')
                break

#---------
print('~ ~ ~ Welcome to Hangman ~ ~ ~')
playgame(wordlist,diagram)

while True:
    c=input('\nDo you want to play again? (y/n): ')
    if c=='y':
        playgame(wordlist,diagram)
    elif c=='n':
        break
    else:
        print('Invalid input')

