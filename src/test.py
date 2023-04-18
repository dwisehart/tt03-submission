import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

ZERO   = 0b00000
ONE    = 0b00001
TWO    = 0b00011
THREE  = 0b00010
FOUR   = 0b00110
FIVE   = 0b00100
SIX    = 0b01100
SEVEN  = 0b01000
EIGHT  = 0b11000
NINE   = 0b10000

@cocotb.test()
async def test_my_design( dut ):
    dut._log.info( "start" )
    clock = Clock( dut.CLK, 10, units="ns" )
    cocotb.start_soon( clock.start() )

    dut.RST.value = 1
    await ClockCycles( dut.CLK, 10 )
    dut.RST.value = 0

    dut.log.info( "Starting at 0000" )
    await ClockCycles( dut.CLK, 1 )               # 0000
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 0010" )
    await ClockCycles( dut.CLK, 1 )               # 0010
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ONE
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 0090" )
    await ClockCycles( dut.CLK, 71 )              # 0090
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 0100" )
    await ClockCycles( dut.CLK, 1 )               # 0100
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 0190" )
    await ClockCycles( dut.CLK, 81 )               # 0190
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ONE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 0200" )
    await ClockCycles( dut.CLK, 1 )               # 0200
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == TWO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 0990" )
    await ClockCycles( dut.CLK, 781 )               # 0990 - 0210
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 1000" )
    await ClockCycles( dut.CLK, 1 )               # 1000
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 1990" )
    await ClockCycles( dut.CLK, 981 )               # 1990
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ONE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 2000" )
    await ClockCycles( dut.CLK, 1 )               # 2000
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == TWO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Count to 9990" )
    await ClockCycles( dut.CLK, 7981 )               # 9990
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == NINE
    assert int( dut.HUND.value ) == NINE
    assert int( dut.TENS.value ) == NINE
    assert int( dut.ONES.value ) == NINE

    dut.log.info( "Rollover to 0000" )
    await ClockCycles( dut.CLK, 1 )               # 0000
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.THOU.value ) == ZERO
    assert int( dut.HUND.value ) == ZERO
    assert int( dut.TENS.value ) == ZERO
    assert int( dut.ONES.value ) == NINE
