d = {}
d1 = dict()
d2 = dict(name = 'Alex')
d3 = dict([('name', 'Alex')])
d4 = dict.fromkeys(['a', 'b'], 0)
d = dict(name='Dasha', age=25, len=166, apple=1, course='Python')
del d['age']
d.pop('len', None)
d1 = {'great' : 23, 'bite': 0}
print(d)
print(d1)
d5 = dict(name='Dasha', age=25, len=166, apple=1, course='Python')
d5.update(d1)
print(d5)
d11 = d5.keys()
print(d11)
d22 = d5.values()
print(d22)
d33 = d5.copy()
print(d33)
d33.clear()
print(d33)

#задача №2

store = {'apple':5, 'orange':10, 'melon':100}
price = {'apple':45, 'orange':55, 'melon':85}
store['apple']=7
price['orange']=62
print(store)
print(price)
store['berry']=122
price['berry']=99
store['juice']=24
price['juice']=20
print(store)
print(price)
total = {'apple':store['apple']*price['apple'], 'orange':store['orange']*
          price['orange'], 'melon':store['melon']*price['melon'],
         'all_store': store['apple']+store['orange']+store['melon']}
sum = {'all_sum': total['apple']+total['orange']+total['melon']}
h = total.update(sum)

# таска №3

hero = {
    'health': 100,
    'gold': 500,
    'mana': 100,
    'artefacts' : ['knife', 'shield', 'helmet'],
    'backpack' : ['mana', 'tablet']
}
enemy_hero = {
    'health': 150,
    'gold': 300,
    'mana': 100,
    'artefacts' : ['boots', 'ring'],
    'backpack' : ['meet']
}

hero['health'] += 100
hero['artefacts'].append('sward')
hero['health'] -=50
hero['backpack'].remove('tablet')
hero['gold'] -= 50
hero['backpack'].append('tablet')
hero['gold'] -= 100
hero['artefacts'].remove('knife')
hero['gold'] -= 200
hero['artefacts'].append('kolchuga')
hero.pop('mana', None)
hero['backpack'].remove('mana')
hero['health'] /= 2
hero['gold'] += enemy_hero['gold']
hero['artefacts'].extend(enemy_hero['artefacts'])
enemy_hero.clear()



