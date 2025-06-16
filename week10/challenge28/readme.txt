 Memristor Simulation - Challenge #28 (Week 10)

Objective:
The goal of this challenge was to model and simulate a memristor  using a software-based approach in Python rather than LTspice. The expected output was to visualize the characteristic I–V hysteresis loop of a memristor under an applied sinusoidal voltage input.

What I Did
1. Switched from LTspice to Python Simulation:
 Ans) Instead of using SPICE simulation with subcircuits, I implemented a memristor using code.
2. Implemented the Biolek Memristor Model:
   Ans) Used parameters like Ron, Roff, uv, device length (D), and a non-linear window function (Biolek's window function).
   - Simulated the memristor’s internal state variable `x(t)` which controls its resistance.
3. Created a Sine Wave Input:
   Ans) A 1kHz sine wave of 5V amplitude was applied as the voltage across the memristor.
4. Simulated Over Time:
    Ans) Wrote a loop to compute the memristor's dynamic resistance, current, and state evolution over 20ms.
5. Visualized the I–V Hysteresis Loop:
   Ans)Plotted the resulting current vs voltage to visualize the pinched hysteresis curve that is characteristic of a memristor.

What I Learned
The memristor is a  non-linear, state-dependent device whose resistance changes based on the history of current flow.
- The Biolek window function helps simulate boundary effects and ensures stable state transitions.
- Python is powerful  for modeling and visualization of electronic devices, especially when we want full control over equations and parameters.
- A memristor shows a pinched hysteresis loop  in I–V space, which is strongest at low frequencies and collapses as frequency increases.
- I now understand this behavior better after simulating it.

Outcome
I successfully implemented a dynamic simulation of a memristor using Python, reproduced the I–V hysteresis loop, and understood how internal physical parameters affect memristive behavior. This approach avoids SPICE complexities and allows full programmability and extension for further research.


