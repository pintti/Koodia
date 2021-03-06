#pragma once
#include "Header.h"

struct attacks {
    /* example attack values that you need :
    base_damage, diceroll(d4, d6 etc.), hit_all(T / F), effect / s(AP, burn etc.), type(water, fire etc.)*/
    std::string attack_name;
    int base_damage{ 0 };
    int diceroll{ 0 };
    bool hit_all{ false };
    int effects{ NULL };
    int type{ NULL };
};

class Monster {
public:
    std::string m_monster_name{};
    int m_health{0};
    int m_armor{0};
    int m_type{NULL};   //monster type ex. water, fire etc.
    int m_dmg{0};
    int m_nmbr_of_attacks{0}; // use this to check for number of attacks, but how to check probability for which attack to use?

    Monster(std::string name, int health, int armor, int type, int dmg, int nmbr_attacks) {
        m_monster_name = name;
        m_health = health;
        m_armor = armor;
        m_type = type;
        m_nmbr_of_attacks = nmbr_attacks;
    }
};

class Goblin : public Monster {
public:
    attacks bash{"Bash", 3, 0 };

    Goblin()
        : Monster{"Goblin", 20, 0, 0, 3, 1}
    {}

};