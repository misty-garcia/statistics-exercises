# For the following problems, use python to simulate the problem and calculate an experimental probability, then compare that to the theoretical probability.
from scipy import stats
import numpy as np
import pandas as pd

# A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.
n_trials = 10_000

sim_cars = np.random.poisson(2,n_trials)

cars = stats.poisson(2)

# What is the probability that no cars drive up in the noon hour?
(sim_cars == 0).mean()

cars.pmf(0)

# What is the probability that 3 or more cars come through the drive through?
(sim_cars >= 3).mean()

cars.sf(2)

# How likely is it that the drive through gets at least 1 car?
(sim_cars >= 1).mean()

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
np.percentile(gpa,position*100 - 10)

stats.norm(3,.3).ppf(position)
stats.norm(3,.3).ppf(position-.10)

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

data = np.random.choice(["click","no click"], (n_trials,visitors), p=[.02,.98])
((data == "click").sum(axis=1) >= 97).mean()

stats.binom(visitors,avg_click).sf(clicks-1)

# 4. You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.
n_trials = 10_000
p_correct = 1/100

# What is the probability that at least one of your first 60 answers is correct?
questions = 60

data = np.random.choice(["correct","not correct"],(n_trials,questions),p=[p_correct,1-p_correct])
((data == "correct").sum(axis=1) >= 1).mean()

stats.binom(questions,p_correct).sf(0)

# 5. The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. 
n_trials = 10_00
p_cleaning = .03
cohorts = 3
students_p_cohort = 22
p_students_break = .9
students_on_break = round(cohorts * students_p_cohort * p_students_break)

data = np.random.choice(["clean","no clean"],(n_trials,students_on_break),p=[.03,.97])
p_day_clean = ((data == "clean").sum(axis=1) >= 1).mean()
p_day_clean #experiment

p_clean_day = stats.binom(students_on_break,p_cleaning).sf(p_students_break)
p_clean_day #theory 

# How likely is it that the break area gets cleaned up each day?
n_days = 5
data = np.random.choice(["clean today", "no clean today"],(n_trials,n_days),p = [p_day_clean, 1-p_day_clean])
((data == "clean today").sum(axis=1) == n_days).mean() 

stats.binom(n_days,p_clean_day).pmf(n_days)

# How likely is it that it goes two days without getting cleaned up?
n_days = 2
data = np.random.choice(["clean today", "no clean today"],(n_trials,n_days),p = [p_day_clean, 1-p_day_clean])
((data == "no clean today").sum(axis=1) == n_days).mean() 

stats.binom(n_days,1-p_clean_day).pmf(n_days) 

# How likely is it that it goes all week without getting cleaned up?
n_days = 5
data = np.random.choice(["clean today", "no clean today"],(n_trials,n_days),p = [p_day_clean, 1-p_day_clean])
((data == "no clean today").sum(axis=1) == n_days).mean() 

stats.binom(n_days,1-p_clean_day).pmf(n_days)


# 6. You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.
n_trials = 10_000
mean = 15
sd = 3
order_time = 2
receive_time = 10
lunch_time = 60

num_people = np.random.normal(mean,sd,n_trials).round()
wait = (num_people + 1) * order_time + receive_time
((lunch_time - wait) >=15).mean()

# turn it into time? 
mean_order_time = mean * order_time
sd_order_time = sd * order_time

stats.norm(mean_order_time,sd_order_time).cdf(33)

# Connect to the employees database and find the average salary of current employees, along with the standard deviation. Model the distribution of employees salaries with a normal distribution and answer the following questions:

# What percent of employees earn less than 60,000?
# What percent of employees earn more than 95,000?
# What percent of employees earn between 65,000 and 80,000?
# What do the top 5% of employees make?