---
title: "Processing Multiple Files and Writing Files"
teaching: 25
exercises: 10
questions:
- "How do I analyze multiple files at once?"
objectives:
- "Import a python library."
- "Use python library funtions."
- "Process multiple files using a `for` loop."
- "Print output to a new text file."
keypoints:
- "Use the glob function in the python library glob to find all the files you want to analyze."
- "You can have multiple `for` loops nested inside each other."
- "Python can only print strings to files."
- "Don't forget to close files so python will actually write them."
---
## Processing multiple files

In our previous lesson, we parsed values from output files.  While you might have seen the utility of doing such a thing, you might have also wondered why we didn't just search the file and cut and paste the values we wanted into a spreadsheet.  If you only have 1 or 2 files, this might be a very reasonable thing to do.  But what if you had 100 files to analyze?  What if you had 1000?  In such a case the cutting and pasting method would be very tedious and time consuming.  

One of the real powers of writing a program to analyze your data is that you can just as easily analyze 100 files as 1 file.  In this example, we are going to parse the output files for a several of the latest entires to the [Protein Data Bank](https://www.rcsb.org/) and extract resolution data and atom counts for each one.  The output files are all saved in a folder called PDB_files that you should have downloaded in the setup for this lesson.  Make sure the folder is in the same directory as the directory where you are writing and executing your code.

To analyze multiple files, we will need to import a python **library**.  A **library** is a set of modules which contain functions. The functions within a library or module are usually related to one another. Using libraries in Python reduces the amount of code you have to write. In the last lesson, we imported `os.path`, which was a module that handled filepaths for us.

In this lesson, we will be using the `glob` library, which will help us read in multiple files from our computer.  Within a library there are modules and functions which do a specific computational task.  Usually a function has some type of input and gives a particular output.  To use a function that is in a library, you often use the dot notation introduced in the previous lesson.  In general
```
import library_name
output = library_name.funtion_name(input)
```
{: .language-python}

We are going to import two libraries.  One is the `os` library which controls functions related to the operating system of your computer. We used this library in the last lesson to handle filepaths.  The other is the `glob` library which contains functions to help us analyze multiple files.  If we are going to analyze multiple files, we first need to specify where those files are located.

>## Exercise
>
> How would you use the `os.path` module to point to the directory where your PDB files are located?
>
>> ## Solution
>> ~~~
>> outfile = os.path.join('data', 'PDB_files')
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}

In order to get all of the files which match a specific pattern, we will use the wildcard character `*`.

```
file_location = os.path.join('data', 'PDB_files', '*.pdb')
print(file_location)
```
{: .language-python}
```
data/PDB_files/*.pdb
```
{: .output}

This specifies that we want to look for all the files in a directory called `data/PDB_files` that end in ".pdb".  The * is the wildcard character which matches any character.  

Next we are going to use a function called `glob` in the library called `glob`.  It is a little confusing since the function and the library have the same name, but we will see other examples where this is not the case later.  The output of the function `glob` is a list of all the filenames that fit the pattern specified in the input.   The input is the file location.
```
import glob
filenames = glob.glob(file_location)
print(filenames)
```
{: .language-python}
```
['data/PDB_files/6l35.pdb', 'data/PDB_files/7tim.pdb', 'data/PDB_files/4eyr.pdb', 'data/PDB_files/4ezi.pdb', 'data/PDB_files/7l1f.pdb', 'data/PDB_files/6vqs.pdb', 'data/PDB_files/7bgj.pdb', 'data/PDB_files/7bfv.pdb', 'data/PDB_files/1vxh.pdb', 'data/PDB_files/7dno.pdb', 'data/PDB_files/6lsv.pdb']
```
{: .output}

This will give us a list of all the files which end in `*.pdb` in the `PDB_files` directory. Now if we want to parse every file we just read in, we will use a `for` loop to go through each file.
```
for f in filenames:
    outfile = open(f,'r')
    data = outfile.readlines()
    outfile.close()
    for line in data:
        if 'RESOLUTION.' in line:
            res_line = line
            words = res_line.split()
            resolution = float(words[3])
            print(resolution)
```
{: .language-python}

```
3.23
1.9
1.8
1.15
3.89
2.38
6.9
1.84
1.7
2.03
2.65
```
{: .output}

Notice that in this code we actually used two `for` loops, one nested inside the other.  The outer `for` loop counts over the filenames we read in earlier.  The inner `for` loop counts over the line in each file, just as we did in our previous file parsing lesson.  

The output our code currently generates is not that useful.  It doesn't show us which file each resolution value came from.  

We want to print the name of the molecule with the resolution. We can use `os.path.basename`, which is another function in `os.path` to get just the name of the file.

~~~
first_file = filenames[0] # look above to recall the content of filenames
print(first_file)

file_name = os.path.basename(first_file)
print(file_name)
~~~
{: .language-python}

~~~
data/PDB_files/6l35.pdb
6l35.pdb
~~~
{: .output}

> ## Exercise
>
> How would you extract the PDB ID from the example above?
>
>> ## Solution
>> You can use the `str.split` function introduced in the last lesson, and split at the '.' character.
>> ~~~
>> split_filename = file_name.split('.')
>> molecule_name = split_filename[0]
>> print(molecule_name)
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}

Using the solution above, we can modify our loop so that it prints the file name along with each resolution value.

~~~
for f in filenames:
    # Get the PDB ID
    file_name = os.path.basename(f)
    split_filename = file_name.split('.')
    molecule_name = split_filename[0]

    # Read the data
    outfile = open(f,'r')
    data = outfile.readlines()
    outfile.close()

    # Loop through the data
    for line in data:
        if 'RESOLUTION.' in line:
            res_line = line
            words = res_line.split()
            resolution = float(words[3])
            print(molecule_name, ":", resolution)
~~~
{: .language-python}

~~~
6l35 : 3.23
7tim : 1.9
4eyr : 1.8
4ezi : 1.15
7l1f : 3.89
6vqs : 2.38
7bgj : 6.9
7bfv : 1.84
1vxh : 1.7
7dno : 2.03
6lsv : 2.65
~~~
{: .output}

## Printing to a File
Finally, it might be useful to print our results in a new file, such that we could share our results with colleagues or or e-mail them to our advisor.  Much like when we read in a file, the first step to writing output to a file is opening that file for writing.  In general to open a file for writing you use the syntax
```
filehandle = open('file_name.txt', 'w+')
```
{: .language-python}

The `w` means open the file for writing.  If you use `w+` that means open the file for writing and if the file does not exist, create it.  You can also use `a` for append to an existing file or `a+`.  The difference between `w+` and `a+` is that `w+` will overwrite the file if it already exists, whereas `a+` will keep what is already there and just add additional text to the file.  

Python can only write strings to files.  Our current print statement is not a string; it prints two python variables.  To convert what we have now to a string, you place a capital **F** in front of the line you want to print and enclose it in single quotes.  Each python variable is placed in braces. Then you can either print the line (as we have done before) or you can use the `filehandle.write()` command to print it to a file.

To make the printing neater, we will separate the file name from the energy using a tab. To insert a tab, we use the special character `\t`.

```
datafile = open('resolutions.txt', 'w+')  #This opens the file for writing

for f in filenames:
    # Get the PDB ID
    file_name = os.path.basename(f)
    split_filename = file_name.split('.')
    molecule_name = split_filename[0]
    
    # Read the data
    outfile = open(f,'r')
    data = outfile.readlines()
    outfile.close()    
    
    # Loop through the data
    for line in data:
        if 'RESOLUTION.' in line:
            res_line = line
            words = res_line.split()
            resolution = float(words[3])
            datafile.write(F'{molecule_name} \t {resolution} \n')
            
datafile.close()
```
{: .language-python}

After you run this command, look in the directory where you ran your code and find the "resolutions.txt" file.  Open it in a text editor and look at the file.

In the file writing line, notice the `\n` at the end of the line.  This is the newline character.  Without it, the text in our file would just be all smushed together on one line.  Also, the `filehandle.close()` command is very important.  Think about a computer as someone who has a very good memory, but is very slow at writing.  Therefore, when you tell the computer to write a line, it remembers what you want it to write, but it doesn't actually write the new file until you tell it you are finished.   The `datafile.close()` command tells the computer you are finished giving it lines to write and that it should go ahead and write the file now.  If you are trying to write a file and the file keeps coming up empty, it is probably because you forgot to close the file.  

## A final note about string formatting
The F'string' notation that you can use with the print or the write command lets you format strings in many ways.  You could include other words or whole sentences.  For example, we could change the file writing line to
```
datafile.write(F'For the PDB Entry {molecule_name} the resolution is {resolution} in Angstroms.')
```
{: .language-python}
where anything in the braces is a python variable and it will print the value of that variable.  

{% include links.md %}

## Project Assignment
You can complete this assignment to test your skills. This project should be used when this material is used in a long workshop, or if you are working through this material independently.

> ## File parsing homework
>
> The goal of this exercise is to extract the Enzyme Commission Class for a series of enzyme structures in PDB files and write them to a new text file called 'EC_class.txt'. The files are located in the `data/enzymes` folder. If you open any of these files and search for the term "EC:" you will find a listing that looks like this:

> COMPND   6 EC: 1.2.1.13;      
> You are probably familiar with these numbers, but just in case - the Enzyme Commission class tells you the function of an enzyme in a hierarchical format. You can learn more at the [BRENDA EC Explorer](https://www.brenda-enzymes.org/ecexplorer.php?browser=1&f[nodes]=21&f[action]=close&f[change]=21#21). 
> Your assignment is to parse the files in the `data/enzymes` folder and write a new file named  `EC_class.txt` that contains the PDB ID and EC class for each of these enzymes. When you open the file in your text editor, it should look like this:

> 7tim 	  5.3.1.1 
> 6zt7 	  3.2.1.55 
> 5eu9 	  4.2.1.11 
> 3iva 	  2.1.1.13 
> 2pkr 	  1.2.1.13 
> 3vnd 	  4.2.1.20 
> 5veu 	  1.14.14.1

>> ## Hint
>> It helps when you are writing code to break up what you have to do into steps. Overall, we want to get information from the file. How do we do that?

>> If you think about the steps you will need to do this assignment you might come up with a list that is like this, you might have a list like

>> 1.    Open the file for reading
>> 1.    Read the data in the file
>> 1.    Loop through the lines in the file.
>> 1.    Get the information from the line we are interested in.
>> 1.    Write the information to a file.

>>It can be helpful when you code to write out these steps and work on it in pieces. Try to write the code using these steps. Note that as you write the code, you may come up with other steps! 
>> First, thing about what you have to do for step 1, and write the code for that. Next, think about how you would do step 2 and write the code for that. You can troubleshoot each step using print statments. 
>> The steps build on each other, so you can work on getting each piece written before moving on to the next. 
>> 
>> ## Solution
>> ~~~
>> \# *Open the file for reading*
>> file_location = os.path.join('data', 'enzymes', '*.pdb')
>> \# *# Make sure you can see all of the files*
>> filenames = glob.glob(file_location)
>> print(filenames)  #Once you're sure it's working, comment this line out.
>> \# *Loop through the lines in the files*
>> datafile = open('EC_class.txt', 'w+')  #This opens the file for writing
>> for f in filenames:
>>     # Get the PDB ID
>>     file_name = os.path.basename(f)
>>     split_filename = file_name.split('.')
>>     molecule_name = split_filename[0]
>>\# *Get the information from the line we are interested in.*    
>>     outfile = open(f,'r')
>>     data = outfile.readlines()
>>     outfile.close()
>> \# *Write the information to a file*
>>     for line in data:
>>         if 'EC:' in line:
>>             ec_line = line
>>             words1 = ec_line.split(';')    
>>             # print(words1)
>>             words2 = words1[0].split(':')
>>             datafile.write(F'{molecule_name} \t {words2[1]} \n')       
>> datafile.close()
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}