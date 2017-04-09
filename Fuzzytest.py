# FYP2017
# Program to determine economy level of system using fuzzy logic (TESTING)
# Author: Kunal Jagadeesh
# License: Public Domain

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
batt_percent = ctrl.Antecedent(np.arange(0, 101, 1), 'Battery_percentage')
temp = ctrl.Antecedent(np.arange(15, 35, 1), 'Temperature')
cloud_cover = ctrl.Antecedent(np.arange(0, 1, 0.01), 'Cloud_cover')
eco_level = ctrl.Consequent(np.arange(1, 4, 0.01), 'Economy_level')

# Battery membership function population
batt_percent['Low_battery'] = fuzz.trapmf(batt_percent.universe, [0, 0, 20, 30])
batt_percent['Medium_battery'] = fuzz.trapmf(batt_percent.universe, [20, 25, 75, 80])
batt_percent['High_battery'] = fuzz.trapmf(batt_percent.universe, [75, 80, 100, 100])

# Temperature membership function population
temp['Low_temperature'] = fuzz.trapmf(temp.universe, [0, 0, 20, 22])
temp['Medium_temperature'] = fuzz.trapmf(temp.universe, [20, 23, 27, 30])
temp['High_temperature'] = fuzz.trapmf(temp.universe, [28 , 30, 35, 35])

# Cloud_cover membership function population
cloud_cover['Minimum_clouds'] = fuzz.trapmf(cloud_cover.universe, [0, 0, 0.20, 0.25])
cloud_cover['Medium_clouds'] = fuzz.trapmf(cloud_cover.universe, [0.20, 0.25, 0.65, 0.70])
cloud_cover['High_clouds'] = fuzz.trapmf(cloud_cover.universe, [0.65, 0.70, 1, 1])

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
eco_level['Critical'] = fuzz.trimf(eco_level.universe, [0, 1.0, 2.0])
eco_level['Alert'] = fuzz.trimf(eco_level.universe, [1.75, 2.25, 2.75])
eco_level['Normal'] = fuzz.trimf(eco_level.universe, [2.5, 3.0, 3.5])
eco_level['Economyless'] = fuzz.trimf(eco_level.universe, [3.25, 4.0, 5.0])

batt_percent.view()
temp.view()
cloud_cover.view()
eco_level.view()

# Rules
rule1 = ctrl.Rule(batt_percent['Low_battery'] &
                  (~temp['High_temperature']),
                  eco_level['Critical'])
rule2 = ctrl.Rule(batt_percent['Low_battery'] &
                  temp['High_temperature'] &
                  cloud_cover['High_clouds'],
                  eco_level['Critical'])
rule3 = ctrl.Rule(batt_percent['Low_battery'] &
                  temp['High_temperature'] &
                  (~cloud_cover['High_clouds']),
                  eco_level['Alert'])
rule4 = ctrl.Rule(batt_percent['Medium_battery'] &
                  temp['Low_temperature'] &
                  (~cloud_cover['High_clouds']),
                  eco_level['Alert'])
rule5 = ctrl.Rule(batt_percent['Medium_battery'] &
                  temp['Low_temperature'] &
                  cloud_cover['High_clouds'],
                  eco_level['Critical'])
rule6 = ctrl.Rule(batt_percent['Medium_battery'] &
                  (~temp['Low_temperature']) &
                  (~cloud_cover['High_clouds']),
                  eco_level['Normal'])
rule7 = ctrl.Rule(batt_percent['Medium_battery'] &
                  (~temp['Low_temperature']) &
                  cloud_cover['High_clouds'],
                  eco_level['Alert'])
rule8 = ctrl.Rule(batt_percent['High_battery'] &
                  temp['Low_temperature'] &
                  (~cloud_cover['High_clouds']),
                  eco_level['Normal'])
rule9 = ctrl.Rule(batt_percent['High_battery'] &
                  temp['Low_temperature'] &
                  cloud_cover['High_clouds'],
                  eco_level['Alert'])
rule10 = ctrl.Rule(batt_percent['High_battery'] &
                  (~temp['Low_temperature']) &
                  (~cloud_cover['High_clouds']),
                  eco_level['Economyless'])
rule11 = ctrl.Rule(batt_percent['High_battery'] &
                  (~temp['Low_temperature']) &
                  cloud_cover['High_clouds'],
                  eco_level['Normal'])

eco_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4,
                                   rule5, rule6, rule7, rule8,
                                   rule9, rule10, rule11])

eco_mode = ctrl.ControlSystemSimulation(eco_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
eco_mode.input['Temperature'] = 50
eco_mode.input['Cloud_cover'] = 0.5
eco_mode.input['Battery_percentage'] = 50

# Crunch the numbers
eco_mode.compute()

print (eco_mode.output['Economy_level'])
eco_level.view(sim=eco_mode)

