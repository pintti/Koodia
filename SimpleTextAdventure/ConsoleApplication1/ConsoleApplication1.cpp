#include "Header.h"
#include "Enemy.h"

int count_damage(int health, int damage, int armor = 0, bool weakness = false, std::string type = NULL);
//int m_attack(monster attacker);


int main(){
    Goblin jake;
    std::cout << "You encountered a " <<jake.m_monster_name<<'\n'<<jake.m_monster_name << " has " <<
        jake.m_health<< " HP.\n";
    jake.m_health -= 3;
    std::cout << jake.m_monster_name << " has " << jake.m_health << " HP.";
    
    return 0;
}


int count_damage(int health, int damage, int armor = 0, float weakness = 0.0, int atk_type = 0) {
    int dmg = (damage - armor);
    return dmg;
}


//int m_attack(monster attacker) { 
    //check for weakness
    //roll for damage
    //check armor and negate damage accordingly
    //apply damage
    //apply any effects
//}