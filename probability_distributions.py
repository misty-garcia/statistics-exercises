# For the following problems, use python to simulate the problem and calculate an experimental probability, then compare that to the theoretical probability.
from scipy import stats
import numpy as np

# A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.
cars = stats.poisson(2)

# What is the probability that no cars drive up in the noon hour?
cars.pmf(0)

# What is the probability that 3 or more cars come through the drive through?
cars.sf(2)

# How likely is it that the drive through gets at least 1 car?
cars.sf(0)

# 2. Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following:
# What grade point average is required to be in the top 5% of the graduating class?
n_trials = 10_000
mean = 3.0
std = 0.3

position = 95
gpa = np.random.normal(mean, std, n_trials)
np.percentile(gpa,position)

stats.norm(3,.3).isf(.05)
stats.norm(3,.3).ppf(.95)

# What GPA constitutes the bottom 15% of the class?
position = 15
gpa = np.random.normal(mean, std, n_trials)
np.percentile(gpa,position)

stats.norm(3,.3).ppf(.15)

# An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?
position = .30
gpa = np.random.normal(mean, std, n_trials)
np.percentile(gpa,position*100)
np.percentile(gpa,position*100 + 10)

stats.norm(3,.3).ppf(position)
stats.norm(3,.3).ppf(position+.10)

# If I have a GPA of 3.5, what percentile am I in?
grade = 3.5
gpa = np.random.normal(mean, std, n_trials)
(gpa <= 3.5).mean()

stats.norm(3,.3).cdf(grade)

# 3. A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 click-throughs. How likely is it that this many people or more click through?
n_trials = 10_000
avg_click = .02
visitors = 4326
clicks = 97

visitors/clicks

data = np.random.choice(["click","no click"], (n_trials,visitors), p=[.02,.98])
((data == "click").sum(axis=1) >= 97).mean()
data

stats.binom(visitors,avg_click).sf(clicks)

# 4. You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.
questions = 100 

# What is the probability that at least one of your first 60 answers is correct?
answers = 60

# The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. How likely is it that the break area gets cleaned up each day? How likely is it that it goes two days without getting cleaned up? All week?

# You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

