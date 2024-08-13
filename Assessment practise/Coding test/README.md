# Identifying Duplicate Companies House Records

**This is an exam exercise, so treat the "tasks" below as exam questions and please focus on your theoretical approach for the first 10-15 minutes across all tasks.**

You should alter either the [JavaScript](./Files/Javascript/index.js) or [Python](./Files/Python/main.py) script to perform the tasks listed. Each task can be completed independently of the others, so if you get stuck on one this will not stop you from completing the other tasks.

## Scoring System

There is no negative or corrective marking and we accept all attempts, even if they are incomplete; however, tasks 1, 2 and 3 have been broken down in to three broad criteria, those being:

- You have written a theoretical approach in code comments (i.e. Pseudocode)
- You have made an attempt at a task; however, it is not fully functional or complete
- You have fully complete and finished a task and have followed good common practices

**This test is aimed to be general and best suited for a certain type of individual; we do not expect that most people will gain 100% marks or that all of the tasks will be fully completed to the full criteria above.**

## How to Answer

The purpose of the test is to give you the opportunity to demonstrate to us, at a minimum, your basic working understanding of the question or task areas; however, the test is also designed to give you the opportunity to demonstrate / impress us with the way you solve the problems. To achieve this, you will need to optimise the way you answer the questions.

**Based on the three bullet points in the scoring system, we would like you to spend the first 10-15 minutes understanding tasks 1, 2, and 3 and explaining the theoretical approach you would take to tasks 1, 2, and 3 before proceeding through the rest of the criteria.** This will also assist us in understanding where your skill set might be optimised even if code is not written for any one or more of the tasks.

## Tasks

### 1. Modify Comparision Function (15pts)

Running the code will reveal a duplicate of `"KADAMA, Roger Martin"` because there are two entries with identical names but different ids. However, when we examine the data, we see two unflagged company officers/directors with the ids `ek2h3gNkpApxboMC4TjygxIGoLM` and `751yqHp6Eb7m47qeSgTXDX32_OQ`.

The task at hand here is to change the `compare()` function so that these two enteries and any other potential duplicates are flagged.

### 2. Optimise for Machine Learning (15pts)

The script is currently generating a list of probable duplicates based on the attributes we have chosen, which are initially the names of the company officers/directors; however, the order is currently arbitrary, and every factor is or will be regarded equally relevant. 

The goal of this task is to modify the code so that this is not the case and that any variable factors can be fine-tuned afterwards, either manually or by a Machine Learning model.

### 3. Intergrate the Companies House REST API (30pts)

The code currently retrieves an array of officers for companies within Manchester using a [JSON file](./Files/officers.json); however, the [Companies House API](https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference) should be implemented to retrieve live data.

*Hint: To retrieve the data found in the [officers.json](./Files/officers.json) file, it will most likely be necessary to request more than one API endpoint.*

Note: Remember to include documentation on how to use the script after the API has been integrated.

## Additional Tasks (Extension)

If the previous tasks have been completed or you need a break from them, you can complete the additional tasks below, which are worth fewer points and don't give you extra points for your theoretical approach.

### 4. Unit Testing (6pts)

The [JavaScript](./Files/Javascript/index.js) and [Python](./Files/Python/main.py) scripts are currently trivial; however, there is no reason why the functions in them would not end up in a system with a CI/CD pipeline. In light of this, we want to use a unit testing framework of your choosing to ensure that when the code is modified, there are no errors or bugs in the main functions and that they return the intended results.

### 5. Code Comments (3pts)

There are currently no code comments in the [JavaScript](./Files/Javascript/index.js) or [Python](./Files/Python/main.py) scripts. This task consists of simply reading the code enough to comprehend it and adding the missing code comments to both current code and code you add so that anyone else who picks up this project will not struggle to grasp how it works.

### 6. Refactoring (4pts)

A number of bad practises and debugging have intentionally been left in the [JavaScript](./Files/Javascript/index.js) and [Python](./Files/Python/main.py) scripts; your task is to remove or fix as many of these issues as possible.