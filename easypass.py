import random

counts = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' , 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen']
objects = ['cats', 'dogs', 'deers', 'lambs', 'birds', 'camels', 'people', 'monkeys' ,'rats','insects', 'mosquitos', 'snakes', 'giraffes', 'elephants', 'rabbits']
actions = ['play', 'watch', 'read', 'discuss']
activites = ['football', 'basketball', 'tennis', 'sex', 'cycling', 'archery', 'running', 'swimming', 'jumping', 'handball', 'hockey', 'dart', 'billards', 'chess', 'jenga', 'monopoly', 'risk', 'munchkin', 'gameofthrones', 'friends', 'breakingbad', 'lacasadepapel']
prepositions = ['in', 'on', 'under', 'behind', 'at']
locations = ['the world', 'the backyard', 'the garden' ,'the zoo', 'the football field', 'the milky way', 'galaxy' ,'paris', 'amsterdam' ,'berlin', 'istanbul', 'tokyo', 'warsaw', 'budapest', 'prague', 'rome', 'vienna', 'zurich']
times = ['once', 'twice', 'three times', 'four times', 'five times', 'six times', 'seven times']
intervals = ['a day', 'a year', 'a month', 'a week', 'a decade', 'a century']
numbers = '1234567890'
symbols = '+-*/?*!=.:;'

count = ''.join(random.choice(counts))
obj = ''.join(random.choice(objects))
action = ''.join(random.choice(actions))
activity = ''.join(random.choice(activites))
prepos = ''.join(random.choice(prepositions))
location = ''.join(random.choice(locations))
time = ''.join(random.choice(times))
interval = ''.join(random.choice(intervals))
number = ''.join(random.choices(numbers, k=random.choice([1,2,3])))
symbol = ''.join(random.choices(symbols, k=random.choice([1])))


total = count + ' ' + obj + ' ' + action + ' ' + activity + ' ' + prepos + ' ' + location + ' ' + time + ' ' + interval + ' ' + number + ' ' + symbol
print(total)

passwordstring = total.replace(' ', '')
print(passwordstring)
print(len(passwordstring))