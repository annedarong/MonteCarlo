#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Course: DS 5100 
Topic: Final Project
Student: Anneda Rong (aar2dk)
Date: July 2022
"""

from multiprocessing.sharedctypes import Value
from operator import index
import pandas as pd
import numpy as np
import random

class Die:
    
    def __init__(self, faces):
        '''
        Initializes the Die class. Takes in an array of faces and initalizes all weights of the face to 1 and creates a dataframe with the array of faces and weights.

        @faces: An array or list of ints or strings of numbers
        '''
        self.faces = faces
        self.weight = np.full(len(faces),1.0)
        self._face_weight_df = pd.DataFrame({'Faces':self.faces,'Weights':self.weight})
    
    def change_weight(self, face, new_weight):
        '''
        Changes a face's corresponding weight. Accepts the face value that the new weight will be applied to.

        @face: An integer or string of the face to change
        @new_weight: The new weight value to change the corresponding face to
        '''
        current_faces = self._face_weight_df['Faces']
        is_face = (face == current_faces).any()
        if (not is_face):
            raise Exception("The 'face' passed is not found.")

        try:
            float(new_weight)
        except ValueError:
            raise ValueError("The 'weight' passed cannot be converted to a float/number. Please pass in a valid numerical value.")

        loc = current_faces[current_faces == face].index[0]
        self._face_weight_df.iloc[loc,1] = float(new_weight)
    
    def roll_die(self, num_times = 1):
        '''
        A function to roll the die based on the provided faces and weights. Will return a list of face outcome(s)

        @num_times: An integer representing the number of times to roll the die. Default is set to 1.
        '''
        faces = self._face_weight_df['Faces']
        weights = self._face_weight_df['Weights']
        outcome = random.choices(faces,weights,k = num_times)
        return(outcome)
    
    def show(self):
        '''
        returns the dataframe
        '''
        return(self._face_weight_df)

class Game:
    def __init__(self, die_objects):
        self.die_objects = die_objects
    
    def play(self, num_times):
        '''
        takes how many times want to roll dice

        rolls the dice

        saves N x M df (where N = rolls and M = dice)
        '''
        game_dict = {}
        for i, val in enumerate(self.die_objects):
            game_dict[i] = val.roll_die(num_times)
        self._game_df = pd.DataFrame(game_dict)
        self._game_df.index = self._game_df.index + 1
        self._game_df.index.name = "Rolls"
    
    def show(self, size = 'wide'):
        '''
        if wide, return game_df
        if narrow, set multi-index
        check if size is valid (either narrow or wide)
        '''
        game_df = self._game_df
        size = str.lower(size)
        if (size != 'wide' and size != 'narrow'):
            raise Exception("Invalid input. Input must either be 'narrow' or 'wide'.")
        if (size ==  'narrow'):
            values = self._game_df.values
            reshaped_val = np.reshape(values,values.shape[0] * values.shape[1])
            iterables = [[*range(1,len(self._game_df.index) + 1)], list(self._game_df.columns)]
            index = pd.MultiIndex.from_product(iterables, names = ["Roll","Dice"])
            game_df = pd.DataFrame({"Face Values": reshaped_val}, index = index)
        return game_df

class Analyzer:
    def __init__(self, game_object):
        '''
        Initializes the Game object along with the data type of the Game's values

        @game_object: A Game Object to be analyzed on
        '''
        self.game_object = game_object
        d_type = type(self.game_object.show().values)

    def jackpot(self):
        '''
        Finds the amount of time a play had all of the same faces on a roll.

        Returns the count of jackpots that were in the Game.
        Results of which play had the jackpot are returned in a dataframe called jackpot_df
        '''    
        same_row_df = self.game_object.show().apply(lambda x: x == x[0], axis = 1).all(1)
        self.jackpot_df = (self.game_object.show().iloc[:,0])[same_row_df]
        count = sum(same_row_df)
        return count

    def combo(self):
        '''
        Keeps track of distinct combinations. Results of the combination along with how many time the combinations appeared are returned in a dataframe called combo_df. All combonations are sorted in ascending order.
        '''
        game_df = self.game_object.show()
        combo_count = {}
        combo_list = []
        game_df.apply(lambda x: combo_list.append(tuple(x.sort_values())),axis = 1)
        for i in combo_list:
            if i in combo_count:
                combo_count[i] += 1
            else:
                combo_count[i] = 1
        index_name = [f"Position {x+1}"for x in range(game_df.shape[1])]
        self.combo_df = pd.DataFrame({"Combo Count":combo_count.values()}, index = pd.MultiIndex.from_tuples(combo_count.keys(), name = index_name))

    def face_counts_per_roll(self):
        '''
        Computes how many times a given face is rolled in each event.
        '''
        faces = self.game_object.die_objects[0].show()['Faces']
        current_game = self.game_object.show()
        faces_dict = dict.fromkeys(faces)
        values = current_game.values
        for i, val in enumerate(values):
            for v in val:
                value_dict = faces_dict[v]
                if (value_dict == None):
                    faces_dict[v] = [0 for x in range(current_game.shape[0])]
                faces_dict[v][i] += 1
        self.face_counts_df = pd.DataFrame(faces_dict)
        self.face_counts_df.index += 1
        self.face_counts_df.index.name = "Roll Number"
        self.face_counts_df.fillna(0,inplace=True)