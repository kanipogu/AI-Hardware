import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
import numpy as np

@cocotb.test()
async def test_threshold(dut):
    dut._log.info("Starting threshold test...")

    # Start a 10ns period clock on dut.clk
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Load pixel data
    pixel_data = np.loadtxt("verilog/input_pixels.txt", dtype=np.uint8)
    results = []

    for pix in pixel_data:
        dut.pixel_in.value = int(pix)
        await RisingEdge(dut.clk)

        # Handle 'X' values safely
        val = dut.binary_out.value
        if val.is_resolvable:
            results.append(int(val))
        else:
            dut._log.warning("Unresolvable value at pixel: writing 0")
            results.append(0)

    # Save hardware output
    np.savetxt("verilog/verilog_output.txt", results, fmt="%d")
    dut._log.info("Simulation complete. Output saved to verilog_output.txt.")

