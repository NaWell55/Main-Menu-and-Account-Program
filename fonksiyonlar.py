import math
def topla(a,b):
    return a + b


def cikar(a,b):
    return a - b


def carpma(a,b):
    return a * b


def bolme(a, b):                      
    if b == 0:
        return "0 ile bölme yapamazsın"
    return a / b


def usalma(a,b):
    return a ** b


def karekok(a):
    return math.sqrt(a)


def mutlakdeger(a):     
    if a < 0:
        return -a
    return a


def modalma(a,b):
    return a % b


def ortalama(a, b):            
    return (a + b) / 2


def enbuyuk(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "İki sayıda eşit"
    



def ucgencevre(a, b, c):
    return a + b + c

def ucgenalan(t, y):
    return t*y/2

def karecevre(a):
    return a*4

def karealan(a):
    return a*a

def dikdortgencevre(a, b):
    return 2*(a+b)

def dikdortgenalan(a, b):
    return a*b






def superlig():
    print("""- TRENDYOL SÜPER LİG PUAN DURUMU -
Sezon
2025-26                                                    

Takım                    OM  G   B  M  AG  YG  A   P     Son 5
1-Galatasaray            26  20  4  2  62  18  44  64    GMGGG
2-Fenerbahçe             26  16  9  1  57  27  30  57    GBBGM
3-Trabzonspor            26  17  6  3  52  29  23  57    MGGGG
4-Beşiktaş               26  14  7  5  47  30  17  49    GGGMG
5-Göztepe                26  11  10 5  30  20  10  43    BMBMB
6-Başakşehir             26  12  6  8  44  30  14  42    MGGGM
7-Samsunspor             26  8   11 7  29  31  -2  35    MBBMG
8-Kocaelispor            26  9   6  11 23  27  -4  33    GMMGM
9-Gaziantep FK           26  8   9  9  35  42  -7  33    MMBBG
10-Rizespor              26  7   9  10 32  36  -4  30    BGGGM
11-Alanyaspor            26  5   13 8  28  32  -4  28    GMMBB
12-Konyaspor             26  6   9  11 30  39  -9  27    MGMBG
13-Gençlerbirliği        26  6   7  13 28  36  -8  25    BMBBM
14-Kasımpaşa             26  5   9  12 22  36  -14 24    GBMBG
15-Antalyaspor           26  6   6  14 25  43  -18 24    GMBMM
16-Eyüpspor              26  6   7  14 19  37  -18 22    MGBMM
17-Kayserispor           26  3   11 12 20  48  -28 20    BGBMM
18-Karagümrük            26  4   5  17 24  46  -22 17    MBMBG
                          
UEFA Şampiyonlar Ligi ---> 1
UEFA Avrupa Ligi ---> 3
UEFA Konferans Ligi ---> 4
Küme düşme ---> 16, 17, 18

Son 5 maç
G ---> Galibiyet
B ---> Beraberlik
M ---> Mağlubiyet
""")





def premierlig():
    print("""- PREMIER LEAGUE PUAN DURUMU -
Sezon
2025-26                                                    

Takım                    OM  G   B  M  AG  YG  A    P     Son 5
1-Arsenal                31  21  7  3  61  22  39   70    GGGGG
2-Manchester City        30  18  7  5  60  28  32   61    GGGGB
3-Manchester United      30  15  9  6  54  41  13   54    BGGMG
4-Aston Villa            30  15  6  9  40  37  3    51    GBMMM
5-Liverpool              30  14  7  9  49  40  9    49    GGGMB
6-Chelsea                30  13  9  8  53  35  18   48    BBMGM
7-Brentford              30  14  5  11 46  41  5    47    GBMGB
8-Everton                30  12  7  11 34  35  -1   43    MMGGM
9-Newcastle United       30  12  6  12 43  43  0    42    GMMGG
10-Bournemouth           30  9   14 7  44  46  -2   41    GBBBB
11-Fulham                30  12  5  13 40  43  -3   41    MGMMB
12-Brighton              30  10  10 10 39  36  3    40    MGMGG
13-Sunderland            30  10  10 10 30  35  -5   40    MMBGM
14-Crystal Palace        30  10  9  11 33  35  -2   39    MGMGB
15-Leeds United          30  7   11 12 37  48  -11  32    BBMMB
16-Tottenham             30  7   9  14 40  47  -7   30    MMMMB
17-Nottingham Forest     30  7   8  15 28  43  -15  29    BMMBB
18-West Ham United       30  7   8  15 36  55  -19  29    BBMGB
19-Burnley               30  4   8  18 32  58  -26  20    GBMMM
20-Wolverhampton         31  3   7  21 23  54  -31  16    BBMGG

UEFA Şampiyonlar Ligi ---> 1-4
UEFA Avrupa Ligi ---> 5
UEFA Konferans Ligi ---> 6
Küme düşme ---> 18, 19, 20

Son 5 maç
G ---> Galibiyet
B ---> Beraberlik
M ---> Mağlubiyet
""")
    

def laliga():
    print("""- LA LIGA PUAN DURUMU -
Sezon
2025-26                                                    

Takım                    OM  G   B  M  AG  YG  A    P     Son 5
1-Barcelona              28  23  1  4  77  28  49   70    GGGGG
2-Real Madrid            28  21  3  4  60  24  36   66    GMMGG
3-Atletico Madrid        28  17  6  5  47  25  22   57    MGGGG
4-Villarreal             28  17  4  7  51  33  18   55    GGMBB
5-Real Betis             28  11  11 6  43  35  8    44    BBBMB
6-Celta                  28  10  11 7  38  31  7    41    BGMBB
7-Real Sociedad          28  10  8  10 43  42  1    38    BMBGG
8-Espanyol               28  10  7  11 35  42  -7   37    BMBBB
9-Getafe                 28  10  5  13 23  30  -7   35    MGMGX
10-Athletic Bilbao       28  10  5  13 30  40  -10  35    GGMBM
11-Osasuna               28  9   7  12 33  35  -2   34    BBMBM
12-Girona                28  8   10 10 31  43  -12  34    BMBMG
13-Valencia              28  8   8  12 30  42  -12  32    GMGGM
14-Sevilla               28  8   7  13 37  47  -10  31    BGBBM
15-Rayo Vallecano        28  7   10 11 27  34  -7   31    GBBGB
16-Mallorca              28  7   7  14 33  45  -12  28    MMMBG
17-Alaves                28  7   7  14 26  38  -12  28    BBMMB
18-Elche                 28  5   11 12 36  45  -9   26    BMMBM
19-Levante               28  6   7  15 30  45  -15  25    MMMGB
20-Oviedo                28  4   9  15 18  44  -26  21    BMMBG

UEFA Şampiyonlar Ligi ---> 1-4
UEFA Avrupa Ligi ---> 5
UEFA Konferans Ligi ---> 6
Küme düşme ---> 18, 19, 20

Son 5 maç
G ---> Galibiyet
B ---> Beraberlik
M ---> Mağlubiyet
""")
    

def seriea():
    print("""- SERIE A PUAN DURUMU -
Sezon
2025-26                                                    

Takım                    OM  G   B  M  AG  YG  A    P     Son 5
1-Inter                  29  22  2  5  65  23  42   68    GGGMB
2-Milan                  29  17  9  3  44  21  23   60    BMGGM
3-Napoli                 29  18  5  6  45  30  15   59    BMGGG
4-Como                   29  15  9  5  48  22  26   54    GGGGG
5-Juventus               29  15  8  6  51  28  23   53    MMGBG
6-Roma                   29  16  3  10 39  23  16   51    BGBMM
7-Atalanta               29  12  11 6  40  27  13   47    GGMBB
8-Bologna                29  12  6  11 38  34  4    42    GGGMG
9-Lazio                  29  10  10 9  29  28  1    40    MBMGB
10-Sassuolo              29  11  5  13 35  39  -4   38    GGMMM
11-Udinese               29  10  6  13 33  42  -9   36    MMGMB
12-Parma                 29  8   10 11 21  36  -15  34    GGBBM
13-Genoa                 29  8   9  12 36  40  -4   33    BGMGG
14-Torino                29  9   6  14 32  50  -18  33    MMGMG
15-Cagliari              29  7   9  13 31  41  -10  30    MBBMM
16-Fiorentina            29  6   10 13 34  43  -9   28    BGGMB
17-Lecce                 29  7   6  16 21  39  -18  27    MGGGM
18-Cremonese             29  5   9  15 23  44  -21  24    BMMGM
19-Pisa                  29  2   12 15 23  49  -26  18    MMMMG
20-Verona                29  3   9  17 22  51  -29  18    MMMGM

UEFA Şampiyonlar Ligi ---> 1-4
UEFA Avrupa Ligi ---> 5
UEFA Konferans Ligi ---> 6
Küme düşme ---> 18, 19, 20

Son 5 maç
G ---> Galibiyet
B ---> Beraberlik
M ---> Mağlubiyet
""")
    

def bundesliga():
    print("""- BUNDESLIGA PUAN DURUMU -
Sezon
2025-26                                                    

Takım                    OM  G   B  M  AG  YG  A   P     Son 5
1-Bayern Münih           26  21  4  1  93  25  68  67    GGGGB
2-Borussia Dortmund      26  17  7  2  55  26  29  58    BMGMG
3-Hoffenheim             26  15  5  6  54  34  20  50    BMGBB
4-Stuttgart              26  15  5  6  51  34  17  50    BGBBG
5-RB Leipzig             26  14  5  7  48  35  13  47    BBGGM
6-Leverkusen             26  13  6  7  49  33  16  45    MBGBB
7-Eintracht Frankfurt    26  10  8  8  49  49  0   38    GMGBG
8-Freiburg               26  9   7  10 37  43  -6  34    MGMGM
9-Union Berlin           26  8   7  11 31  42  -11 31    GMBBG
10-Augsburg              26  9   4  13 31  45  -14 31    GGGMM
11-Hamburg               26  7   9  10 29  37  -8  30    BMGMB
12-Mönchengladbach       26  7   7  12 30  43  -13 28    MMGBG
13-Mainz 05              26  6   9  11 31  41  -10 27    MBBBG
14-Köln                  26  6   7  13 35  44  -9  25    MBMMB
15-Werder Bremen         26  6   7  13 29  47  -18 25    MMGGM
16-St. Pauli             26  6   6  14 23  42  -19 24    MGBGM
17-Wolfsburg             26  5   6  15 35  56  -21 21    BMMMB
18-Heidenheim            26  3   5  18 24  58  -34 14    BMMMM
                          
UEFA Şampiyonlar Ligi ---> 1. , 2. , 3. , 4.
UEFA Avrupa Ligi ---> 5.
UEFA Konferans Ligi ---> 6.
Küme düşme ---> 17. , 18.
Play-out ---> 16.

Son 5 maç
G ---> Galibiyet
B ---> Beraberlik
M ---> Mağlubiyet
""")
    

def lig1():
    print("""- LIGUE 1 PUAN DURUMU -
Sezon
2025-26                                                    

Takım                    OM  G   B  M  AG  YG  A   P     Son 5
1-PSG                    25  18  3  4  54  22  32  57    MGGGM
2-Lens                   26  18  2  6  49  23  26  56    GMBBM
3-Marsilya               26  15  4  7  53  33  20  49    BMGGG
4-Lyon                   26  14  5  7  40  27  13  47    GMGBB
5-Lille                  26  13  5  8  40  33  7   44    BGMGB
6-Monaco                 26  13  4  9  45  37  8   43    GGGGG
7-Rennes                 26  12  7  7  43  37  6   43    GGGGM
8-RC Strasbourg          26  10  7  9  40  31  9   37    BGBBB
9-Lorient                26  9   10 7  37  40  -3  37    GBBBG
10-Brest                 26  10  6  10 34  36  -2  36    BGGGM
11-Toulouse              26  9   7  10 37  32  5   34    MBBMG
12-Angers                26  9   5  12 23  32  -9  32    MMMGM
13-Paris FC              26  6   10 10 29  41  -12 28    MBGBB
14-Le Havre              26  6   9  11 20  32  -12 27    GMMMB
15-Nice                  26  7   6  13 32  48  -16 27    MMBMG
16-Auxerre               26  4   7  15 19  36  -17 19    GMBMM
17-Nantes                25  4   5  16 22  42  -20 17    MMGM
18-Metz                  26  3   4  19 25  60  -35 13    MMMMM
                          
UEFA Şampiyonlar Ligi grup aşaması ---> 1. , 2. , 3.
UEFA Şampiyonlar Ligi eleme turu ---> 4.
UEFA Avrupa Ligi ---> 5.
UEFA Konferans Ligi ---> 6.

Küme düşme ---> 17. , 18.
Play-out ---> 16.

Son 5 maç
G ---> Galibiyet
B ---> Beraberlik
M ---> Mağlubiyet
""")
