Week 3 – Challenge 10

Aim:
To identify the bottlenecks in a Q-learning algorithm and propose a hardware acceleration strategy using SystemVerilog.

Problems I Faced:
- Originally didn’t have a good performance baseline.
- Wrote Verilog code (q_accelerator.sv) before doing proper software profiling.
- Was unsure if Q-value update is the best target for hardware.

Final Outcome:
- Used performance analysis to identify Q-update as a bottleneck.
- Designed a SystemVerilog accelerator to offload Q-value update computation.
- Planned for Python and Verilog co-simulation.

What I Learned:
- Hardware/software partitioning should follow empirical evidence, not assumptions.
- Simple arithmetic operations can be bottlenecks and candidates for hardware.
- It’s essential to simulate and validate correctness before synthesis.


