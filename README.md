# MonteCarlo

Metadata
Student Name: Anneda Rong (aar2dk)
Project Name: Monte Carlo Simulator


Synopsis; Code for: <br />
    How to Install: <br />
    Once the repo is pulled in locally run the command below to install module. <br />
    ```
    pip install -e .
    ```
    <br />
    <br />
    How to Import: <br />
    Simply import MonteCarlo to being using the module. <br />
    ```
    import MonteCarlo
    ```
    <br />
    <br />
    How to Create Dice: <br />
    To create a Die Object a list must be passed through specifying the faces that are to be put on the Dice. <br />
    ```
    TestDice = Die(['H','T'])
    ```
    <br />
    <br />
    How to Play Games: <br />
    In order to play a Game class a Game object is needed. The Game class accepts a list of Die Objects. <br />
    ```
    TestGame = Game([Die1,Die2])
    ```
    <br />
    To play the Game simply use the play method that takes in a parameter specifying how many "games" are to be played. <br />
    ```
    TestGame.play(100)
    ```
    <br />
    Nothing is returned as all the game data is saved in a dataframe that can be see with the show method. <br />
    ```
    TestGame.show()
    ```
    <br />
    <br />
    How to Analyze Games: <br />
    In order to analyze the games a game object must be passed to the Analyzer class. <br />
    ```
    TestAnalyzer = Analyzer(TestGame)
    ```
    <br />
    There are three analyze methods that can be used. <br />
    ```
    TestAnalyzer.jackpot()
    TestAnalyzer.combo()
    TestAnalyzer.face_counts_per_roll()
    ```
<br />
<br />
API description <br />
The ‘Die’ Class: <br />
	Methods: <br />
	change_weight():
        Changes a face's corresponding weight. Accepts the face value that the new weight will be applied to.
        <br />
        @face: An integer or string of the face to change <br />
        @new_weight: The new weight value to change the corresponding face to <br />
	roll_die(): 
        A function to roll the die based on the provided faces and weights. Will return a list of face outcome(s) <br />
        @num_times: An integer representing the number of times to roll the die. Default is set to 1.
<br />
<br />
The ‘Game’ Class:<br />
	Methods:<br />
	play():
        @num_times: the amount of time to play the game or roll the dice <br />
        takes how many times want to roll dice
        rolls the dice
        saves N x M df (where N = rolls and M = dice) <br />
        show():
        @size: indicates how the dataframe to look. Either 'wide' or 'narrow' <br />
        if wide, return game_df
        if narrow, set multi-index
        check if size is valid (either narrow or wide)
        <br />
        <br />


The ‘Analyzer’ Class: <br />
	Methods: <br />
	jackpot():
        Finds the amount of time a play had all of the same faces on a roll.
        Returns the count of jackpots that were in the Game.
        Results of which play had the jackpot are returned in a dataframe called jackpot_df <br />
        combo():
        Keeps track of distinct combinations. Results of the combination along with how many time the combinations appeared are returned in a dataframe called combo_df. All combonations are sorted in ascending order. <br />
        face_counts_per_roll():
        Computes how many times a given face is rolled in each event.
        <br />
        <br />

Manifest: <br />
__init__.py <br />
setup.py <br />
montecarlo.py <br />
montecarlo_tests.py <br />
montecarlo_demo.ipynb <br />
letter-freqs.csv <br />
FinalProjectSubmission.ipynb
