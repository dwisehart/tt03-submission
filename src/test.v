`default_nettype none
`timescale 1ns/1ps

  module test
  (
   input [7:0]  io_in,
   output [4:0] hunM, tenM, mil,
                hunT, tenT, thou,
                hund, tens, ones
  );

   grey m_grey( io_in, hunM, tenM, mil, hunT, tenT, thou, hund, tens, ones );

endmodule
