`default_nettype none
`timescale 1ns/1ps

  module tb
  (
   input        CLK,
   input        RST,
   input [59:0] INIT,

   output [4:0] ONES,
   output [4:0] TENS,
   output [4:0] HUND,
   output [4:0] THOU,
   output [4:0] TEN_THOU,
   output [4:0] HUN_THOU,
   output [4:0] MIL,
   output [4:0] TEN_MIL,
   output [4:0] HUN_MIL
   output [4:0] BIL,
   output [4:0] TEN_BIL,
   output [4:0] HUN_BIL
  );

   initial begin
      $dumpfile ("tb.vcd");
      $dumpvars (0, tb);
      #1;
   end

    test m_test
    (
     .io_in ({ 6'b0, RST, CLK }),
     .init  ( INIT ),
     .hunB  ( HUN_BIL ),
     .tenB  ( TEN_BIL ),
     .bil   ( BIL ),
     .hunM  ( HUN_MIL ),
     .tenM  ( TEN_MIL ),
     .mil   ( MIL ),
     .hunT  ( HUN_THOU ),
     .tenT  ( TEN_THOU ),
     .thou  ( THOU ),
     .hund  ( HUND ),
     .tens  ( TENS ),
     .ones  ( ONES )
    );

endmodule
