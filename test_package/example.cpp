#include <iostream>

#include <imgui.h>

int main()
{
	ImGuiIO& io = ImGui::GetIO();

	std::cout << "ImGui::GetIO().IniFilename = " << io.IniFilename << std::endl;
}

