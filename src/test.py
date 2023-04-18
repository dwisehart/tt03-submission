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

    dut._log.info( "Starting at 0" )
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 10" )
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ONE
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 90" )
    await ClockCycles( dut.CLK, 71 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 100" )
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 190" )
    await ClockCycles( dut.CLK, 81 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ONE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 200" )
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == TWO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 990" )
    await ClockCycles( dut.CLK, 781 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 1,000" )
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 1,990" )
    await ClockCycles( dut.CLK, 981 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ONE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 2,000" )
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == TWO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 9,990" )
    await ClockCycles( dut.CLK, 7981 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 10,000" )
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ONE
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 99,990" )
    await ClockCycles( dut.CLK, 99990 - 10009 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 100,000" )
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == ONE
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 999,990" )
    await ClockCycles( dut.CLK, 999990 - 100009 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ZERO
    assert int( dut.HUN_THOU.value ) == NINE
    assert int( dut.TEN_THOU.value ) == NINE
    assert int( dut.THOU.value )     == NINE
    assert int( dut.HUND.value )     == NINE
    assert int( dut.TENS.value )     == NINE
    assert int( dut.ONES.value )     == NINE

    dut._log.info( "Count to 1,000,000" )
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ZERO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == ONE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == TWO
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == THREE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FOUR
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == FIVE
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SIX
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == SEVEN
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == EIGHT
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.MIL.value )      == ONE
    assert int( dut.HUN_THOU.value ) == ZERO
    assert int( dut.TEN_THOU.value ) == ZERO
    assert int( dut.THOU.value )     == ZERO
    assert int( dut.HUND.value )     == ZERO
    assert int( dut.TENS.value )     == ZERO
    assert int( dut.ONES.value )     == NINE
