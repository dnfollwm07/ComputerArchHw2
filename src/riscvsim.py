from definitions import *
from structure import *




class RISCVSIM(object):

    # --------------------------------------------------------------
    # TASK--IMPLEMENTATION NEEDED
    # Guide:
    # Check the structure.py and definitions.py
    # Only 1 line is needed for each variable
    def __init__(self):
        # progam counter is a register
        self.pc = YOUR_CODE_HERE
        # register files
        self.rf = YOUR_CODE_HERE
        # instruction memory
        self.imem = YOUR_CODE_HERE
        # data memory
        self.dmem = YOUR_CODE_HERE
    # --------------------------------------------------------------
    

    def run(self, entry_point):
        SIMULATOR.run(self, entry_point)


class SIMULATOR(object):
    # simulator will work as the riscv platform
    @staticmethod
    def run(simulator:RISCVSIM, entry_point):
        SIMULATOR.core = simulator

        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part A
        # Guide:
        # Set the program counter
        # Check where is the register binds to
        # Only 1 line is needed
        YOUR_CODE_HERE
        # --------------------------------------------------------------

        while True:
            status = SIMULATOR.cycle()

            # --------------------------------------------------------------
            # TASK--IMPLEMENTATION NEEDED
            # Part A
            # Guide:
            # update the stats, you used it in Task 2
            # update cycle and instruction count here
            # 2 lines are enough
            YOUR_CODE_HERE
            # --------------------------------------------------------------

            if not status == EXC_NONE:
                pc = SIMULATOR.core.pc.read()
                if status == EXC_EBREAK:
                    print("[ebreak] Stop Simulation")
                else:
                    print("Exception at 0x%08x: " % pc)
                    print(EXC_MSG[status])
                break
            
        # deal with the exceptions if any
        print("Simulation Finished")
        
        SIMULATOR.core.rf.dump()

        

        
    # return status
    @staticmethod
    def cycle():
        
        pc, inst, status = SIMULATOR.IF()
        
        # Exception: instruction memory error 
        if status == False:
            return EXC_IMEM_ERROR

        opcode, isa_info = SIMULATOR.ID(inst)

        # Exception: illegal instruction encoding
        if opcode == EXC_ILLEGAL_INST:
            return EXC_ILLEGAL_INST  
        
        status = SIMULATOR.EX(pc, inst, opcode, isa_info)
        
        SIMULATOR.MEM()
        
        SIMULATOR.WB()

        return status

    @staticmethod
    def alu_fn(pc, inst, opcode, isa_info):
        np.seterr(all='ignore')



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  update the stats, you used it in Task 2
        YOUR_CODE_HERE
        # --------------------------------------------------------------



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   prepare all the operands
        #   check rv32i.py

        # get register index
        rs1 = YOUR_CODE_HERE
        rs2 = YOUR_CODE_HERE
        rd = YOUR_CODE_HERE

        # get register values
        rs1_val = YOUR_CODE_HERE
        rs2_val = YOUR_CODE_HERE

        # get immediate values
        imm_i = YOUR_CODE_HERE
        imm_u = YOUR_CODE_HERE
        # --------------------------------------------------------------
            
        # decide the operand 1
        # check the IN_ALU1 options
        op_1 = None
        if isa_info[IN_ALU1] == OP1_RS1:
            op_1 = rs1_val
        elif isa_info[IN_ALU1] == OP1_PC:
            op_1 = pc
        else:
            op_1 = WORD(0)

        # decide the operand 2
        # check the IN_ALU2 options
        op_2 = None
        if isa_info[IN_ALU2] == OP2_RS2:
            op_2 = rs2_val
        elif isa_info[IN_ALU2] == OP2_IMI:
            op_2 = imm_i
        elif isa_info[IN_ALU2] == OP2_IMU:
            op_2 = imm_u
        else:
            op_2 = WORD(0)
        


        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   0. decide the output based on the op_1 and op_2
        #   1. check the IN_OP options
        #   2. check ref [2]
        #   3. each case can be done in 1~2 lines
        out = None
        if isa_info[IN_OP] == ALU_ADD:
            YOUR_CODE_HERE
        elif isa_info[IN_OP] == ALU_SUB:
            YOUR_CODE_HERE
        elif isa_info[IN_OP] == ALU_MUL:
            out = (op_1 * op_2) & 0xffffffff
        elif isa_info[IN_OP] == ALU_MULHU:
            out = ((WORD(op_1) * WORD(op_2)) >> 32) & 0xffffffff
        elif isa_info[IN_OP] == ALU_AND:
            YOUR_CODE_HERE
        elif isa_info[IN_OP] == ALU_OR:
            YOUR_CODE_HERE
        elif isa_info[IN_OP] == ALU_XOR:
            YOUR_CODE_HERE
        elif isa_info[IN_OP] == ALU_SLT:
            # set less than (signed)
            YOUR_CODE_HERE
        elif isa_info[IN_OP] == ALU_SLTU:
            # set less than (unsigned)
            YOUR_CODE_HERE
        elif isa_info[IN_OP] == ALU_SLL:
            YOUR_CODE_HERE
        elif isa_info[IN_OP] == ALU_SRA:
            YOUR_CODE_HERE
        elif isa_info[IN_OP] == ALU_SRL:
            YOUR_CODE_HERE
        else:
            out = WORD(0)
        # --------------------------------------------------------------



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   set the pc to the next instruction
        #   2 lines are enough
        YOUR_CODE_HERE
        # --------------------------------------------------------------



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   Commit results
        #   1 line is enough
        YOUR_CODE_HERE
        # --------------------------------------------------------------
        return EXC_NONE

    
    @staticmethod
    def mem_fn(pc, inst, opcode, isa_info):

        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  update the stats, you used it in Task 2
        YOUR_CODE_HERE
        # --------------------------------------------------------------



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  1. prepare the operands
        #  2. notice that imm will be treated as signed
        rs1 = YOUR_CODE_HERE
        rs1_val = YOUR_CODE_HERE
        # LOAD 
        if isa_info[IN_OP] == MEM_LD:

            # lw rd, rs1, imm
            rd = YOUR_CODE_HERE
            imm_i = YOUR_CODE_HERE
            addr = YOUR_CODE_HERE
            # read from memory
            data, status = YOUR_CODE_HERE


            if status:
                # write to destination
                YOUR_CODE_HERE
            else:
                print("Exception at 0x%08x: " % pc, end="")
                print(EXC_MSG[EXC_DMEM_ERROR])
                return EXC_DMEM_ERROR
        else: # STORE
            
            # sw rs1, rs2, imm
            rs2 = YOUR_CODE_HERE
            rs2_val = YOUR_CODE_HERE
            imm_s  = YOUR_CODE_HERE
            addr = YOUR_CODE_HERE
            # write to memory
            data, status = YOUR_CODE_HERE
            
            # Exception: data memory error
            if not status:
                print("Exception at 0x%08x: " % pc, end="")
                print(EXC_MSG[EXC_DMEM_ERROR])
                return EXC_DMEM_ERROR
        # --------------------------------------------------------------
    


        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  set the pc to the next instruction
        #  2 lines are enough
        YOUR_CODE_HERE
        # --------------------------------------------------------------



        return EXC_NONE

    
    @staticmethod
    def ctrl_fn(pc, inst, opcode, isa_info):


        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   set the pc
        #   2 lines are enough
        YOUR_CODE_HERE
        # --------------------------------------------------------------



        # for now ebreak will stop simulation
        # ecall is os syscall, not implemented now
        # Exception: ebreak
        if inst == EBREAK or inst == ECALL:
            return EXC_EBREAK
        


        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  prepare the operands
        #  check rv32i.py
        rs1 = YOUR_CODE_HERE
        rs2 = YOUR_CODE_HERE

        # used by jal and jalr to store the return address
        rd = YOUR_CODE_HERE

        rs1_val = YOUR_CODE_HERE
        rs2_val = YOUR_CODE_HERE

        imm_i = YOUR_CODE_HERE
        imm_j = YOUR_CODE_HERE
        imm_b = YOUR_CODE_HERE
        # --------------------------------------------------------------



        # the return address for jal and jalr
        pc_prepare = pc + 4

        
        
        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   check ref [2]
        #   notice the sign or unsigned when comparing the values
        #   decide the next pc in each case
        pc_next = None
        if opcode == JAL:
            YOUR_CODE_HERE
        elif opcode == BEQ:
            YOUR_CODE_HERE
        elif opcode == BNE:
            YOUR_CODE_HERE
        elif opcode == BLT:
            # signed
            YOUR_CODE_HERE
        elif opcode == BGE:
            # signed
            YOUR_CODE_HERE
        elif opcode == BLTU: 
            # unsigned
            YOUR_CODE_HERE
        elif opcode == BGEU: 
            # unsigned
            YOUR_CODE_HERE
        elif opcode == JALR:
            YOUR_CODE_HERE
        else:
            pc_next = pc_prepare

        if opcode == JAL or opcode == JALR:
            # a register is changed
            # 1 line is enough
            YOUR_CODE_HERE
        # --------------------------------------------------------------

        # pc_next is has been decided
        # Update PC
        SIMULATOR.core.pc.write(pc_next)
        return EXC_NONE
    
    @staticmethod
    def IF():
        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part A
        # Guide:
        #  1. get the pc
        #  2. access the instruction memory, valid is True
        pc = YOUR_CODE_HERE
        inst, status = YOUR_CODE_HERE
        # --------------------------------------------------------------

        # Exception: instruction memory error
        if not status:
            print("Exception at 0x%08x: " % pc, end="")
            return EXC_IMEM_ERROR, 0
        return pc,inst,status

    @staticmethod
    def ID(inst):
        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part A
        # Guide:
        #  1. get the opcode
        #  2. get the isa info though the opcode
        #  3. we defined all isa info in isa_encodings.py
        opcode = YOUR_CODE_HERE

        # Exception: illegal instruction
        if opcode == ILLEAGAL:
            return EXC_ILLEGAL_INST,None
        
        isa_info = YOUR_CODE_HERE
        return opcode,isa_info
        # ------------------------------------------------------------


    @staticmethod
    def EX(pc, inst, opcode, isa_info):
        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  1. assume the function units (alu, mem, ctrl) are implemented
        #  2. decide which function unit to issue
        #  3. each function unit will return a status and EX will also return it
        #  4. check the definitions.py [Which function unit to use]
        #  5. 6 lines are enough
        YOUR_CODE_HERE
        # --------------------------------------------------------------


    # --------------------------------------------------------------
    # !!!DO NOT MODIFY!!!
    # We dont need to implement these functions in this task
    @staticmethod
    def MEM():
        pass

    @staticmethod
    def WB():
        pass
    # --------------------------------------------------------------


@staticmethod
def helper_dis(pc,inst):
    from parser import PROGRAM
    decode = PROGRAM.disassemble(pc,inst)
    print(decode)