#include <iostream>
#include <fstream>

using namespace std;

int main() {
	cout << "Hello world\n";
	int forward = 0, depth = 0, input = 0, aim = 0;
	char command[10];
	ifstream inFile("C:\\Users\\allut\\Documents\\Github\\Koodia\\Advent2021\\adv2.txt");
	while (inFile >> command >> input) {
		//cout << "C: " << command << " I: " << input << "\n";
		if (!aim) {
			if (command[0] == 'f') {
				forward += input;
			}
			if (command[0] == 'd') {
				aim += input;
			}
			if (command[0] == 'u') {
				aim -= input;
			}
		}
		else {
			if (command[0] == 'f') {
				forward += input;
				depth += input * aim;
			}
			if (command[0] == 'd') {
				aim += input;
			}
			if (command[0] == 'u') {
				aim -= input;
			}
		}
	}
	cout << "Forward: " << forward << " Depth: " << depth << "\n";
	cout << "Sum: " << forward * depth;
}