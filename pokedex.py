import conexao as con

conexao = con.Connection()

pokedex = conexao.query(f"""
SELECT nat_id, pokemon, hp, attack, defense, special_attack, special_defense, speed, total, type_i, type_ii, ability_i, ability_ii, hidden_ability, ev_worth, gender, egg_group_i, egg_group_ii, catch_rate, evolve FROM pokedex;""")

for nat_id, pokemon, hp, attack, defense, special_attack, special_defense, speed, total, type_i, type_ii, ability_i, ability_ii, hidden_ability, ev_worth, gender, egg_group_i, egg_group_ii, catch_rate, evolve in pokedex:
    print(f"""
    Nat_id: {nat_id}
    Pokemon: {pokemon}
    HP: {hp}
    Atk: {attack}
    Def: {defense}
    SpA: {special_attack}
    SpD: {special_defense}
    Spe: {speed}
    Total: {total}
    Type1: {type_i}
    Type2: {type_ii}
    Ability1: {ability_i}
    Ability2: {ability_ii}
    Hidden_Ability: {hidden_ability}
    EV_Worth: {ev_worth}
    Gender: {gender}
    Egg_Group1: {egg_group_i}
    Egg_Group2: {egg_group_ii}
    Catch_Rate: {catch_rate}
    Evolve: {evolve}      
            
    """)