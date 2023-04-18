`default_nettype none
`timescale 1ns/1ps

  module tb
  (
   input        CLK,
   input        RST,
   output [4:0] ONES,
   output [4:0] TENS,
   output [4:0] HUND,
   output [4:0] THOU
  );

   initial begin
      $dumpfile ("tb.vcd");
      $dumpvars (0, tb);
      #1;
   end

    test m_test
    (
     .io_in ({ 6'b0, RST, CLK }),
     .thou  ( THOU ),
     .hund  ( HUND ),
     .tens  ( TENS ),
     .ones  ( ONES )
    );

endmodule
