# Abyde
Esoteric language thingy IDK pls help    
Default file extension is `abde`
## Registers
`ro` is the register that all commands output to.    
`ra` is a register used for basic data storage.    
`rb` is a register also used for basic data storage.    
`rs` contains the current byte to be output to screen.    
All registers should start at zero, except for `rb`, which should start at one.
## Instructions
All commands are seperated by `|`.    
Parameters are seperated by ` `.    
Sections are ended with `||`.    
`a` Adds parameter one and two and outputs to ro.    
`s` Subtracts parameter two from one and outputs to ro.    
`m` Moves data from the second parameter to the first parameter.    
`o` Outputs rs to stdout.    
`i` Waits for one byte stdin and outputs to ro.    
`b` Checks if the first parameter is zero and, if so, continues.    
Else, it jumps to the next section.    
`q` Stops execution entirely.    
## Test
In examples you are provided with `fulltest.abyde`.    
To pass the provided test with a working interpreter, type anything into stdin    
except for `a`. It should fail if you input `a` and only `a` (that means it works)