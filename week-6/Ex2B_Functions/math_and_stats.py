import random      # The numbers will be different every time you run it because of the random values
import math        # for pi, rounding up and down
import statistics  # for mean, median, mode, etc.

vals_1_100 = range(1, 100)
# creates a sequence of numbers from 1 to 99

vals_sample = random.sample(vals_1_100, 75)
# picks 75 unique random numbers from your sequence (no repeats)

vals_choices = random.choices(vals_1_100, k=200)
# picks 200 random numbers, repeats are allowed

radius = random.randint(3, 10)
# picks one random number between 3 and 10 for our circle radius

pi = math.pi
# stores the value of pi (3.14159...)

sum_sample = sum(vals_sample)
# adds all 75 numbers together

avg_sample = statistics.mean(vals_sample)
# finds the average of the 75 numbers

median_sample = statistics.median(vals_sample)
# finds the middle number of the 75 numbers

avg_200 = statistics.mean(vals_choices)
# finds the average of all 200 numbers

median_200 = statistics.median(vals_choices)
# finds the middle number of the 200 numbers

mode_200 = statistics.mode(vals_choices)
# finds the number that appears the most in our 200 numbers

stdev_200 = statistics.stdev(vals_choices)
# measures how spread out the 200 numbers are

var_200 = statistics.variance(vals_choices)
# another way to measure how spread out the 200 numbers are

area_raw = pi * radius ** 2
# calculates the area of our circle using pi x radius squared

area_up = math.ceil(area_raw)
# rounds the area UP to the nearest whole number

area_dn = math.floor(area_raw)
# rounds the area DOWN to the nearest whole number

print("_Experimenting with a subset of integers 1-100:")
# prints the first section header (underscore is required by the lab)

print(f"Sum of 75 sample values from 1 to 100: {sum_sample}")
# prints the sum of our 75 numbers

print(f"Average of 75 sample values: {avg_sample:.2f}")
# :.2f means round to 2 decimal places when printing

print(f"Median of 75 sample values: {median_sample}")

print('\n')
# adds a blank line between sections

print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {avg_200:.2f}")
print(f"Median of 200 values: {median_200}")
print(f"Mode of 200 values: {mode_200}")
print(f"Standard deviation of 200 values: {stdev_200:.2f}")
print(f"Variance of 200 values: {var_200:.2f}")

print('\n')
# another blank line between sections

print("_Modeling a random circle:")

print(f"Radius = {radius}, area = {area_up} (rounded up to the nearest integer)")
# prints the area rounded up

print(f"Radius = {radius}, area = {area_dn} (rounded down to the nearest integer)")
# prints the area rounded down