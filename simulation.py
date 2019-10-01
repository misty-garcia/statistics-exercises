import pandas as pd
import numpy as np

# 1. How likely is it that you roll doubles when rolling two dice?r
n_trials = 10_000_000
n_dice = 2

rolls = np.random.choice([1,2,3,4,5,6],(n_trials,n_dice))

df_rolls = pd.DataFrame(rolls)
(df_rolls[0] == df_rolls[1]).mean()

# 2. If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?
n_trials = 10_000
n_coins = 8

flips = np.random.choice(["H","T"],(n_trials,n_coins))
flips

((flips == "H").sum(axis=1) == 3).mean()

((flips == "H").sum(axis=1) > 3).mean()

# 3. There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?
n_sim_boards = nrows = 10_000
n_boards = ncols = 2 
p_dscohort = .25

data = np.random.random((nrows,ncols))
data

billboard = (data <= p_dscohort)

(billboard.sum(axis=1) == 2).mean()

# 4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?
n_trials = 10_000
avg_poptart = 3
days = 5
error = 1.5
total_poptarts = 17

poptarts_eaten = np.random.normal(avg_poptart*days,error,n_trials)
poptarts_eaten = poptarts_eaten.round()
poptarts_eaten

(total_poptarts - poptarts_eaten >= 1).mean()

# 5. Compare Heights

# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?
avg_man_height = 178
man_height_sd = 8
avg_wom_height = 170
wom_height_sd = 6

n_trials = 10_000

men_heights = np.random.normal(avg_man_height, man_height_sd, n_trials)
wom_heights = np.random.normal(avg_wom_height, wom_height_sd, n_trials)

(wom_heights > men_heights).mean()

# 6. When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?
n_trials = nrows = 1_000_000
p_corrupt = 1/250

students = ncols = 50
data = np.random.random((nrows,ncols))
corrupt = (data <= p_corrupt)
(corrupt.sum(axis=1) == 0).mean()

students = ncols = 100
data = np.random.random((nrows,ncols))
corrupt = (data <= p_corrupt)
(corrupt.sum(axis=1) == 0).mean()

# What is the probability that we observe an installation issue within the first 150 students that download anaconda?
students = ncols = 150
data = np.random.random((nrows,ncols))
corrupt = (data <= p_corrupt)
(corrupt.sum(axis=1) == 0).mean()
1 - (corrupt.sum(axis=1) == 0).mean()

# How likely is it that 450 students all download anaconda without an issue?
students = ncols = 450
data = np.random.random((nrows,ncols))
corrupt = (data <= p_corrupt)
(corrupt.sum(axis=1) == 0).mean()

# 7. There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?
n_trials = 10_000
p_foodtruck = .70
days = 3

data = np.random.random((n_trials,days))
data
no_food_truck = data >= p_foodtruck
1-((no_food_truck).sum(axis=1) == 0).mean()

# How likely is it that a food truck will show up sometime this week?
days = 7

data = np.random.random((n_trials,days))
food_truck = data <= p_foodtruck
((food_truck).sum(axis=1) >= 1).mean()

# 8. If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?
n_trial = 10_000
days = list(range(1,365))

people = 23

data = np.random.choice(days,(n_trial,people))
data

df_data = pd.DataFrame(data)
df_data
df_data.nunique(axis=1)
df_data.nunique(axis=1) == people
(df_data.nunique(axis=1) == people).mean()

people = 20
data = np.random.choice(days,(n_trial,people))
df_data = pd.DataFrame(data)
(df_data.nunique(axis=1) == people).mean()

people = 40
data = np.random.choice(days,(n_trial,people))
df_data = pd.DataFrame(data)
(df_data.nunique(axis=1) == people).mean()

