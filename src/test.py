import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

@cocotb.test()
async def test_my_design( dut ):
    dut._log.info( "start" )
    clock = Clock( dut.CLK, 10, units="ns" )
    cocotb.start_soon( clock.start() )

    dut.RST.value = 1
    await ClockCycles( dut.CLK, 10 )
    dut.RST.value = 0

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b00000

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b00001

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b00011
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b00011
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b00011
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b00011
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b00011
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b00011
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b00011
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b00011
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b00011
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b00011

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b00010
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b00010
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b00010
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b00010
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b00010
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b00010
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b00010
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b00010
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b00010
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b00010

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b00110
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b00110
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b00110
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b00110
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b00110
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b00110
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b00110
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b00110
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b00110
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b00110

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b00100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b00100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b00100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b00100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b00100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b00100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b00100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b00100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b00100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b00100

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b01100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b01100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b01100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b01100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b01100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b01100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b01100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b01100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b01100
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b01100

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b01000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b01000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b01000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b01000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b01000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b01000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b01000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b01000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b01000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b01000

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b11000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b11000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b11000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b11000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b11000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b11000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b11000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b11000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b11000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b11000

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b10000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b10000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b10000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b10000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b10000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b10000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b10000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b10000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b10000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b10000

    # Start over

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b00000
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b00000

    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00000
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00001
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00011
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00010
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00110
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b00100
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01100
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b01000
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b11000
    assert int( dut.TENS.value ) == 0b00001
    await ClockCycles( dut.CLK, 1 )
    assert int( dut.ONES.value ) == 0b10000
    assert int( dut.TENS.value ) == 0b00001

