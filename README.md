# Thought.ai OA

#### REF: https://thoughtfulautomation.notion.site/FDE-Technical-Screen-12af43a78fa480af8d97c2fc9478cb18

## Intro
Hi,
This repo consists of code for a simple sorting task as part of technical screening at Thoughtful ai.

TASK: Based on given sorting conditions, create a sort function that accepts width, height, length and mass and returns the type of STACK the package belongs to.
The stack can be "STANDARD", "SPECIAL", or "REJECTED".

## Steps to Run
Assumption: you have already git cloned the project and moved inside the current directory.

1. Import the class in your code\
    `from package_sorter import PackageSorter`

2. Initialize an instance of the class\
    `my_package_sorter = PackageSorter()`

3. Run the sort function\
    `my_package_sorter.sort(100,22,34,4)`

## Steps to Test
I am using the pytest package to streamline testing.
I'd recommend creating a virtual environment first!

I have written about 22 tests, which tests edge cases, and bad input types which are auto handled or auto rejected!

1. Install pytest by typing the following command in your terminal\
    `pip install -r requirements.txt`\
    or\
    `pip install pytest`

2. Run all tests by typing the folling command in your terminal\
    `pytest`

3. If `pytest` is not recogized you may use\
    `python -m pytest`


