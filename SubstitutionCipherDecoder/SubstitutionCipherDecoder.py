from random import shuffle

# Dictionary of words/suffixes each with a score based on how common they are
words = {
        'all': 2828, 'think': 180, 'just': 123, 'when': 577, 'over': 646, 'go': 1046, 'its': 548, 'ld': 2361, 'le': 8012,
        'also': 85, 'had': 814, 'day': 296, 'to': 7020, 'only': 372, 'th': 29424, 'ti': 4866, 'has': 419, 'do': 1553,
        'them': 530, 'his': 3907, 'get': 242, 'de': 4784, 'know': 331, 'they': 572, 'not': 1466, 'now': 1030, 'him': 1267,
        'like': 685, 'this': 1273, 'good': 200, 'she': 523, 'because': 73, 'people': 42, 'ed': 9071, 'ea': 6270, 'back': 208,
        'up': 1462, 'see': 1004, 'are': 1001, 'year': 116, 'et': 3069, 'es': 7922, 'out': 1429, 'even': 303, 'what': 510,
        'for': 2448, 're': 11436, 'ra': 3305, 'then': 592, 'new': 123, 'be': 3825, 'we': 2533, 'who': 616, 'use': 372,
        'come': 255, 'by': 1290, 'on': 8971, 'about': 310, 'ol': 2311, 'would': 427, 'of': 7119, 'could': 221, 'ou': 8303,
        'or': 7667, 'first': 207, 'into': 529, 'one': 1640, 'en': 8647, 'cr': 1269, 'your': 275, 'he': 25586, 'from': 1039,
        'her': 3411, 'there': 802, 'two': 289, 'been': 408, 'their': 610, 'way': 660, 'was': 1655, 'that': 2943, 'some': 888,
        'but': 1167, 'hi': 9296, 'ha': 10966, 'with': 1907, 'than': 424, 'must': 289, 'me': 5591, 'made': 177, 'look': 322,
        'these': 373, 'work': 122, 'say': 329, 'us': 3058, 'ur': 3135, 'will': 389, 'te': 6840, 'can': 528, 'were': 716, 'my': 738,
        'and': 7377, 'give': 126, 'is': 8238, 'it': 7435, 'an': 14394, 'as': 6775, 'ar': 7611, 'at': 9948, 'have': 757, 'in': 19065,
        'any': 591, 'if': 1222, 'want': 65, 'no': 3773, 'make': 157, 'nd': 10732, 'ng': 9771, 'how': 422, 'other': 632, 'take': 222,
        'which': 623, 'you': 1204, 'er': 14419, 'nt': 5299, 'our': 941, 'after': 296, 'most': 532, 'the': 18475, 'well': 217, 'st': 7883,
        'si': 2686, 'so': 3161, 'time': 570, 'sa': 2021, 'se': 6480
    }

key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

times = int(input("Enter number of times to shuffle the key: "))

print("Start: ", key, sep="")
for i in range (0,times):
    shuffle(key)
    print(i,": ",key,sep="")