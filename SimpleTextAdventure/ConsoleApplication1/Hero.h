#pragma once
#include "Header.h"

struct stats {
	int Str{};
	int Dex{};
	int Int{};
	int Agi{};
	int Ctn{};
	//int Chr{};
};


class Hero {
public:
	std::string h_name{};
	int h_health{};
	int h_armor{};
	int h_type{};
	stats status{};

};