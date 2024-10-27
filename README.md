[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LZ95pz-v)
# CS151 PROGRAMMING ASSIGNMENT #3

### 🔵 Understand the problem and Design before Coding 🔵

#### 🟢 FINAL DUE: Thursday 11/07/24

- #### Programming Grade: EMRN    

## I. PROBLEM:

- You are creating a program to display ASCII art and string decorations to the user. 
- ASCII art is just a combination of characters that make a design or pattern.

## II. PURPOSE OF THE ASSIGNMENT

The purpose of this assignment is to give you  
1. Practice with protecting against bad user input
2. Practice with decision making
3. An opportunity to use looping
4. Practice with designing functions
5. Practice with implementing functions
6. A chance to be creative

## III. REQUIREMENTS ANALYSIS 

The first stage in your programming assignment is the requirements analysis stage.  
- You must understand the problem before you can try to solve it.

Your program must give the user three design options. 
- It should allow users to keep choosing options and seeing the output from their choice until they've chosen to stop: Outputting a circle, outputting a set of lines, or outputting a random design. 
- Each of those options have further requirements below. 
  - Your program must be implemented such that all of your code is in functions, where each function solves one task.

### Outputting  a circle
How can you make a circle? This shape will be more an approximation of a circle using slashes, underscores, and/or dashes. 
- Don't overthink it; this part shouldn't be too hard, just figure out how to output the right characters to make what basically looks like a circle on the screen.

### Outputting a set of lines
The user gets to decide three things each time they choose an option:

1. How many lines to draw. The lines are drawn directly after each other, on a new line.
2. What character or set of characters are repeated to make the line
3. How many times to repeat the character(s) for the line

For example, if the user chooses to output 3 lines that use "*" that is repeated 20 times, the output will look like:
```
********************
********************
********************
```

### Random design
You must create three different designs to be displayed. 
- When the user chooses this option, your program will randomly choose which of the three designs to output. 

For your three designs, they must be substantially different from the circle and line requirements. 
- You can, however, get inspiration from elsewhere. Here are the rules:

1. **At most one design may be an _ASCII art_ you find online**, 
   - Even if it includes the python code to generate it. 
   - *You MUST put a comment with exactly where you got it from if you go this route, otherwise it is plagiarism.*
        ```python
        (\,--------'()'--o
         (_    ___    /~"
          (_)_)  (_)_)
        ```
2. **Your other two designs must be entirely your own creation or inspired by art you find elsewhere.** 
   - However, you *may NOT look up the code for how to create them*; you must try to figure it out yourself. 
   - You can use string functionality, loops, etc. 
   - If you get inspiration from elsewhere, credit that inspiration in your code in a comment!
3. **Only one of your designs may write out the art line by line**; 
   - All others must have some more complex element. 
   - For example it may have a loop, use the `*` symbol to replicate a string, or use a string function call.

### Usability
Your program must have excellent usability, including error checking. 
- It should be clear what to input, and error checking should prevent the user from crashing your program.

## IV. DESIGN

The second stage is to design your solution based on the requirements. 
   - Think about how to break the problem up into different smaller problems that are easier to solve. 
   - In particular, what functions do you need? 
     - Remember that functions are the single tasks that the program is solving.

Although **🟢design are not to be turned in🟢**, I high recommend doing this for yourself.
   - You can use `design.md` and `flowchart.drawio.svg` to practice your solution.

For this design, you need to determine the functions that you need. 
   - For each function you need to know:
```
Purpose:
Name:
Parameters:
Return:
Algorithm: 
```

For the main function, you also need an algorithm for what the high level steps of the algorithm will be. 
- If you need to call a function, saying something like "Call the XXX function with arguments Y, Z" 
  - (if a function was named XXX and you had values Y and Z you were planning to send as arguments, e.g. `XXX(Y,Z)`).

## V. PROGRAMMING REQUIREMENTS

After your design is complete and correct, it’s time to start programming and then testing. 
- This is a great time to start practicing iterative development. 
- Instead of writing an entire program and then testing it, write part of it, test it, then write the next part. 
- That way if something is broken it will be easier to figure out why. 
  - You are **🟢not required turn in test🟢**, but you can use `test_cases.xlsx` to keep track of your tests
- Now that you have functions, there are natural ways to build up a working program. 
  - For example, get the basic menu functionality working, where you just output what each option does. 
  - Then, add in one design (say, the circle) and make sure that works. 
  - Then add in the code for the lines. 
  - Then start adding in the three option designs. 
- This way, you have a working program after each addition, and can test if it's right before you move on to the rest of the code. 
  - You should commit and push frequently --- after each coding session or function that you have written.

Remember that your program should:
1. Follow good usability/HCI principles in input and output. 
- You must go above and beyond what we were doing in the first half of the semester, now that we know how to special characters like tabs, and f strings for print formatting.
2. Protect the program against bad user input
3. State at the start the purpose of the program.

## VII. ASSIGNMENT REMINDERS

Follow the programming assignment requirements document for comments, formatting, etc.
- Follow the honor code guidelines outlined in the syllabus and at https://www.loyola.edu/academics/computer-science/current-students/honor-code.

**Remember to ask for help early if you are stuck -- don't wait until the night before it's due to start asking for help.**

## `VIII. FINAL SUBMISSION due 11/07`
### What to Submit in GitHub:

1. Completed `main.py` file
2. `reflection.md` -> Reflection of the assignment


**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get? 
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working by yourself?
   
***Remember to commit and push your GitHub project.***