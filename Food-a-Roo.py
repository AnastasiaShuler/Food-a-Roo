# Food-a-Roo.py
# V1 Beta; August 7, 2014

import os
from whoosh.fields import Schema, TEXT, KEYWORD
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.filedb.filestore import FileStorage
from whoosh.query import *
from whoosh.qparser import QueryParser

def startUp():
    kangaroo = '''

        WELCOME TO FOOD-A-ROO
                                                 :\ 
                                                'M$H
                                              .sf$$br
                                            .J\J\J$L$L
                                          .:d  )fM$$$$$r
                                      ..P*M .4MJP   '*'
                            .sed"""""".ser d$$$F
                         .M\>x.IJM$$$B$$$$BJ$MR. ...
                        dFPxnMMM$$$R$$$$$$$h"$ks$$"$$r
                      J\.. .MMM8$$$$$LM$P\..'*/    \*/
                     d :d$r "M$$$$br'$M\d$R/
                    J\MM\ *L   *M$B8MM$B.**
                   :fd$>  :fhr 'MRM$$M$$"
                   MJ$>    '5J5.:M8$$>
                  :fMM     d$Fd$$R$$F
                  4M$P .$$*.J*$$**
                  M4$>  '$>dRdF
                  MMM|    *L*B.                 V1 Beta
                 :$$F      ?k"Re                Aug. 7, 2014
           .   .$$P/         **'$$B..
           ^:e$F"               '"""'

               '''

    # Clear the terminal; allows for both windows and unix use
    os.system('cls' if os.name == 'nt' else 'clear')
    print kangaroo
    q = 'Generate Schedule [G], Add Recipe [A], Quit [q]\t\t'
    c = '';
    # Prompt the user for some action
    while c != 'q':
        print 'What would you like to do? Type "HELP" for help'
        c =raw_input(q).lower()
        if c == 'q' or c == 'quit':
            print 'Thanks for using Food-A-Roo. We hope to see you soon! \n\n'
            break
        elif c == 'g' or c == 'generate' or c == 'generate schedule':
            print '\t Generating New \'Rooin Schedule'
            generateSchedule()
        elif c == 'a' or c == 'add' or c == 'add recipe':
            print 'Lets add some new food'
            addRecipe()

        elif c == 'help' or c == 'h':
            print 'Don\'t worry! Helpful \'Roo is on the way!'
            helpfulRoo()
        else:
            print 'I\'m sorry, I don\'t understand what you mean. Try again.'


def generateSchedule():
    while True:
        print 'The current directory is ' + os.getcwd()
        ques = 'Is the FAR index (directory) in the current directory? [y/n]\t'
        c = raw_input(ques).lower()
        if c == 'y' or c == 'yes':
            idxDir = os.getcwd()
            break
        elif c == 'n' or c == 'no':
            while True:
                idxDir = raw_input('Where is it?\t').lower()
                try:
                    os.chdir(idxDir)
                    break
                # Im sure this only works in Windoze                        
                except WindowsError:
                    print 'Sorry, I couldn\'t navigate to that directory'
            break
        elif c == 'q' or c == 'quit':
            print '\tReturning to the Main Menu'
            return
        else:
            print 'I\'m sorry, I don\'t understand what you mean. Try again.'

    # Open the index
    print '\nThe Food \'Roo is gathering your recipes. Please wait paitiently ...'

    idxDir = idxDir + '/FAR_Storage'
    storage = FileStorage(idxDir)
    idx = storage.open_index(indexname = 'FAR')

    result = idx.searcher().documents()
    r = result
    print 'Yay! We\'ve got a whole pouch full of recipies'
    print 'You\'ve got ' + str(len(list(r))) + ' recipies in Food \'Roo\'s pouch\n\n'


    for item in result:
        print 'I can get in here'

        print item
        print item['Name']

def addRecipe():
    '''
    addRecipe()
    Adds a new recipe to the index for use in schedule generation
    '''

    idx = findIndex()
    wrt = idx.writer()
    Q1= 'What would you like to call this recipe? \t'
    name = raw_input(Q1)
    Q2 = 'What ingredients are needed? Be sure to specify quantity and seperate with commas\n\t'
    ingrs = raw_input(Q2)
    wrt.add_document(Name = name.decode(), Ingr = ingrs.decode())
    wrt.commit()

    while True:
        q = 'Would you like to add another? \t'
        c = raw_input(q).lower()
        if c == 'y' or c == 'yes':
            addRecipe()
            break
        elif c == 'n' or c == 'no':
            print '\tReturning to the Main Menu\n\n'
            return 
        elif c == 'q' or c == 'quit':
            # Return to the main menu
            print '\tReturning to the Main Menu\n'
            return 
        else:
            print 'I\'m sorry, I don\'t understand what you mean. Try again.'


def findIndex():
    while True:
        q = 'Do you already have a Recipe Index? [y/n]\t'
        c = raw_input(q).lower()
        if c == 'y' or c == 'yes':
            # Create a new recipe index
            print 'I\'m sory, this feature has not been implemented yet :('
        elif c == 'n' or c == 'no':
            # ask for the existing file
            idx = newIndex()
            break
        elif c == 'q' or c == 'quit':
            # Return to the main menu
            print '\tReturning to the Main Menu\n'
            return 
        else:
            print 'I\'m sorry, I don\'t understand what you mean. Try again.'

    return idx
    
def newIndex():
    '''
    newIndex()
    Creates the index/schema for the Whoosh module
    INPUTS: (none)
    OUTPUTS: idx -- index 
    '''
    print '\tCreating a new Index in the current directory'
    # Create an index to store the artist/title and lyrics
    schm = Schema(Name=TEXT(stored=True), Ingr=KEYWORD(stored=True, commas=True))
    # Create a directory called FAR_Storage; will contain the index
    # See Whoosh documentation for more information
    if not os.path.exists('FAR_Storage'):
        os.mkdir('FAR_Storage')
    idxDir ='FAR_Storage'
    storage = FileStorage(idxDir)
    idx = storage.create_index(schm, indexname='FAR')
    idx = storage.open_index(indexname = 'FAR')
    return idx

def helpfulRoo():
    h = '''
    Welcome to Food-A-Roo. Thanks for joining us.

      Food-A-Roo is a program that allows you to generate weekly or monthly meal
    plans based on pre-saved recipies. Additionally, Food-A-Roo will also
    produce a grocery list, with everything you need to make sure the week 
    goes smoothly.

      Getting started is easy - just type 'add recipie' (or simply 'a') at the 
    start-up screen to begin adding your recipies. Enter a title when prompted,
    then the list of ingredients. It's that simple!

      When you are ready to generate your food schedule, simply enter 'generate
    schedule' at the start-up screen. When prompted, select weekly/monthy, and 
    volia! Your schedule and shopping list will be displayed (and saved to a 
    text file for later viewing).

      Thanks for using Food-A-Roo. More detailed instructions can be found in 
    the FAR_ReadMe.txt file that was included in your download. If you seem to 
    be missing this file, or simply want to go check out the project, you can
    find it at:
            https://github.com/AnastasiaShuler/Food-a-Roo

      Thanks and happy 'rooing!


    '''
    print h


if __name__ == "__main__":
    '''
    When run from the command line, runs startUp()
    '''
    startUp()
