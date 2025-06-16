export WAVEFORM_FORMAT=VCD
SIM ?= questa
TOPLEVEL_LANG = verilog
VERILOG_SOURCES = threshold.v
TOPLEVEL = threshold
MODULE = test_threshold

include $(shell cocotb-config --makefiles)/Makefile.sim

# ? Regression test rule ? tabs are mandatory here!
regress:
	@echo "[INFO] Running regression test via Cocotb"
	mkdir -p verilog
	make SIM=$(SIM) TOPLEVEL=$(TOPLEVEL) MODULE=$(MODULE)

