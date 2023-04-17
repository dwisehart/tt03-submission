`default_nettype none
`timescale 1ns/1ps

  module tb
  (
   input        CLK,
   input        RST,
   output [4:0] ONES,
   output [4:0] TENS
  );

   initial begin
      $dumpfile ("tb.vcd");
      $dumpvars (0, tb);
      #1;
   end

   wire [7:0] inputs    = { 6'b0, RST, CLK };
   wire [7:0] outputs;
   wire [1:0] extra;
   assign     ONES      = outputs[4:0];
   assign     TENS      = { extra[1:0], outputs[7:5] };

    test m_grey (
        .io_in (inputs),
        .io_out (outputs),
        .ext_out (extra)
    );

endmodule
