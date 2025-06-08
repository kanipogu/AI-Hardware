module threshold(
    input wire clk,
    input wire [7:0] pixel_in,
    output reg binary_out
);

initial begin
    binary_out = 0;  // Ensure known startup state
end

always @(posedge clk) begin
    // Default to 0 every cycle to prevent latch/inferred 'x'
    binary_out <= 0;

    // Simple threshold logic: pixel > 127 ⇒ white (1)
    if (pixel_in > 8'd127)
        binary_out <= 1;
end

endmodule
