# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/student/.local/lib/python3.8/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/student/.local/lib/python3.8/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/student/catcin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/student/catcin_ws/build

# Utility rule file for _run_tests_geodesy_nosetests_tests.test_bounding_box.py.

# Include any custom commands dependencies for this target.
include hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/compiler_depend.make

# Include the progress variables for this target.
include hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/progress.make

hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py:
	cd /home/student/catcin_ws/build/hectorDroneSim/geographic_info/geodesy && ../../../catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/catkin/cmake/test/run_tests.py /home/student/catcin_ws/build/test_results/geodesy/nosetests-tests.test_bounding_box.py.xml "\"/home/student/.local/lib/python3.8/site-packages/cmake/data/bin/cmake\" -E make_directory /home/student/catcin_ws/build/test_results/geodesy" "/usr/bin/nosetests3 -P --process-timeout=60 /home/student/catcin_ws/src/hectorDroneSim/geographic_info/geodesy/tests/test_bounding_box.py --with-xunit --xunit-file=/home/student/catcin_ws/build/test_results/geodesy/nosetests-tests.test_bounding_box.py.xml"

_run_tests_geodesy_nosetests_tests.test_bounding_box.py: hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py
_run_tests_geodesy_nosetests_tests.test_bounding_box.py: hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/build.make
.PHONY : _run_tests_geodesy_nosetests_tests.test_bounding_box.py

# Rule to build all files generated by this target.
hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/build: _run_tests_geodesy_nosetests_tests.test_bounding_box.py
.PHONY : hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/build

hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/clean:
	cd /home/student/catcin_ws/build/hectorDroneSim/geographic_info/geodesy && $(CMAKE_COMMAND) -P CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/cmake_clean.cmake
.PHONY : hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/clean

hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/depend:
	cd /home/student/catcin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/student/catcin_ws/src /home/student/catcin_ws/src/hectorDroneSim/geographic_info/geodesy /home/student/catcin_ws/build /home/student/catcin_ws/build/hectorDroneSim/geographic_info/geodesy /home/student/catcin_ws/build/hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : hectorDroneSim/geographic_info/geodesy/CMakeFiles/_run_tests_geodesy_nosetests_tests.test_bounding_box.py.dir/depend

