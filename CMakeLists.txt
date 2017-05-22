project(imgui)
cmake_minimum_required(VERSION 2.8.12)

set(SRC_FILES
	imgui/imgui.cpp
	imgui/imgui_demo.cpp
	imgui/imgui_draw.cpp)

add_library(imgui STATIC ${SRC_FILES})

