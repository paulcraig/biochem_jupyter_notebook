---
title: "File Parsing"
teaching: 20
exercises: 25
questions:
- "How do I sort through all the information in a text file and extract particular pieces of information?"
objectives:
- "Open a file and read in its contents line by line."
- "Search for a particular string in a file."
- "Manipulate strings and change data types."
- "Print to a new file."
keypoints:
- "You should use the os.path module to work with file paths."
- "One of the most flexible ways to read in the lines of a file is the `readlines()` function."
- "An `if` statement can be used to find a particular string within a file."
- "The split() function can be used to seperate the elements of a string."
- "You will often need to recast data into a different data type when it was read in as a string."
---
## Working with files
One of the most common tasks in research is analyzing data.  An enormous amount of data is currently being generated in biochemistry and molecular biology, much of it pertaining to sequence and structure. The PDB file format is commonly used to describe macromolecular structures that have been determined by experimental methods. You may be interested in exploring the text and/or the data in a PDB file.  While the [PDB web site](https://www.rcsb.org/) is very helpful, there are times when it would be handy to extract specific information about one protein (or 1,000) with a few keystrokes. For example, you might be interested in the resolution of a structure, or the small molecules that are bound to the macromolecule.  In general, this is called file parsing.

### Working with file paths - the `os.path` module
For this section, we will be working with the file `4eyr` in the `PDB_files` directory.

To see this, go to a new cell and type `ls`. `ls` stands for 'list', and will list all of the contents of the current directory. **This command is not a Python command, but will work in the Jupyter notebook**. To see everything in the `data` directory, type

~~~
ls data
~~~

You should see something like **All filenames and directory listings will need to be updated**
~~~
PDB_files/      remdesivir.pdb  remdesivir.sdf  remdesivir.xyz
~~~
{: .output}

Here, `remdesivir.pdb`, `remdesivir.sdf`, and `remdesivir.xyz` are all files, while `PDB_files` is another directory.

In order to parse a file, you must tell Python the location of the file, or the "file path". For example, you can see what folder your Jupyter notebook is in by typing `pwd` into a cell in your notebook and evaluating it. `pwd` stands for 'print working directory', and can also be used in your terminal to see what directory you're in.

After evaluating the cell with `pwd`, you should see an output similar to the following if you are on Mac or Linux:
~~~
'/Users/YOUR_USER_NAME/biochem_jupyter_book/Workshop_plagiarized_to_biochem'
~~~
{: .output}

or similar to this if you are on Windows
~~~
'C:\Users\YOU_USER_NAME\biochem_jupyter_book/Workshop_plagiarized_to_biochem'
~~~
{: .output}

Notice that the file paths are different for these two systems. The Windows system uses a forward slash ('\\'), while Mac and Linux use a backslash ('/') for filepaths.

When we write a script, we want it to be usable on any operating system, thus we will use a python module called `os.path` that will allow us to define file paths in a general way.

In order to get the path to the `4eyr.pdb` file in a general way, type
~~~
import os

protein_file = os.path.join('data', 'PDB_files','4eyr.pdb')
print(protein_file)
~~~
{: .python}

You should see something similar to the following
~~~
data/PDB_files/4eyr.pdb
~~~
{:. .output}

Here, we have specified that our filepath contains the 'data' and 'PDB_files' directory, and the `os.path` module has made this into a filepath that is usable by our system. If you are on Windows, you will instead see that a forward slash is used.

> ## Absolute and relative paths
> File paths can be *absolute*, or *relative*.
>
> A relative file path gives the location relative to the directory we are in. Thus, if we are in the `Workshop_plagiarized_to_biochem` directory, the relative filepath for the `4eyr.pdb` file would be `data/PDB_files/4eyr.pdb`
>
> An absolute filepath gives the complete path to a file. This could file path could be used from anywhere on a computer, and would access the same file. For example, the absolute filepath to the  `4eyr.pdb` file on a Mac might be `Users/YOUR_USER_NAME/biochem_jupyter_book/Workshop_plagiarized_to_biochem`. You can get the absolute path of a file using `os.path.abspath(path)`, where path is the relative path of the file.
{: .callout}

> ## Python `pathlib`
> We are working with the `os.path` module here, and this is how you will see people handle file paths in most Python code. However, as of Python 3.6, there is also a `pathlib` module in the Python standard library that can be used to represent and manipulate filepaths. `os.path` works with filepaths as strings, while in the `pathlib` module, paths are objects. A good overview of the pathlib module can be found [here](https://realpython.com/python-pathlib/).
{: .callout}

## Reading a file

In Python, there are many ways in python to read in information from a text file.  The best method to use depends on the type of data and the type of analysis you are performing.  If you have a file with lots of different types of information, text and numbers, with different types of formatting, the most generic way to read in information is the `readlines()` function.  Before you can read in a file, you have to open the file using the file path we defined above. This will create a file object, or filehandle.  The file we will be analyzing in this example is a [PDB web site](https://www.rcsb.org/structure/4EYR) file for an HIV protease complex with the inhibitor Ritonavir.

```
outfile = open(protein_file,"r")
data = outfile.readlines()
```
{: .language-python}
This code opens a file for reading and assigns it to the filehandle  `outfile`. The `r` argument in the function stands for `read`. Other arguments might be `w` for `write` if we want to write new information to the file, or `a` for append if we want to add new information at the end of the file.

In the next line, we use the `readlines` function to get our file as a list of strings.  Notice the dot notation introduced last lesson; readlines acts on the file object given right before the dot.  The function creates a list called data where each element of the list is a string that is one line of the file.  This is always how the
`readlines()` function works.

> ## `readlines` function behavior
> Note that the `readlines` function can only be used on a file object one time. If you forget to set `outfile.readlines()` equal to a variable, you must `open` the file again in order to get the contents of the file.
{: .callout}

After you open and read information from a file object, you should always close the file.

~~~
outfile.close()
~~~
{: .language-python}

> ## Check Your Understanding
> Check that your file was read in correctly by determining how many lines are in the file.
>> ## Answer
>> ~~~
>> print(len(data))
>> ~~~
>> {: .language-python}
>> ~~~
>> 2232
>> ~~~
>> {: .output}
> {: .solution}
{: .challenge}

## Searching for a pattern in your file
The file we opened is the complete PDB file for the [Crystal structure of multidrug-resistant clinical isolate 769 HIV-1 protease in complex with ritonavir](https://www.rcsb.org/structure/4EYR).  As stated previously, the `readlines()` function put the file contents into a list where each element is a line of the file. You may remember from lesson 1 that a `for` loop can be used to execute the same code repeatedly. As we learned in the previous lesson, we can use a for loop to iterate through elements in a list.

Let's take a look at what's in the file.

~~~
for line in data:
  print(line)
~~~
{: .language-python}

This will print exactly what is in the file.

If you look through the output, you will find a line that starts with HETNAM. This line contains information about the ligand or small molecule that is bound to HIV protease in this structure, providing both the abbreviation (RIT) and the full name of the drug (RITONAVIR).  We want to search through this file and find that line, and print only that line. We can do this using an `if` statement.

Returning to our file example,

```
for line in data:
    if 'HETNAM' in line:
        HETNAM_line = line
        print(HETNAM_line)
```
{: .language-python}

```
HETNAM     RIT RITONAVIR
```
{: .output}

Remember that `readlines()` saves each line of the file as a string, so `HETNAM_line` is a string that contains the whole line.  For our analysis, if we are most interested in the abbreviation for the drug, we need to split up the line so we can save just that abbreviation as a different variable name. To do this, we use a new function called `split`.  The `split` function takes a string and divides it into its components using a *delimiter*.

The *delimiter* is specified as an argument to the function (put in the parenthesis `()`). If you do not specify a delimiter, a space is used by default. Let's try this out.

~~~
HETNAM_line.split()
~~~
{: .language-python}

~~~
['HETNAM', 'RIT', 'RITONAVIR']
~~~
{: .language-output}

We can save the output of this function to a variable as a new list. In the example below, we take the line we found in the `for` loop and split it up into its individual words.

```
words = HETNAM_line.split()
print(words)
```
{: .language-python}

```
['HETNAM', 'RIT', 'RITONAVIR']
```
{: .output}

From this `print` statement, we now see that we have a list called words, where we have split `HETNAM_line`.  The abbreviation is actually the second element of this list, so we can now save it as a new variable.

```
abbrev = words[1]
print(abbrev)
```
{: .language-python}

```
RIT
```
{: .output}

We might also want to extract the number of atoms in the protein in this file. We will modify the above steps to achieve the desired result. We will be looking for the line that contains the term `PROTEIN ATOMS`.

```
for line in data:
    if 'PROTEIN ATOMS' in line:
        PROTEIN_ATOM_line = line
        words = PROTEIN_ATOM_line.split()
        print(PROTEIN_ATOM_line)
```
{: .language-python}

```
['REMARK', '3', 'PROTEIN', 'ATOMS', ':', '1514']
```
{: .output}

We can see that the fifth element in this list is a colon (:). It is possible to modify the split command to split lines using the colon as the delimiter (':').

```
for line in data:
    if 'PROTEIN ATOMS' in line:
        PROTEIN_ATOM_line = line
        words = PROTEIN_ATOM_line.split(':')
        print(words)
```
{: .language-python}

```
['REMARK   3   PROTEIN ATOMS            ', ' 1514                                    \n']
```
{: .output}

From this `print` statement, we now see that we have a list called words, where we have split `PROTEIN_ATOM_line`.  The number of atoms in the protein is actually the second element of this list, so we can now save it as a new variable.

```
atoms = words[1]
print(atoms)
```
{: .language-python}

```
 1514                                    
```
{: .output}

The HIV protease structure in 4eyr.pdb is a dimer. Let's find the number of atoms in each monomer unit. If we now try to do a math operation on atoms, we get an error message.  Why do you think that is?
```
atoms / 2
```
{: .language-python}
```
TypeError                                 Traceback (most recent call last)
<ipython-input-43-5ff957608802> in <module>
----> 1 atoms / 2

TypeError: unsupported operand type(s) for /: 'str' and 'int'
```
{: .error}
Even though `atoms` looks like a number to us, it is really a string, so we can not add an integer to it.  We need to change the data type of energy to a float. This is called *casting*.

```
atoms = float(atoms)
```
{: .language-python}

Now it will work.  If we thought ahead we could have changed the data type when we assigned the variable originally.

```
atoms = float(words[1])
```
{: .language-python}

>## Exercise on File Parsing (should we move this to the end?)
Use the provided 7tim.pdb file, which includes structural information and data about a complex of of a small molecule bound to the enzyme, triose phosphate isomerase. Find the resolution of the structure, teh total number of protein atoms, the total number of heterogroup atoms, and the identify the small molecule (hint: HETNAM) by abbreviation and full name. Remember - you need to use os.join to be able to read the file. Your output should look like this: 
> ~~~
> RESOLUTION : 1.90 ANGSTROMS
> PROTEIN ATOMS : 3766
> HETEROGEN ATOMS : 20
> HETNAM Abbreviation: PGH Full name: PHOSPHOGLYCOLOHYDROXAMIC

> ~~~
> {: language.python}
>
> > ## Solution
>>
>> This is one possible solution for the 7tim.pdb parsing exercise.
>> ~~~
>> with open(protein_file,"r") as outfile2:
>>    data2 = outfile2.readlines()
>> for line in data2:
>>     if 'RESOLUTION.' in line:
>>        RESOLUTION_line = line
>>        words = RESOLUTION_line.split()
>>        words[2] = words[2].rstrip('.')  # to remove the . from the end of RESOLUTION.
>>        words[-1] = words[-1].rstrip('.')
>>        print(words[2], ':', words[3], words[-1])
>>    if 'PROTEIN ATOMS' in line:
>>        PROTEIN_ATOMS_line = line
>>        words = PROTEIN_ATOMS_line.split()
>>        print(words[2], words[3], ':', words[5] )
>>    if 'HETEROGEN ATOMS' in line:
>>        HETEROGEN_ATOMS_line = line
>>        words = HETEROGEN_ATOMS_line.split()
>>        print(words[2], words[3], ':', words[5])
>>    if 'HETNAM' in line:
>>        HETNAM_line = line
>>        words = HETNAM_line.split()
>>        print('HETNAM Abbreviation:', words[1], 'Full name:', words[2])
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}

## Searching for a particular line number in your file
There is a lot of other information in the PDB file we might be interested in.  For example, we might want to pull out the sequence of the protein.  If we look through the file in a text editor, we notice that the sequence is given in a series of lines that begin with `SEQRES` 

SEQRES   1 A  247  ALA ARG THR PHE PHE VAL GLY GLY ASN PHE LYS LEU ASN  

followed by a seriew of lines that contain the full sequence using three letter abbreviations for the amino acids.  In this case, we don't want to pull something out of this line, as we did in our previous example, but we want to know which line of the file this is so that we can then pull the sequence from the next few lines.  

When you use a for loop, it is easy to have python keep up with the line numbers using the `enumerate` command.  The general syntax is
```
for linenum, line in enumerate(list_name):
    do things in the loop
```
{: .language-python}

In this notation, there are now *two* variables you can use in your loop commands, `linenum` (which can be named something else) will keep up with what iteration you are on in the loop, in this case what line you are on in the file. The variable `line` (which could be named something else) functions exactly as it did before, holding the actual information from the list.  Finally, instead of just giving the list name you use `enumerate(list_name)`.  

This block of code searches our file for the line that contains "Center" and reports the line number.
```
for linenum, line in enumerate(data2):
    if 'SEQRES   1 A' in line:
        print(linenum, ':', line, sep = '')
```
{: .language-python}
```
369:SEQRES   1 A  247  ALA ARG THR PHE PHE VAL GLY GLY ASN PHE LYS LEU ASN      
```
{: .output}
Now we know that this is line 369 in our file (remember that you start counting at zero!).  

>## Check Your Understanding
>What would be printed if you entered the following:
>~~~
> print(data2[370])
> print(data2[371])
> print(data2[372])
> print(data2[373])
> print(data2[374])
> ~~~
>{: .language.python}
>
>> ## Answer
>>
>> It prints line 370-375 of the list `data` which is the first line that contains "SEQRES   1 A" and then the sequence information for the next 5 lines from the PDB file for 7TIM.
>> ~~~
>> SEQRES   2 A  247  GLY SER LYS GLN SER ILE LYS GLU ILE VAL GLU ARG LEU          

>> SEQRES   3 A  247  ASN THR ALA SER ILE PRO GLU ASN VAL GLU VAL VAL ILE          

>> SEQRES   4 A  247  CYS PRO PRO ALA THR TYR LEU ASP TYR SER VAL SER LEU          

>> SEQRES   5 A  247  VAL LYS LYS PRO GLN VAL THR VAL GLY ALA GLN ASN ALA          

>> SEQRES   6 A  247  TYR LEU LYS ALA SER GLY ALA PHE THR GLY GLU ASN SER         
>> ~~~
>> {: .output}
> {: .solution}
{: .challenge}

## A final note about regular expressions
Sometimes you will need to match something more complex than just a particular word or phrase in your output file.  Sometimes you will need to match a particular word, but only if it is found at the beginning of a line.  Or perhaps you will need to match a particular pattern of data, like a capital letter followed by a number, but you won't know the exact letter and number you are looking for.  These types of matching situations are handled with something called *regular expressions* which is accessed through the python module `re`.  While using regular expressions is outside the scope of this tutorial, they are very useful and you might want to learn more about them in the future.  A tutorial can be found at _______.  

{% include links.md %}
