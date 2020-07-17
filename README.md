# Abyde
Esoteric language thingy IDK pls help    
Default file extension is `abyde`
## Registers
`ro` is the register that all commands output to.    
`ra` is a register used for basic data storage.    
`rb` is a register also used for basic data storage.    
`rt` is a temporary register that should mainly only be used as swap.    
`rs` contains the current byte to be output to screen.    
All registers should start at zero, except for `rb`, which should start at one.
## Instructions
All commands are seperated by `|`.    
Parameters are seperated by ` `.    
Sections are ended with `||`.    
`a` Adds parameter one and two and outputs to ro.    
`s` Subtracts parameter two from one and outputs to ro.    
`m` Copies data from the second parameter to the first parameter.    
`o` Outputs rs to stdout.    
`i` Waits for one byte stdin and outputs to ro.    
`b` Continue if parameter is not zero.    
`q` Stops execution entirely.    
`r` Repeats the current section.    
## Test
In examples you are provided with `fulltest.as`.    
You will need to properly compile this from AbydeScript    
and run it in a working interpreter.    
The test should only pass if you type `a`.    
Otherwise, it should fail.