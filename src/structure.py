

from definitions import *
from rv32i import *

# --------------------------------------------------------------
# NOTICE
# Used for debugging
# Default value is 0
# You can change the value to support your debugging information
# But make sure when in level 0, the output is clean and matches the samples
class LOG(object):
    level = 1
    start_at = 0
    MAX_LEVEL = 6
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# 32 general registers in riscv
# Each register is 32 bit
registers = [
        'zero', 
        'ra',
        'sp',  
        'gp',  
        'tp',  
        't0',  
        't1',  
        't2',
        's0',   
        's1',  
        'a0',  
        'a1',  
        'a2',  
        'a3',  
        'a4',  
        'a5',
        'a6',   
        'a7',  
        's2',  
        's3',  
        's4',  
        's5',  
        's6',  
        's7',
        's8',   
        's9',  
        's10', 
        's11', 
        't3',  
        't4',  
        't5',  
        't6' 
]
# --------------------------------------------------------------



# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Register Structure
# Implement the read and write functions
# Only 1 lines are needed for each function
class REG(object):
    def __init__(self, val = 0):
        self.reg = WORD(val)

    def read(self):
        YOUR_CODE_HERE
    
    def write(self, content):
        YOUR_CODE_HERE
# --------------------------------------------------------------



# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Register File Structure
# Implement the read and write functions
# Be careful with the register index
# Special case: 
#  Read from register 0 should always return 0
#  Write to register 0 should always be ignored
class RF(object):
    def __init__(self):
        self.rf = WORD([0] * NUM_REGS)
        pass

    def read(self, reg_idx):
        YOUR_CODE_HERE

    def write(self, reg_idx, content):
        YOUR_CODE_HERE
    

    # !!!DO NOT MODIFY!!!
    # for debug, print all registers in format
    def dump(self, col=4):
        print("-------------")
        for i in range(0, NUM_REGS,col):
            str = ""
            for reg in range(i, min(NUM_REGS, i+col)):
                rname = registers[reg]
                rval = self.rf[reg]
                show_name = "%s ($%d):" % (rname, reg)
                show_val = "%-11s0x%08x    " % (show_name, rval)
                str += show_val
            print(str)
# --------------------------------------------------------------




# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Memory Structure
# retuen value: (data, access status)
# Only need you to implement the M_XRD and M_XWR cases
# Notice that the address should be word-aligned
#
# Hints:
# You should use word_address to access the memory
# Notice that each memory has its own start address
# Treat all numbers as unsigned (use WORD to warp them)
# 1 line for each case is enough
class MEM(object):
    def __init__(self, _s, _sz, _ws):
        self.word_sz = _ws
        # how many words can be stored
        self.capacity = _sz//_ws
        self.start = _s
        self.end = _s + _sz
        self.memory = WORD([0] * self.capacity)
        self.used_wd = 0      
        
    
    def access(self, valid, addr, data, ctrl):
        # valid condition
        if not valid:
            res = (WORD(0), True)
        elif (addr<self.start) or (addr>=self.end):
            res = (WORD(0), False)
        # make sure it's word-aligned
        elif addr % self.word_sz != 0:
            res = (WORD(0), False)
        # get the offset relative to the start
        elif ctrl == M_XRD:
            val = YOUR_CODE_HERE
            res = (val, True)
        elif ctrl == M_XWR:
            YOUR_CODE_HERE
            # just to keep the return format consistent
            res = (WORD(0), True)
        else:
            res = (WORD(0), False)
        return res

    def dump(self):
        pass
# --------------------------------------------------------------



# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Stats Structure
# Implement the metrics
# For the ratio, multiply by 100.0 to get the percentage for printing
class STATS(object):
    # !!!DO NOT MODIFY!!!
    cycle           = 0         # number of CPU cycles
    icount          = 0         # number of instructions executed

    inst_alu        = 0         # number of ALU instructions
    inst_mem        = 0         # number of load/store instructions
    inst_ctrl       = 0         # number of control transfer instructions

    @staticmethod
    def print_stats():
        cpi = YOUR_CODE_HERE
        alu_ratio =  YOUR_CODE_HERE
        data_ratio = YOUR_CODE_HERE
        ctrl_ratio = YOUR_CODE_HERE

        # !!!DO NOT MODIFY!!!
        print("%d instructions executed in %d cycles. CPI = %.3f" % (STATS.icount, STATS.cycle, cpi))
        print("Data transfer:    %d instructions (%.2f%%)" % (STATS.inst_mem, data_ratio))
        print("ALU operation:    %d instructions (%.2f%%)" % (STATS.inst_alu, alu_ratio))
        print("Control transfer: %d instructions (%.2f%%)" % (STATS.inst_ctrl, ctrl_ratio))
# --------------------------------------------------------------


