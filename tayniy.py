# import random
#
#
# def main():
#     names = 'Travis', 'Eric', 'Bob', 'Rose', 'Jessica', 'Anabel'
#     while True:
#         targets = random.sample(names, len(names))
#         if not any(a == b for a, b in zip(targets, names)):
#             break
#     for source, target in zip(names, targets):
#         list_a = '{} will give to {}.'.format(source, target)
#         print(list_a)
#
#
# if __name__ == '__main__':
#     main()
import random

def pick_recipient(group, recipients, single_flag):
    for person in group:
        gift = random.choice(recipients)
        if single_flag == 0:
            while gift in group:
                gift = random.choice(recipients)
        else:
            while gift in person:
                gift = random.choice(recipients)
        mail_list.append('%s=%s' % (person, gift))
        recipients.remove(gift)
    return recipients


if __name__ == "__main__":
    global mail_list
    mail_list = []

    # create lists of people, group couples at beginning or end of list and the singles opposite
    all_recipients = ['name_1-CoupleA: name_1-CoupleA@gmail.com',
                      'name_2-CoupleA: name_2-CoupleA@gmail.com',
                      'name_3-CoupleB: name_3-CoupleB@hotmail.com',
                      'name_4: name_4CoupleB@hotmail.com',
                      'name_5-Single: name_5-Single@gmail.com',
                      'name_6-Single: name_6-Single@gmail.com']

    # create couples and lists of singles to make sure couples don't get their other half
    # modify the groups to match the list of people from above
    coupleA = all_recipients[0:2]
    coupleB = all_recipients[2:4]
    single = all_recipients[4:]

    # keep initial list in tact
    possible_recipients = all_recipients

    # modify the groups to match what the input list is
    possible_recipients = pick_recipient(coupleA, possible_recipients,
                                         single_flag=0)
    possible_recipients = pick_recipient(coupleB, possible_recipients,
                                         single_flag=0)
    possible_recipients = pick_recipient(single, possible_recipients,
                                         single_flag=1)

    print (mail_list)