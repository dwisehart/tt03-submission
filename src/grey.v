`default_nettype none

module dwisehart_top #( parameter MAX_COUNT = 1000 )
(
 input [7:0]  io_in,
 output [7:0] io_out
);

   wire       i_clk        = io_in[0];
   wire       i_rst        = io_in[1];
   wire [5:0] i_unused     = io_in[7:2];
   reg [4:0]  r_ones;
   assign     io_out[4:0]  = r_ones;
   reg [4:0]  r_tens;
   assign     io_out[7:5]  = r_tens[2:0];

   always @( posedge i_clk )
     if( i_rst ) begin
        r_ones          <= 'd0;
        r_tens          <= 'd0;
     end
     else if( r_ones == 'b10000 ) begin
        r_tens          <= f_grey( r_tens );
        r_ones          <= 'd0;
     end
     else begin
        r_tens          <= r_tens;
        r_ones          <= f_grey( r_ones );
     end

   function [4:0] f_grey( input [4:0] f_in );
      case( f_in )
        'b00000: return 'b00001;  // 0
        'b00001: return 'b00011;  // 1
        'b00011: return 'b00010;  // 2
        'b00010: return 'b00110;  // 3
        'b00110: return 'b00100;  // 4
        'b00100: return 'b01100;  // 5
        'b01100: return 'b01000;  // 6
        'b01000: return 'b11000;  // 7
        'b11000: return 'b10000;  // 8
        default: return 'b00000;  // 9 or anything else
      endcase
   endfunction

endmodule
