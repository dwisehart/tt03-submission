`default_nettype none
`timescale 1ns/1ps

  module dwisehart_top
  (
   input [7:0]  io_in,
   output [7:0] io_out
  );

   grey m_grey( io_in, io_out );

endmodule
