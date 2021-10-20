# Scaling-Dice
Your goal for this challenge is to write a Python function to determine the probability of different outcomes when rolling an arbitrary set of dice.

## Monte-Carlo Simulation Dices
MCS uses random sampling to evaluate possible outcomes.

* Your program should simulate rolling dice over and over to see how many times each outcome occurs and then determine the probabilities based on that.
* You'll need to simulate a really large number of rolls to get a result that's statistically significant. 

## Input
Variable Number of Arguments for sides of dice. 

## Output 
Table of probability for each possible outcome. 

For e.g. 
*  from dice import roll_counter
*  roll_counter(4,6,6,6,4)

Outcome	Probability
5	0.03%
6	0.14%
7	0.43%
8	1.01%
9	1.95%
10	3.36%
11	5.10%
12	7.11%
13	8.95%
14	10.53%
15	11.41%
16	11.32%
17	10.51%
18	9.01%
19	7.07%
20	5.14%
21	3.33%
22	1.96%
23	1.02%
24	0.43%
25	0.15%
26	0.03%
