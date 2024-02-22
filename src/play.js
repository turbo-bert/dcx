[
    ["//", "========================================================================================================="],
    ["//", "This is an example file - making it hopefully easier to start things for you when you're new to this!"],
    ["//", "========================================================================================================="],
    ["//", "- A play.js file is valid JSON and consists of ONLY ONE singular array (as you can see) with many, many STEPS being arrays for themselves - again"],
    ["//", "- All columns in a STEP array are typed as string! So don't put numbers or booleans in it! (ok, first column can be real null)"],
    ["//", "- If a STEP's first column is a double slash '//' it won't be executed. Just make sure it's still JSON..."],
    ["//", "- 1st column of a step refers to an element with a XPath expression (beware of the escaping, JSON, ...)"],
    ["//", "- 2st column is the actual command you want to execute - followed by any needed columns for parameters"],
    ["//", "- Don't forget - last command must not have a trailing comma, this is JSON..."],
    ["//", "- Your default ENV is prefilled 2 variables: $PWD, $HOME . They can directly be used in 'env' expansion for inputs, ..."],
    ["//", "- Extend four ENV by creating a play.env file. Don't use any ticks after the '=' sign"],
    ["//", ""],
    
    [null, "get", "https://google.de"],
    [null, "path", "/why"],

    [null, "halt"]                    
]
