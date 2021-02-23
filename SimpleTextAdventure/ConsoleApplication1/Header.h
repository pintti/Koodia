#pragma once

#include <iostream>
#include <cmath>
#include <string>
#include <random>

int roll_d4();
int roll_d6();
int roll_d8();
int roll_d12();
int roll_d20();

enum Types {
    fire,       // 0
    water,      // 1
    air,        // 2
    earth,      // 3
    dark,       // 4
    light       // 5
};

enum AttackEffects {
    piercing,	// 0, ignores specific armor
    crushing,	// 1, ignores specific armor
    stunning,	// 2, enemy loses one round
    burning,	// 3, causes enemy to lose health every turn
    bleeding	// 4, causes enemy to lose health every turn
};

enum dicerolls {
    d4_roll,    // 0, roll d4
    d6_roll,    // 1, roll d6
    d8_roll,    // 2, roll d8
    d12_roll,   // 3, roll d12
    d20_roll    // 4, roll d20
};