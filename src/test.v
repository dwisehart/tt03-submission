`default_nettype none
`timescale 1ns/1ps

  module test
  (
   input [7:0]  io_in,
   input [59:0] init,
   output [4:0] hunB, tenB, bil,
                hunM, tenM, mil,
                hunT, tenT, thou,
                hund, tens, ones
  );

   grey m_grey( io_in, init, hunB, tenB, bil, hunM, tenM, mil, hunT, tenT, thou, hund, tens, ones );

endmodule
