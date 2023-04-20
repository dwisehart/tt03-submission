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

   localparam pZERO        = 'b10001;
   localparam pONE         = 'b00001;
   localparam pTWO         = 'b00011;
   localparam pTHREE       = 'b00010;
   localparam pFOUR        = 'b00110;
   localparam pFIVE        = 'b00100;
   localparam pSIX         = 'b01100;
   localparam pSEVEN       = 'b01000;
   localparam pEIGHT       = 'b11000;
   localparam pNINE        = 'b10000;

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
        r_hunB          <= f_init_grey( init[59:55] );
        r_tenB          <= f_init_grey( init[54:50] );
        r_bil           <= f_init_grey( init[49:45] );
        r_hunM          <= f_init_grey( init[44:40] );
        r_tenM          <= f_init_grey( init[39:35] );
        r_mil           <= f_init_grey( init[34:30] );
        r_hunT          <= f_init_grey( init[29:25] );
        r_tenT          <= f_init_grey( init[24:20] );
        r_thou          <= f_init_grey( init[19:15] );
        r_hund          <= f_init_grey( init[14:10] );
        r_tens          <= f_init_grey(   init[9:5] );
        r_ones          <= f_init_grey(   init[4:0] );
     end
     else
       casex({                  r_tenB == pNINE,  r_bil == pNINE,
               r_hunM == pNINE, r_tenM == pNINE,  r_mil == pNINE,
               r_hunT == pNINE, r_tenT == pNINE, r_thou == pNINE,
               r_hund == pNINE, r_tens == pNINE, r_ones == pNINE })
         'b11_111_111_111: begin
            r_hunB      <= f_grey( r_hunB );
            r_tenB      <= pZERO;
            r_bil       <= pZERO;
            r_hunM      <= pZERO;
            r_tenM      <= pZERO;
            r_mil       <= pZERO;
            r_hunT      <= pZERO;
            r_tenT      <= pZERO;
            r_thou      <= pZERO;
            r_hund      <= pZERO;
            r_tens      <= pZERO;
            r_ones      <= pZERO;
         end
         'b01_111_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= f_grey( r_tenB );
            r_bil       <= pZERO;
            r_hunM      <= pZERO;
            r_tenM      <= pZERO;
            r_mil       <= pZERO;
            r_hunT      <= pZERO;
            r_tenT      <= pZERO;
            r_thou      <= pZERO;
            r_hund      <= pZERO;
            r_tens      <= pZERO;
            r_ones      <= pZERO;
         end
         'bX0_111_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= f_grey( r_mil );
            r_hunM      <= pZERO;
            r_tenM      <= pZERO;
            r_mil       <= pZERO;
            r_hunT      <= pZERO;
            r_tenT      <= pZERO;
            r_thou      <= pZERO;
            r_hund      <= pZERO;
            r_tens      <= pZERO;
            r_ones      <= pZERO;
         end
         'bXX_011_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
            r_hunM      <= f_grey( r_hunM );
            r_tenM      <= pZERO;
            r_mil       <= pZERO;
            r_hunT      <= pZERO;
            r_tenT      <= pZERO;
            r_thou      <= pZERO;
            r_hund      <= pZERO;
            r_tens      <= pZERO;
            r_ones      <= pZERO;
         end
         'bXX_X01_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
            r_hunM      <= r_hunM;
            r_tenM      <= f_grey( r_tenM );
            r_mil       <= pZERO;
            r_hunT      <= pZERO;
            r_tenT      <= pZERO;
            r_thou      <= pZERO;
            r_hund      <= pZERO;
            r_tens      <= pZERO;
            r_ones      <= pZERO;
         end
         'bXX_XX0_111_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
            r_hunM      <= r_hunM;
            r_tenM      <= r_tenM;
            r_mil       <= f_grey( r_mil );
            r_hunT      <= pZERO;
            r_tenT      <= pZERO;
            r_thou      <= pZERO;
            r_hund      <= pZERO;
            r_tens      <= pZERO;
            r_ones      <= pZERO;
         end
         'bXX_XXX_011_111: begin
            r_hunB      <= r_hunB;
            r_tenB      <= r_tenB;
            r_bil       <= r_bil;
            r_hunM      <= r_hunM;
            r_tenM      <= r_tenM;
            r_mil       <= r_mil;
            r_hunT      <= f_grey( r_hunT );
            r_tenT      <= pZERO;
            r_thou      <= pZERO;
            r_hund      <= pZERO;
            r_tens      <= pZERO;
            r_ones      <= pZERO;
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
            r_thou      <= pZERO;
            r_hund      <= pZERO;
            r_tens      <= pZERO;
            r_ones      <= pZERO;
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
            r_hund      <= pZERO;
            r_tens      <= pZERO;
            r_ones      <= pZERO;
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
            r_tens      <= pZERO;
            r_ones      <= pZERO;
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
            r_ones      <= pZERO;
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
        pZERO:   f_grey  = pONE;
        pONE:    f_grey  = pTWO;
        pTWO:    f_grey  = pTHREE;
        pTHREE:  f_grey  = pFOUR;
        pFOUR:   f_grey  = pFIVE;
        pFIVE:   f_grey  = pSIX;
        pSIX:    f_grey  = pSEVEN;
        pSEVEN:  f_grey  = pEIGHT;
        pEIGHT:  f_grey  = pNINE;
        default: f_grey  = pZERO;
      endcase
   endfunction

////////////////////////////////////////
   function [4:0] f_init_grey( input [4:0] f_in );
      case( f_in )
        pZERO:   f_init_grey  = pZERO;
        pONE:    f_init_grey  = pONE;
        pTWO:    f_init_grey  = pTWO;
        pTHREE:  f_init_grey  = pTHREE;
        pFOUR:   f_init_grey  = pFOUR;
        pFIVE:   f_init_grey  = pFIVE;
        pSIX:    f_init_grey  = pSIX;
        pSEVEN:  f_init_grey  = pSEVEN;
        pEIGHT:  f_init_grey  = pEIGHT;
        pNINE:   f_init_grey  = pNINE;
        default: f_init_grey  = pZERO;
      endcase
   endfunction

//////////////////////////////////////////////////
   wire       w_zero        = ( r_hunB == pZERO &&
                                r_tenB == pZERO &&
                                r_bil  == pZERO &&
                                r_hunM == pZERO &&
                                r_tenM == pZERO &&
                                r_mil  == pZERO &&
                                r_hunT == pZERO &&
                                r_tenT == pZERO &&
                                r_thou == pZERO &&
                                r_hund == pZERO &&
                                r_tens == pZERO &&
                                r_ones == pZERO );
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
