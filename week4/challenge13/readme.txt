In this assignment, 
I implemented and benchmarked the SAXPY (Single-precision A·X Plus Y) operation on the GPU using Python with the numba.cuda backend inside Google Colab.
The SAXPY operation is defined as:
y[i]=a⋅x[i]+y[i]y[i] = a \cdot x[i] + y[i]y[i]=a⋅x[i]+y[i] 
This operation was executed for varying input sizes from 21^15 to 2^25, and the GPU execution time was measured for each size.

What I Did:
•	Used numba.cuda.jit to define a custom GPU kernel for SAXPY.
•	Allocated arrays on the host and transferred them to the GPU using cuda.to_device.
•	Executed the kernel across increasing vector sizes from 32,768 to 33 million elements.
•	Measured kernel execution time using Python’s time.time() and synchronized with cuda.synchronize().
•	Plotted the execution time vs input size using matplotlib to visually interpret GPU performance.

What I Observed:
•	Execution time increased with vector size, which is expected due to the linear scaling of memory access and computation.
•	Performance was very fast for smaller sizes, and the GPU efficiently handled large vectors even at 2^25 (over 33 million elements).
•	The relationship between vector size and execution time remained mostly linear, with small fluctuations possibly due to GPU scheduling or memory latency.

What I Learned:
•	How to use GPU computing in Python with numba, which provides a powerful alternative to writing raw CUDA C/C++ code.
•	How to design a performance benchmark that helps evaluate algorithm scalability.
•	The use of Python visualization (matplotlib) to support GPU performance analysis and reporting.



