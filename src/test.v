`default_nettype none
`timescale 1ns/1ps

  module test
  (
   input [7:0]  io_in,
   output [7:0] io_out,
   output [1:0] ext_out
  );

   grey m_grey( io_in, io_out, ext_out );

endmodule
