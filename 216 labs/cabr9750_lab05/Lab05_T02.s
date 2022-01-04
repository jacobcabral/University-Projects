/*
-------------------------------------------------------
file name
description
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
Date:    2021-02-25
-------------------------------------------------------
*/
.org    0x1000    // Start at memory location 1000
.text
.global _start
_start:
    LDR    R2, =Data    // Store address of start of list
    LDR    R3, =_Data   // Store address of end of list
    MOV    R1,#0 //SUM
    MOV    R4,#0 // count values
    MOV    R5,#0 // count bytes
Loop:
    LDR    R0, [R2], #4    // Read address with post-increment (R1 = *R2, R2 += 4)
    ADD    R1, R0, R1
    ADD    R4, R4, #1
    ADD    R5, R5, #4
    CMP    R3, R2       // Compare current address with end of list
    BNE    Loop         // If not at end, continue 

_stop:    B    _stop

.data
.align
    Data:    .word   4,5,-9,0,3,0,8,-7,12    // The list of data
    _Data:    // End of list address
.end