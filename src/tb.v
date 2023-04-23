`default_nettype none
`timescale 1ns/1ps

`ifdef GL_TEST

////////////////////////////////////////
  module tb
  (
   input        CLK,
   input        N_RST,
   input [5:0]  SEL,

   output [7:0] IO_OUT
  );

   dwisehart_top m_top
   (
    .vccd1  ( 1'b1 ),
    .vssd1  ( 1'b0 ),
    .io_in  ({ SEL, ~ N_RST, CLK }),
    .io_out ( IO_OUT )
   );

`else

////////////////////////////////////////
  module tb
  (
   input        CLK,
   input        N_RST,
   input [7:0]  SEL,
   input [59:0] INIT,

   output [4:0] ONES,
   output [4:0] TENS,
   output [4:0] HUND,
   output [4:0] THOU,
   output [4:0] TEN_THOU,
   output [4:0] HUN_THOU,
   output [4:0] MIL,
   output [4:0] TEN_MIL,
   output [4:0] HUN_MIL,
   output [4:0] BIL,
   output [4:0] TEN_BIL,
   output [4:0] HUN_BIL,
   output [7:0] IO_OUT
  );

   initial begin
      $dumpfile ("tb.vcd");
      $dumpvars (0, tb);
      #1;
   end

   grey m_grey
   (
    .i_clk  ( CLK ),
    .i_rst  ( ~ N_RST ),
    .i_sel  ( SEL ),
    .init   ( INIT ),
    .hunB   ( HUN_BIL ),
    .tenB   ( TEN_BIL ),
    .bil    ( BIL ),
    .hunM   ( HUN_MIL ),
    .tenM   ( TEN_MIL ),
    .mil    ( MIL ),
    .hunT   ( HUN_THOU ),
    .tenT   ( TEN_THOU ),
    .thou   ( THOU ),
    .hund   ( HUND ),
    .tens   ( TENS ),
    .ones   ( ONES ),
    .o_cnt  ( IO_OUT )
   );

`endif

endmodule
