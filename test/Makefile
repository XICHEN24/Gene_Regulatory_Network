# ----------------------------------------------------------------
# Variables setup Section                                        -
# ----------------------------------------------------------------
SCRIPT =        ../src/gene_regulatory.py
RUN_DIR =       ./run_dir
DATA_DIR =      ../data/spreadsheets
RESULTS_DIR =   $(RUN_DIR)/results
RUN_FILES_DIR = ../data/run_files

RMR =           rm -rf
GZIP =          gzip
GZIP_D =        gzip -df
MKDIR_P =       mkdir -p

.PHONY: env_setup create_run_dir copy_run_files clean_dir_recursively final_clean 

# ----------------------------------------------------------------
# Benchmarks setup Section                                       -
# ----------------------------------------------------------------
env_setup: create_run_dir copy_run_files

create_run_dir:
	$(MKDIR_P) $(RESULTS_DIR) 

copy_run_files:
	cp $(RUN_FILES_DIR)/*.yml $(RUN_DIR)

# ----------------------------------------------------------------
# Large Benchmarks RUN Section                                   -
# ----------------------------------------------------------------
run_GRN:
	python3 $(SCRIPT) -run_directory $(RUN_DIR) -run_file gene_regulatory.yml



# ----------------------------------------------------------------
# - UNIT TESTS RUN SECTION                                       -
# ----------------------------------------------------------------
unit_tests:
	cd unit; make all_unit_tests

# ----------------------------------------------------------------
# - CLEAN UP SECTION                                             -
# ----------------------------------------------------------------
final_clean: clean_dir_recursively

clean_dir_recursively:
	$(RMR) $(RUN_DIR)


