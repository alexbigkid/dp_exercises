# :octocat: Design Pattern Exercises :octocat: <!-- omit in toc -->
This repo is used for design Pattern exercises of the book Head First Design Patterns.
See: https://www.amazon.com/Head-First-Design-Patterns-Brain-Friendly/dp/0596007124
However instead of Java, Python is used for the exercises.

# Table of Contents <!-- omit in toc -->
- [1. Chapter 1 - Strategy Pattern](#1-chapter-1---strategy-pattern)
- [2. Prerequisites](#2-prerequisites)
- [3. Program tested running on:](#3-program-tested-running-on)

# OO Basics <!-- omit in toc -->
- Abstraction
- Encapsulation
- Polymorthism
- Inheritance

# OO Principles <!-- omit in toc -->
- Encapsulate what varies
- Favor composition over inheritance
- Program to interfaces, not implementations

# SOLID Principles <!-- omit in toc -->
|          | name                          | description                                                                                                                                               |
| :------- | :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <b>S</b> | <b>Single Responsibility:</b> | A class should have one, and only one, reason to change                                                                                                   |
| <b>O</b> | <b>Open/Close:</b>            | Open for extention, Close for modifications                                                                                                               |
| <b>L</b> | <b>Liskov Substitution:</b>   | objects of a superclass shall be replaceable with objects of its subclasses without breaking the application                                              |
| <b>I</b> | <b>Interface Segregation:</b> | Clients should not be forced to depend upon interfaces that they do not use                                                                               |
| <b>D</b> | <b>Dependency Inversion:</b>  | High-level modules, which provide complex logic, should be easily reusable and unaffected by changes in low-level modules, which provide utility features |


## 1. Chapter 1 - Strategy Pattern
<b>The Strategy Pattern</b> defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.


## 2. Prerequisites
| tool   | description                                                                  |
| :----- | :--------------------------------------------------------------------------- |
| make   | tool to execute compile instructions from Makefile                           |
| pip    | python package installer                                                     |
| python | python interpreter (3.8.9 was used)                                          |
| pyenv  | pyenv is used to auto switch to python 3.8.9 virtual environment             |
| direnv | direnv is used to setup locally needed environment variables like PYTHONPATH |



## 3. Program tested running on:
- [x] MacOS Monterey (local machine) / Python 3.8.9
- [ ] Linux Ubuntu 20.04  / Python 3.8.5
- [ ] Windows 10 (pipeline) / Python 3.7
- [ ] Raspberry Pi Zero W (via ssh) / Python 3.7.3


<!-- ## Instructions for developers
| command           | description                                  |
| :---------------- | :------------------------------------------- |
| make help         | to see all make rules                        |
| make my_dish      | executes the main program                    |
| make install      | installs required packages                   |
| make install_dev  | installs required development packages       |
| make test         | runs test                                    |
| make test_verbose | runs test with verbose messaging             |
| make coverage     | runs test, produces coverage and displays it | --> |


<!-- ## Screenshot of functioning app
![The screenshot](docs/running_app.jpg?raw=true "running app") -->

:checkered_flag:
