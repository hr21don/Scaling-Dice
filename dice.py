from random import randint #simulate dice rolls
from collections import Counter #tracking frequency of each outcome


def roll_counter(*dice, time_set=1_000_000): #Accepts a variable number of arguments to represent any number of sides on the dice and an additional argument to simulate the running-trails
    counts = Counter() #keeping track of outcomes

    for roll in range(time_set): #simulating rolling dice for the number of trails
        counts[sum((randint(1,sides) for sides in dice))] += 1 #using randint function to simulate rolling each of the dice and then sum the individual outcomes together

    print('\nOutcome\tProbability')

    for collect_outcome in range(len(dice), sum(dice) + 1): #printing each possible outcome as a percentage
        print('{}\t{:0.2f}%'.format(collect_outcome, counts[collect_outcome]*100/time_set))
        
