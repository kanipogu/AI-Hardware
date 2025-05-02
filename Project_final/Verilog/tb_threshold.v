`timescale 1ns/1ps
module tb;

    // Signals
    reg clk;
    reg [7:0] pixel_in;
    reg [7:0] threshold;
    wire binary_out;

    // Instantiate the threshold module
    threshold uut (
        .clk(clk),
        .pixel_in(pixel_in),
        .threshold(threshold),
        .binary_out(binary_out)
    );

    // Variables
    integer i;
    integer file;
    integer status;              // For fscanf
    reg [7:0] pixels [0:4095];   // 128x32 = 4096 pixels

    // Clock generation
    always #5 clk = ~clk;

    initial begin
        clk = 0;
        threshold = 127; // Set threshold level

        // Open file
        file = $fopen("input_pixels.txt", "r");

        // Check if file opened
        if (file == 0) begin
            $display("ERROR: Cannot open input_pixels.txt");
            $finish;
        end

        // Read 4096 pixels
        for (i = 0; i < 4096; i = i + 1) begin
            status = $fscanf(file, "%d\n", pixels[i]);
        end
        $fclose(file);

        // Apply each pixel to threshold module
        for (i = 0; i < 4096; i = i + 1) begin
            pixel_in = pixels[i];
            #10; // Wait for clock posedge and binary_out result
            $display("%d", binary_out);
        end

        $finish;
    end
endmodule
