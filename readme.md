# First Part - Setup

The initial set of commits involved implementing prior features from earlier assignments into the project. The structure is designed with dynamically loaded plugins that contain logging functions which catch errors and register information. Added basic, non-Pandas history command.

# Second Part - Pandas

The second section was implementing Pandas. In order to do so, I used the base CSV command that was provided with the project, and modified it to receive four separate potential inputs after typing csv in the command line: save, load, clear, delete. These sub-commands allow the user to save a given history, load it in the command line, as well as clear and delete them from the csv file. 

# ENV Variables

The main section I used environmental variables for was one provided through the project, namely the plugin system. It allows the user to easily introduce new commands into the program without having to manually add them into the command handler.

# Pattern

The general design pattern I've used throughout the project is Command Pattern. Using a plugin setup, the program is designed to receive a given command by the user alongside a set of positional arguments, which are then received by the program to then output a given result.

# Logging

Logging was introduced to all relevant command executions. When the user inputs a given operation, they receive an output, both of which are logged accordingly. When an error is made, such as if they input a letter or attempt to divide by zero, the error is caught and registered in a log. Loading and accessing the program similarly make logs, as does turning off the program. 

# LBYL / EAFP 

These principles are demonstrated with the divide command, which has three exceptions, two of which are shared with all other commands. The first is a simple divide by zero exception, which catches and registers if the user tries to divide something like 5 by 0. The second is universal and checks if they try to input letters as their input. The third is universal too, and is a generic exception that registers when other errors appear.

# Video

https://youtu.be/5tx0fOX3OaM

