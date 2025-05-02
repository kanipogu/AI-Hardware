module threshold #(parameter WIDTH=8)(
    input clk,
    input [WIDTH-1:0] pixel_in,
    input [WIDTH-1:0] threshold,
    output reg binary_out
);

    always @(posedge clk) begin
        if (pixel_in > threshold)
            binary_out <= 1'b1;
        else
            binary_out <= 1'b0;
    end

endmodule
