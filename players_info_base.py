info = {

}
Player_scores = {

}
bot_scores = {

}


def save(user_id, first_name):
    idlist = open('id.txt', 'a+')
    if str("\n" + user_id + " : " + first_name) not in idlist.read():
        idlist.write(str("\n" + user_id + " : " + first_name))
    else:
        pass
    idlist.close()


def add_to_base(id, first_name, player_score, bot_score):
    info[id] = first_name
    Player_scores[id] = player_score
    bot_scores[id] = bot_score
