"""program to demonstrate match """

lang=input("enter any programming lang")

match lang:
    case "c":print("i like c")
    case "java":print("i like java")
    case "python":print ("i like python")
    case _:print ("dont like any languages")
           
"""out put:
enter any programming langc
i like c

enter any programming langjava
i like java

enter any programming langpython
i like python

enter any programming langc++
dont like any languages"""

