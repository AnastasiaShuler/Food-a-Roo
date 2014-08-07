# Food-a-Roo.py
# V1 Beta; August 7, 2014

import os

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
    q = 'Generate Schedule [G], Add Recipe [A], Quit [q]\t'
    c = '';
    # Prompt the user for some action
    while c != 'q':
        os.chdir(origDir)   # Change directory back; useful for search
        print 'What would you like to do? Type "HELP" for help'
        c =raw_input(q).lower()
        if c == 'q' or c == 'quit':
            print 'Thanks for \'Roo-ing. We hope to see you soon! \n\n'
            break
        elif c == 'g' or c == 'generate' or c == 'generate schedule':
            print '\t Generating New \'Rooin\' Schedule'

        elif c == 'a' or c == 'add' or c == 'add recipe':
            print 'Lets add some new food'

        elif c == 'help':

        else:
            print 'I\'m sorry, I don\'t understand what you mean. Try again.'


if __name__ == "__main__":
    '''
    When run from the command line, runs startUp()
    '''
    startUp()
