`default_nettype none
`timescale 1ns/1ps

  module grey
  (
   input [7:0]  io_in,
   output [4:0] hunM, tenM, mil,
                hunT, tenT, thou,
                hund, tens, ones
  );

   wire       i_clk        = io_in[0];
   wire       i_rst        = io_in[1];
   wire [5:0] i_unused     = io_in[7:2];

   reg [4:0]  r_ones, r_tens, r_hund, r_thou, r_tenT, r_hunT, r_thouT, r_mil, r_tenM, r_hunM, r_bil;
   assign     ones         = r_ones;
   assign     tens         = r_tens;
   assign     hund         = r_hund;
   assign     thou         = r_thou;
   assign     tenT         = r_tenT;
   assign     hunT         = r_hunT;
   assign     mil          = r_mil;
   assign     tenM         = r_tenM;
   assign     hunM         = r_hunM;

   always @( posedge i_clk )
     if( i_rst ) begin
        r_ones          <= 'd0;
        r_tens          <= 'd0;
        r_hund          <= 'd0;
        r_thou          <= 'd0;
        r_tenT          <= 'd0;
        r_hunT          <= 'd0;
        r_mil           <= 'd0;
        r_tenM          <= 'd0;
        r_hunM          <= 'd0;
     end
     else
       casex({                    r_tenM == 'b10000, r_mil == 'b10000,
               r_hunT == 'b10000, r_tenT == 'b10000, r_thou == 'b10000,
               r_hund == 'b10000, r_tens == 'b10000, r_ones == 'b10000 })
         'b11_111_111: begin
            r_hunM      <= f_grey( r_hunM );
            r_tenM      <= 'd0;
            r_mil       <= 'd0;
            r_hunT      <= 'd0;
            r_tenT      <= 'd0;
            r_thou      <= 'd0;
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'b01_111_111: begin
            r_hunM      <= r_hunM;
            r_tenM      <= f_grey( r_tenM );
            r_mil       <= 'd0;
            r_hunT      <= 'd0;
            r_tenT      <= 'd0;
            r_thou      <= 'd0;
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'bX0_111_111: begin
            r_hunM      <= r_hunM;
            r_tenM      <= r_tenM;
            r_mil       <= f_grey( r_mil );
            r_hunT      <= 'd0;
            r_tenT      <= 'd0;
            r_thou      <= 'd0;
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'bXX_011_111: begin
            r_hunM      <= r_hunM;
            r_tenM      <= r_tenM;
            r_mil       <= r_mil;
            r_hunT      <= f_grey( r_hunT );
            r_tenT      <= 'd0;
            r_thou      <= 'd0;
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'bXX_X01_111: begin
            r_hunM      <= r_hunM;
            r_tenM      <= r_tenM;
            r_mil       <= r_mil;
            r_hunT      <= r_hunT;
            r_tenT      <= f_grey( r_tenT );
            r_thou      <= 'd0;
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'bXX_XX0_111: begin
            r_hunM      <= r_hunM;
            r_tenM      <= r_tenM;
            r_mil       <= r_mil;
            r_hunT      <= r_hunT;
            r_tenT      <= r_tenT;
            r_thou      <= f_grey( r_thou );
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'bXX_XXX_011: begin
            r_hunM      <= r_hunM;
            r_tenM      <= r_tenM;
            r_mil       <= r_mil;
            r_hunT      <= r_hunT;
            r_tenT      <= r_tenT;
            r_thou      <= r_thou;
            r_hund      <= f_grey( r_hund );
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'bXX_XXX_X01: begin
            r_hunM      <= r_hunM;
            r_tenM      <= r_tenM;
            r_mil       <= r_mil;
            r_hunT      <= r_hunT;
            r_tenT      <= r_tenT;
            r_thou      <= r_thou;
            r_hund      <= r_hund;
            r_tens      <= f_grey( r_tens );
            r_ones      <= 'd0;
         end
         default: begin
            r_hunM      <= r_hunM;
            r_tenM      <= r_tenM;
            r_mil       <= r_mil;
            r_hunT      <= r_hunT;
            r_tenT      <= r_tenT;
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
