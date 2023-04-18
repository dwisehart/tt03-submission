`default_nettype none
`timescale 1ns/1ps

  module grey
  (
   input [7:0]  io_in,
   output [4:0] thou, hund, tens, ones
  );

   wire       i_clk        = io_in[0];
   wire       i_rst        = io_in[1];
   wire [5:0] i_unused     = io_in[7:2];

   reg [4:0]  r_ones, r_tens, r_hund, r_thou;
   assign     ones         = r_ones;
   assign     tens         = r_tens;
   assign     hund         = r_hund;
   assign     thou         = r_thou;

   always @( posedge i_clk )
     if( i_rst ) begin
        r_ones          <= 'd0;
        r_tens          <= 'd0;
        r_hund          <= 'd0;
        r_thou          <= 'd0;
     end
     else
       casex({ r_hund == 'b10000, r_tens == 'b10000, r_ones == 'b10000 })
         'b111: begin
            r_thou      <= f_grey( r_thou );
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'b011: begin
            r_thou      <= r_thou;
            r_hund      <= f_grey( r_hund );
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'bX01: begin
            r_thou      <= r_thou;
            r_hund      <= r_hund;
            r_tens      <= f_grey( r_tens );
            r_ones      <= 'd0;
         end
         default: begin
            r_thou      <= r_thou;
            r_hund      <= r_hund;
            r_tens      <= r_tens;
            r_ones      <= f_grey( r_ones );
         end
       endcase

////////////////////////////////////////
   function [4:0] f_grey( input [4:0] f_in );
      case( f_in )
        'b00000: f_grey  = 'b00001;  // 0
        'b00001: f_grey  = 'b00011;  // 1
        'b00011: f_grey  = 'b00010;  // 2
        'b00010: f_grey  = 'b00110;  // 3
        'b00110: f_grey  = 'b00100;  // 4
        'b00100: f_grey  = 'b01100;  // 5
        'b01100: f_grey  = 'b01000;  // 6
        'b01000: f_grey  = 'b11000;  // 7
        'b11000: f_grey  = 'b10000;  // 8
        default: f_grey  = 'b00000;  // 9 or anything else
      endcase
   endfunction

endmodule
