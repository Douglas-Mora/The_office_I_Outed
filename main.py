def outed(meet, boss):
    total_people = 0
    total_score = 0
    for key in meet.keys():
        if key == boss:
            total_score += meet[key]*2
            total_people += 1
        else:
            total_score += meet[key]
            total_people += 1

    if (total_score/total_score) <= 5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'
