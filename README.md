blendNameChange
===============

This little script will help rename the of most attributes of an object and its properties, useful for renaming parts of a reusable asset. *When enabled, this panel appears under the "Tools" tab of the toolshelf in the 3D view, under the panel "Rename Attributes"*.

How to use
===============

To use this script, select all the objects that have attributes you want to change. Check the base name you want to replace and write this in the first field of the rename attributes panel, "find". Then in the second field write in the name to replace it with, "replace". Hit rename to run the script.

Alternatively, the script can be used to simply add a prefix name to the same kind of attributes. Write in 'replace' the name to be put in front of all other names, again working on selected objects and its attributes. Note, if you want "body" to become "main.body", the replace field should have "main." including the dot.


Example Rename
===============

With find=x, replace=y:
If you have an objects named x.leg, x.head, and x, and on these objects is the material someMat.x and it has a texture someMat.x.tex and the objects are part of the group named x.group, the result is:

Objects named y.leg, y.head, and y, and the material is now named someMat.y on all users of the mateiral (selected or not) and it has a texture someMat.y.tex and the group name is now y.group, even if not all members of the group were selected


Example Prefix
===============

With find=x, replace=y.:
If you have an objects named x.leg, x.head, and x, and on these objects is the material someMat.x and it has a texture someMat.x.tex and the objects are part of the group named x.group, the result is:

Objects named y.x.leg, y.x.head, and y.x, and the material is now named y.someMat.x on all users of the mateiral (selected or not) and it has a texture y.someMat.x.tex and the group name is now y.x.group, even if not all members of the group were selected


Known issues
===============

currenly works for most cases, except for example:
find: stevey
replace with: steve

the following does work, however:
find: steve
replace with: stevey

You also cannot 'replace' with nothing, that is, an empty string

Please contact me for other issues or usage questions and feel free to improve!
