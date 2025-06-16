/*module threshold(
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

endmodule*/

module threshold(
    input wire clk,
    input wire [7:0] pixel_in,
    input wire [7:0] threshold,
    output reg binary_out
);
initial begin
    $dumpfile("waveform.vcd");
    $dumpvars(1, clk);           // dump clock signal
    $dumpvars(1, pixel_in);      // input pixel
    $dumpvars(1, threshold);     // threshold register
    $dumpvars(1, binary_out);    // output
end

always @(posedge clk) begin
    binary_out <= (pixel_in > threshold) ? 1'b1 : 1'b0;
end




endmodule

