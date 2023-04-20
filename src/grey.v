`default_nettype none
`timescale 1ns/1ps

  module grey
  (
   input [7:0]  io_in,
   input [59:0] init,
   output [4:0] hunB, tenB, bil,
                hunM, tenM, mil,
                hunT, tenT, thou,
                hund, tens, ones,
   output [7:0] io_out
  );

   wire       i_clk        = io_in[0];
   wire       i_rst        = io_in[1];

////////////////////////////////////////
   reg [4:0]  r_ones, r_tens, r_hund, r_thou,
              r_tenT, r_hunT, r_thouT,
              r_mil, r_tenM, r_hunM,
              r_bil, r_tenB, r_hunB;

   assign     hunB         = r_hunB;
   assign     tenB         = r_tenB;
   assign     bil          = r_bil;
   assign     hunM         = r_hunM;
   assign     tenM         = r_tenM;
   assign     mil          = r_mil;
   assign     hunT         = r_hunT;
   assign     tenT         = r_tenT;
   assign     thou         = r_thou;
   assign     hund         = r_hund;
   assign     tens         = r_tens;
   assign     ones         = r_ones;

   always @( posedge i_clk )
     if( i_rst ) begin
        r_hunB          <= init[59:55];
        r_tenB          <= init[54:50];
        r_bil           <= init[49:45];
        r_hunM          <= init[44:40];
        r_tenM          <= init[39:35];
        r_mil           <= init[34:30];
        r_hunT          <= init[29:25];
        r_tenT          <= init[24:20];
        r_thou          <= init[19:15];
        r_hund          <= init[14:10];
        r_tens          <= init[9:5];
        r_ones          <= init[4:0];
     end
     else
       casex({                    r_tenB == 'b10000, r_bil == 'b10000,
               r_hunM == 'b10000, r_tenM == 'b10000, r_mil == 'b10000,
               r_hunT == 'b10000, r_tenT == 'b10000, r_thou == 'b10000,
               r_hund == 'b10000, r_tens == 'b10000, r_ones == 'b10000 })
         'b11_111_111_111: begin
            r_hunB      <= f_grey( r_hunB );
            r_tenB      <= 'd0;
            r_bil       <= 'd0;
            r_hunM      <= 'd0;
            r_tenM      <= 'd0;
            r_mil       <= 'd0;
            r_hunT      <= 'd0;
            r_tenT      <= 'd0;
            r_thou      <= 'd0;
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'b01_111_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= f_grey( r_tenB );
            r_bil       <= 'd0;
            r_hunM      <= 'd0;
            r_tenM      <= 'd0;
            r_mil       <= 'd0;
            r_hunT      <= 'd0;
            r_tenT      <= 'd0;
            r_thou      <= 'd0;
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'bX0_111_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= f_grey( r_mil );
            r_hunM      <= 'd0;
            r_tenM      <= 'd0;
            r_mil       <= 'd0;
            r_hunT      <= 'd0;
            r_tenT      <= 'd0;
            r_thou      <= 'd0;
            r_hund      <= 'd0;
            r_tens      <= 'd0;
            r_ones      <= 'd0;
         end
         'bXX_011_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
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
         'bXX_X01_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
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
         'bXX_XX0_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
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
         'bXX_XXX_011_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
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
         'bXX_XXX_X01_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
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
         'bXX_XXX_XX0_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
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
         'bXX_XXX_XXX_011: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
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
         'bXX_XXX_XXX_X01: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
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
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
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

//////////////////////////////////////////////////
   wire       w_zero        = ( r_hunB == 'd0 &&
                                r_tenB == 'd0 &&
                                r_bil  == 'd0 &&
                                r_hunM == 'd0 &&
                                r_tenM == 'd0 &&
                                r_mil  == 'd0 &&
                                r_hunT == 'd0 &&
                                r_tenT == 'd0 &&
                                r_thou == 'd0 &&
                                r_hund == 'd0 &&
                                r_tens == 'd0 &&
                                r_ones == 'd0 );
   reg        r_clk, r_zero;

   always @( posedge i_clk )
     if( i_rst ) begin
        r_clk              <= 'b0;
        r_zero             <= 'b0;
     end
     else begin
        r_clk              <= ~ r_clk;
        r_zero             <= w_zero;
     end

////////////////////////////////////////
   wire [5:0] i_sel         = io_in[7:2];
   reg [7:0]  r_out;
   assign     io_out        = r_out;

   always @( posedge i_clk )
     if( i_rst )
       r_out               <= 'd0;
     else
       case( i_sel )
         'b0001_01: r_out  <= { w_zero,      r_hunB, r_tenB[5:4] };
         'b0001_10: r_out  <= { r_hunB[0],   r_tenB, r_bil[5:4] };
         'b0001_11: r_out  <= { r_tenB[0],   r_bil,  r_hunM[5:4] };
         'b0010_01: r_out  <= { r_bil[0],    r_hunM, r_tenM[5:4] };
         'b0010_10: r_out  <= { r_hunM[0],   r_tenM, r_mil[5:4] };
         'b0010_11: r_out  <= { r_tenM[0],   r_mil,  r_hunT[5:4] };
         'b0100_01: r_out  <= { r_mil[0],    r_hunT, r_tenT[5:4] };
         'b0100_10: r_out  <= { r_hunT[0],   r_tenT, r_thou[5:4] };
         'b0100_11: r_out  <= { r_tenT[0],   r_thou, r_hund[5:4] };
         'b1000_01: r_out  <= { r_thou[0],   r_hund, r_tens[5:4] };
         'b1000_10: r_out  <= { r_hund[0],   r_tens, r_ones[5:4] };
         default:   r_out  <= { r_tens[1:0], r_ones, r_clk };
       endcase

endmodule
