#include <iostream>
#include <random>

int roll_d4();
/*uint16_t roll_d6();
uint16_t roll_d8();
uint16_t roll_d12();
uint16_t roll_d20();*/


int roll_d4() {
	std::random_device rd;
	std::mt19937::result_type seed = rd();
	std::mt19937 gen(seed);
	std::uniform_int_distribution<int> distrib(1, 4);
	int nmbr = distrib(gen);
	return nmbr;
}

int roll_d6() {
	std::random_device rd;
	std::mt19937::result_type seed = rd();
	std::mt19937 gen(seed);
	std::uniform_int_distribution<int> distrib(1, 6);
	int nmbr = distrib(gen);
	return nmbr;
}

int roll_d8() {
	std::random_device rd;
	std::mt19937::result_type seed = rd();
	std::mt19937 gen(seed);
	std::uniform_int_distribution<int> distrib(1, 8);
	int nmbr = distrib(gen);
	return nmbr;
}

int roll_d12() {
	std::random_device rd;
	std::mt19937::result_type seed = rd();
	std::mt19937 gen(seed);
	std::uniform_int_distribution<int> distrib(1, 12);
	int nmbr = distrib(gen);
	return nmbr;
}

int roll_d20() {
	std::random_device rd;
	std::mt19937::result_type seed = rd();
	std::mt19937 gen(seed);
	std::uniform_int_distribution<int> distrib(1, 20);
	int nmbr = distrib(gen);
	return nmbr;
}