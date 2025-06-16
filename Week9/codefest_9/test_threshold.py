import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer, ReadOnly
import numpy as np

@cocotb.test()
async def test_threshold(dut):
    # Start 100 MHz clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    dut._log.info("Starting threshold test...")

    # Generate test inputs
    np.random.seed(42)
    num_pixels = 1000
    threshold_val = 128
    input_pixels = np.random.randint(0, 256, num_pixels, dtype=np.uint8)

    # Golden reference model
    golden = (input_pixels > threshold_val).astype(np.uint8)

    # Set threshold input once
    await RisingEdge(dut.clk)
    dut.threshold.value = threshold_val

    mismatches = 0

    for i, pixel in enumerate(input_pixels):
        # Apply input just after clock edge
        await RisingEdge(dut.clk)
        dut.pixel_in.value = int(pixel)

        # Wait one clock cycle for output to settle
        await RisingEdge(dut.clk)
        await ReadOnly()

        # Compare hardware output with golden model
        hw_val = dut.binary_out.value.integer
        expected = int(golden[i])

        if hw_val != expected:
            mismatches += 1
            dut._log.warning(f"[Mismatch] Index={i}, Pixel={pixel}, Expected={expected}, Got={hw_val}")

    # Log final results
    dut._log.info(f"[COVERAGE] Below: {(input_pixels < threshold_val).sum()}, Equal: {(input_pixels == threshold_val).sum()}, Above: {(input_pixels > threshold_val).sum()}")
    dut._log.info(f"[VERIFY] Mismatches vs golden model: {mismatches}")

    # Assertion
    assert mismatches == 0, f"[FAIL] Run had {mismatches} mismatches!"
    await Timer(2, units="us")



