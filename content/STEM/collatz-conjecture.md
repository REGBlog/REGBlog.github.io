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
linkedin = "https://www.linkedin.com/in/rgerjeki/"
github = "https://github.com/rgerjeki"
letterboxd = "https://boxd.it/971m9"
+++

---

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

### The Historical Backdrop of the Collatz Conjecture

The intriguing journey of the Collatz Conjecture began in 1937 when German mathematician Lothar Collatz proposed it. Over the years, various mathematicians have also independently discovered and analyzed it, each contributing unique perspectives to its study. Despite its apparent simplicity, this conjecture has remained an unsolved riddle in number theory, challenging the brightest minds and leading to many discussions and research papers. It is a testament to the enduring allure of mathematical puzzles, continually inspiring generations of mathematicians. Its unresolved status has piqued the interest of professional mathematicians, amateurs, and enthusiasts, leading to a rich tapestry of collaborative and individual research efforts in the pursuit of a solution.

### Understanding the Mathematics of the Collatz Conjecture

The essence of the Collatz Conjecture lies in a deceptively straightforward algorithmic process. Begin with any positive integer, then apply a simple set of rules: if the number is even, divide it by two; if it's odd, triple it and add one. Continue this process with each resulting number. The conjecture asserts that regardless of the starting number, the sequence will inevitably reach the number 1. This process produces a sequence of unpredictable numbers and varies significantly in length depending on the starting number. The beauty and complexity of the conjecture lie in this unpredictability, and it has led to various mathematical explorations and hypotheses. For instance, some mathematicians have delved into the conjecture's implications for understanding the nature of numbers and sequences. In contrast, others have explored its potential connections to other areas in mathematics, such as graph theory and probability. Despite extensive study, the question of why and how every sequence eventually leads to 1 remains a compelling mystery, making the Collatz Conjecture a prime example of the seemingly simple problems in mathematics that can conceal profound complexities.

### The Python Coding Adventure: Visualizing the Conjecture

My Python visualization guide offers more than just an explanation of the Collatz Conjecture; it brings this mathematical puzzle to vivid life. I created an interactive and dynamic visual representation of the conjecture sequences by harnessing the power of Python programming and the capabilities of Matplotlib, a popular data visualization library. As you input various numbers, Python helps us trace their journey through the Collatz process, visually mapping each step as the numbers divide, multiply, and spiral toward the inevitable 1. This program helps in understanding the process and reveals the surprising complexity and beauty hidden in what appears to be a simple sequence of operations. It's a perfect blend of mathematics and coding, offering an engaging way to explore mathematical concepts. This interactive math learning experience is invaluable in demystifying complex concepts, making them accessible and enjoyable to learners of all levels. Whether you're a seasoned programmer, a math enthusiast, or a curious beginner, this Python adventure into the Collatz Conjecture will surely captivate and educate you.

### The Collatz Conjecture in Popular Culture and Education

The Collatz Conjecture's reach extends far beyond the traditional confines of number theory, having carved a niche in popular culture and educational programming. It's frequently featured in online challenges, mathematical games, and educational videos, sparking widespread interest and debate among a diverse audience. The conjecture is an exemplary tool in education, particularly in STEM (Science, Technology, Engineering, and Mathematics) fields. It illustrates how a simple mathematical puzzle can open doors to critical thinking, problem-solving skills, and a deeper appreciation for the beauty and complexity of mathematics. Teachers and educators often use the Collatz Conjecture to introduce students to fundamental concepts in algorithms and programming, demonstrating the practical applications of these skills. Additionally, its unresolved nature makes it an excellent subject for encouraging student research and exploration, fostering curiosity, and pursuing knowledge. This blending of mathematics, entertainment, and education highlights the unique position of the Collatz Conjecture as a bridge between academic study and broader cultural engagement.

### Conclusion

As we conclude our journey through the fascinating world of the Collatz Conjecture, it's clear that this simple mathematical riddle represents much more than just a sequence of numbers. From its historical inception by Lothar Collatz in 1937 to its ongoing allure in the modern day, the conjecture stands as a symbol of the enduring mystery and beauty inherent in mathematics. Our exploration has taken us through the historical evolution of this conjecture, tracing its roots and the profound impact it has had on both professional and amateur mathematicians alike.

Our Python programming adventure brought this mathematical enigma to life, demonstrating the power of coding in visualizing complex concepts. By using Python and Matplotlib, we observed the unique patterns formed by the Collatz sequence and appreciated the seamless integration of mathematics and technology. This interactive and engaging approach to learning underscores the importance of programming in modern education, particularly in STEM fields, and its role in making abstract concepts tangible and understandable.

Furthermore, the Collatz Conjecture's presence in popular culture and educational systems highlights its versatility as a tool for learning and engagement. It is a prime example of how a seemingly simple mathematical problem can ignite curiosity, encourage critical thinking, and foster a deeper appreciation for the intricacies of number theory and algorithms.

In conclusion, the Collatz Conjecture is more than just a topic of mathematical study; it's a journey through history, a challenge for the mind, and a testament to the joys of learning and exploration. Whether you are a mathematician, a student, a programmer, or simply someone with a penchant for puzzles, the Collatz Conjecture offers a window into the limitless potential of numbers and the human mind's quest to understand them. It embodies the spirit of inquiry and the endless pursuit of knowledge. It reminds us that some straightforward questions can lead to the most profound discoveries, even in our advanced digital age.

---

References
==========

*3.11.2 Documentation*. (n.d.). Docs.python.org. https://docs.python.org/3.11/

Charles, F., Henrique, M., De, R., Thiago, O., Catalan, A., Saa, A., & Gueron, E. (n.d.). *An Analysis of the Collatz Conjecture*. Retrieved December 11, 2023, from https://www.csun.edu/~vcmth02i/Collatz.pdf

*Collatz conjecture*. (2020, September 9). Wikipedia. https://en.wikipedia.org/wiki/Collatz_conjecture

*Matplotlib documentation --- Matplotlib 3.5.0 documentation*. (n.d.). Matplotlib.org. https://matplotlib.org/stable/

Veritasium. (2021, July 30). *The Simplest Math Problem No One Can Solve - Collatz Conjecture*. Www.youtube.com. https://www.youtube.com/watch?v=094y1Z2wpJg
