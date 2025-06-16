set target_library osu05_stdcells.db
   set link_library osu05_stdcells.db



read_verilog threshold.v
current_design threshold 
link
check_design
#set_wire_load_model -name "10x10"
#write your timing constraints here
# Define the primary clock (clk) with 10 ns period
create_clock -name clk -period 10 [get_ports clk]

# Set input delays (assume data arrives 2 ns after clk edge)
set_input_delay -clock clk 2 [get_ports pixel_in]
set_input_delay -clock clk 2 [get_ports threshold]

# Set output delay (assume output captured 2 ns after clk edge)
set_output_delay -clock clk 2 [get_ports binary_out]

# (Optional) Set false path for testbench/debug-related signals if any
# set_false_path -from [get_ports debug_signal]

compile
check_timing
report_clock
report_power > pwr.rpt
report_cell > cell.rpt
report_area > area.rpt
report_timing > timing.rpt
