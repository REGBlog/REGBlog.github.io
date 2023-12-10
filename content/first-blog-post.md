+++
title = 'Unlocking the Mysteries of Numbers: A Python Adventure into the Collatz Conjecture'
date = 2023-12-09T19:55:01-05:00
draft = false
description = "Join me as we delve into the captivating realms of the Collatz Conjecture, an enduring enigma in the world of mathematics. In this blog post, I explore the depths of the '3x + 1 problem' using Python as our guide. I'll walk you through the fundamental concepts of the conjecture, followed by a detailed, step-by-step Python tutorial to unravel its mysteries visually. This post is perfect for anyone fascinated by mathematical puzzles, from students and educators to coding enthusiasts and lifelong learners. Together, we'll discover how simple mathematical rules can create complex and mesmerizing patterns, offering insights into the world of numbers and coding in a fun and engaging way."
keywords = "Collatz Conjecture Exploration, Personal Journey in Mathematics, Python Visualization Guide, Understanding 3x + 1 Problem, Exploring Mathematical Puzzles, My Experience with Number Theory, Python Coding for Math, Matplotlib for Beginners, Demystifying Mathematical Conjectures, Interactive Math Learning Experience, STEM Education Insights, Mathematics and Coding Fusion, Personal Math Adventures, Data Visualization Techniques, Programming in Education, Collatz Conjecture, Mathematics Blog, Python Visualization, 3x + 1 Problem, Mathematical Puzzles, Number Theory, Python Programming, Matplotlib Tutorial, Mathematical Conjectures, Interactive Math Learning, STEM Education, Coding in Mathematics, Math and Python, Data Visualization, Educational Programming, Reese Gerjekian, REG Blog"
image = "/images/collatz.webp"
imageBig = "/images/collatz.webp"
categories = ["Python", "Math", "Programming", "Education"]
authors = ["Reese Gerjekian"]
avatar = "/images/reg-avatar.png"
+++

The Collatz Conjecture is a mathematical hypothesis that has puzzled mathematicians for decades. Also known as the "3x + 1 problem", it involves taking any positive integer and applying a simple process: if the number is even, divide it by two; if it's odd, triple it and add one. The conjecture states that no matter what number you start with, you will always eventually reach 1.

In this post, we'll explore this conjecture using Python, specifically visualizing the journey of a number as it goes through this process.

### Setting Up the Environment

First, we need to import the necessary module for plotting our results. We'll use `matplotlib.pyplot` for this purpose.

```python
import matplotlib.pyplot as plt
```

### Initializing the Axes

Next, we set up our x-axis and y-axis lists. The x-axis (`iteration_num_list`) will record the number of iterations, and the y-axis (`num_list`) will record the number at each iteration.

```python
iteration_num_list = [0]
num_list = []
```

### Input and Validation

We need to ensure that the user enters a positive number to start the process. The following code snippet takes care of this:

```python
positive = False
while not positive:
    print("Enter any number: ")
    num = float(input())

    if num <= 0:
        print("INVALID, ENTER POSITIVE NUMBER: ")
    else:
        positive = True
        num_list.append(num)
```

### The Collatz Process

Now comes the core part of our script: applying the Collatz Conjecture to the input number.

```python
num = 3 * num + 1

while num > 1:
    if num % 2 == 0:
        num = num / 2
    else:
        num = 3 * num + 1

    iteration_num_list.append(iteration_num_list[-1] + 1)
    num_list.append(num)
```

### Visualizing the Results

Finally, we plot our results using `matplotlib.pyplot`.

```python
plt.plot(iteration_num_list, num_list)
plt.xlabel('iteration')
plt.ylabel('x in 3(x) + 1')
plt.title('3(x) + 1')
plt.show()
```

This graph provides a visual representation of how the number evolves through the process.

### Completed Code

```python

# importing the required module
import matplotlib.pyplot as plt

# declare x-axis
iteration_num_list = []
x = 0
iteration_num_list.append(x)

# check for positive number
positive = False
while positive == False:
    print("Enter any number: ")
    num = float(input())

    if num <= 0:
        print("INVALID, ENTER POSITIVE NUMBER: ")
        continue
    else:
        break


# declare y-axis
num_list = []
num_list.append(num)

num = 3 * num + 1

while num > 1:
    # if num is even, then divide by 2
    if num % 2 == 0:
        print(num)
        num = num / 2
        # add 1 to the x-axis
        x = x + 1
        iteration_num_list.append(x)
        # add num to the y-axis
        num_list.append(num)
        continue
    # if num is odd, repeat 3(num)+1
    else:
        print(num)
        num = 3 * num + 1
        # add 1 to the x-axis
        x = x + 1
        iteration_num_list.append(x)
        # add num to the y-axis
        num_list.append(num)
        continue

print(num)
print("Done!")

# plotting the points
plt.plot(iteration_num_list, num_list)

# naming the x axis
plt.xlabel('iteration')
# naming the y axis
plt.ylabel('x in 3(x) + 1')

# giving a title to my graph
plt.title('3(x) + 1')

# function to show the plot
plt.show()
```

### Conclusion

The Collatz Conjecture, simple in its definition, leads to surprisingly complex behavior. Through this Python exercise, we get a glimpse of the intriguing patterns that emerge from such a simple algorithm.
