# MonteCarlo

Metadata
Student Name: Anneda Rong (aar2dk)
Project Name: Monte Carlo Simulator


Synopsis; Code for:
    How to Install:
    Once the repo is pulled in locally run the command below to install module.
    '''
    pip install -e .
    '''
    How to Import: 
    Simply import MonteCarlo to being using the module.
    '''python
    import MonteCarlo
    '''
    How to Create Dice:
    To create a Die Object a list must be passed through specifying the faces that are to be put on the Dice.
    '''python
    TestDice = Die(['H','T'])
    '''
    How to Play Games:
    In order to play a Game class a Game object is needed. The Game class accepts a list of Die Objects.
    '''python
    TestGame = Game([Die1,Die2])
    '''
    To play the Game simply use the play method that takes in a parameter specifying how many "games" are to be played.
    '''python
    TestGame.play()
    '''
    Nothing is returned as all the game data is saved in a dataframe that can be see with the show method.
    '''python
    TestGame.show()
    '''
    How to Analyze Games:
    In order to analyze the games a game object must be passed to the Analyzer class.
    '''python
    TestAnalyzer = Analyzer(TestGame)
    '''
    There are three analyze methods that can be used.
    '''python
    TestAnalyzer.jackpot()
    TestAnalyzer.combo()
    TestAnalyzer.face_counts_per_roll()
    '''

API description
The ‘Die’ Class:
	Methods:
		change_weight():
        Changes a face's corresponding weight. Accepts the face value that the new weight will be applied to.

        @face: An integer or string of the face to change
        @new_weight: The new weight value to change the corresponding face to
		

        roll_die():
        A function to roll the die based on the provided faces and weights. Will return a list of face outcome(s)

        @num_times: An integer representing the number of times to roll the die. Default is set to 1.

The ‘Game’ Class:
	Methods:
		play():
        takes how many times want to roll dice
        rolls the dice
        saves N x M df (where N = rolls and M = dice)
		
        
        show():
        if wide, return game_df
        if narrow, set multi-index
        check if size is valid (either narrow or wide)


The ‘Analyzer’ Class:
	Methods:
		jackpot():
        Finds the amount of time a play had all of the same faces on a roll.
        Returns the count of jackpots that were in the Game.
        Results of which play had the jackpot are returned in a dataframe called jackpot_df


		combo():
         Keeps track of distinct combinations. Results of the combination along with how many time the combinations appeared are returned in a dataframe called combo_df. All combonations are sorted in ascending order.


		face_counts_per_roll():
         Computes how many times a given face is rolled in each event.

Manifest:
__init__.py
setup.py
montecarlo.py
montecarlo_tests.py
montecarlo_demo.ipynb
letter-freqs.csv
FinalProjectSubmission.ipynb
