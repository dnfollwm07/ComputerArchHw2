from definitions import *
from isa_encodings import *

# an general instruction structure
class INSTRUCTION(object):
    @staticmethod
    def get_opcode(inst):
        for k, v in rv32i_t.items():
            # --------------------------------------------------------------
            # TASK--IMPLEMENTATION NEEDED
            # Guide:
            #  0. Will return k if it matches the inst 
            #  1. which field of rv32i_t decides which instruction it is?
            #  2. check the definitions.py, somewhere you can find this filed
            #  3. inst is exact the binary string of an instruction
            #  4. why we defined mask in isa_encodings.py
            #  5. 4~5 lines are enough to implement this
            YOUR_CODE_HERE
            # --------------------------------------------------------------
        return ILLEAGAL
    
    @staticmethod
    def get_opcode_str(opcode):
        return rv32i_t[opcode][IN_NAME]
    
    # --------------------------------------------------------------
    # TASK--IMPLEMENTATION NEEDED
    # Guide:
    #  1. check the definitions.py, you defined the mask and shift
    #  2. Be caerful with the bit operation order
    @staticmethod
    def get_rs1(inst):
        return YOUR_CODE_HERE
    
    @staticmethod
    def get_rs2(inst):
        return YOUR_CODE_HERE
    
    @staticmethod
    def get_rd(inst):
        return YOUR_CODE_HERE
    # --------------------------------------------------------------
    
    # n_bits is the number of bits of the immediate value
    @staticmethod
    def get_sign_extend(val, n_bits):
        sign_bit = val >> (n_bits - 1)
        if sign_bit:
            # --------------------------------------------------------------
            # TASK--IMPLEMENTATION NEEDED
            # Guide:
            #  1. bit operation is needed
            #  2. (1 << x) -1 will generate a binary string with x 1s
            #  3. 3 lines are enough
            YOUR_CODE_HERE
            # --------------------------------------------------------------
        else:
            return val
    
    @staticmethod
    def get_imm_i(inst):
        imm = (inst >> 20) & 0xfff
        return INSTRUCTION.get_sign_extend(imm, 12)
    
    @staticmethod
    def get_imm_u(inst):
        imm = inst & 0xfffff000
        return imm
    
    @staticmethod
    def get_imm_s(inst):
        imm_11_5 = (inst >> 25) & 0x7f
        imm_4_0 = (inst >> 7) & 0x1f
        imm = (imm_11_5 << 5) | imm_4_0
        return INSTRUCTION.get_sign_extend(imm, 12)
    
    # --------------------------------------------------------------
    # TASK--IMPLEMENTATION NEEDED
    # Guide:
    #  1. check ref [1], how B-type immediate value is encoded
    #  2. check other get_imm_x functions, see how they are implemented
    #  3. imm_12 means the 12th bit and imm_10_5 means the 10th to 5th bits
    #  4. make sure the imm_x are in the correct bit length
    @staticmethod
    def get_imm_b(inst):
        imm_12 = YOUR_CODE_HERE
        imm_11 = YOUR_CODE_HERE
        imm_10_5 = YOUR_CODE_HERE
        imm_1_4 = YOUR_CODE_HERE
        imm = (imm_12 | imm_11 | imm_10_5 | imm_1_4) << 1
        return INSTRUCTION.get_sign_extend(imm, 13)
    # --------------------------------------------------------------
    
    
    @staticmethod
    def get_imm_j(inst):
        imm_20 = (inst >> 31) << 19
        imm_19_12 = ((inst >> 12) & 0xff) << 11
        imm_11 = ((inst >> 20) & 0x1) << 10
        imm_10_1 = (inst >> 21) & 0x3ff
        imm = (imm_20 | imm_19_12 | imm_11 | imm_10_1) << 1
        return INSTRUCTION.get_sign_extend(imm, 21)
