#import tool for dealing with csv files
import csv
# import data from csv file
# list of name of destination in jakarta 
destination = []
with open('data.csv', 'r') as csvfile:
    # create a csv reader object
    csvreader = csv.reader(csvfile)
    # make a list of lists
    list_of_lists = list(csvreader)
    # loop through the list of lists
    # remove element of list that constains "," and "."
    for i in list_of_lists:
        for j in i:
            if "," in j:
                i.remove(j)
            if "." in j:
                i.remove(j)
            if '' in j: 
                i.remove(j)
            if "-" in j:
                i.remove(j)
            # remove iten if item can type is int or flot 
            try:
                float(j)
                i.remove(j)
            except ValueError:
                pass
        destination.append(i)
# print(destination)
# if item type can be float or int, remove it
for i in destination:
    for j in i:
        try:
            float(j)
            i.remove(j)
        except ValueError:
            pass
# print(destination)
#print(destination)

#remove empty element
for i in destination:
    if len(i) == 0:
        destination.remove(i)
# print(destination)
#print(destination)
#remove emmpty element
for i in destination:
    if len(i) == 0:
        destination.remove(i)
# print(destination)
#print(destination) 
rem = [x for x in destination if x != []]
#print(rem)
#print(len(rem))
truedestination = []
for i in range(len(rem)):
    if i % 2 == 0:
        truedestination.append(rem[i])
# print(truedestination)
#print(truedestination)


destination = [['National Monument'], ['Istiqlal Mosque'], ['Taman Mini Indonesia Indah'], ['Museum Nasional Indonesia'], ['Ragunan Zoo'], ['Taman Impian Jaya Ancol'], ['Museum MACAN (Modern and Contemporary Art in Nusantara)'], ['Dunia Fantasi'], ['Jakarta History Museum'], ['Galeri Nasional Indonesia'], ['Jakarta Cathedral'], ['Wayang Museum'], ['Museum Bank Indonesia'], ['Sea World Ancol'], ['Museum Bahari Jakarta'], ['Pulau Bidadari'], ['Fatahillah Square'], ['Taman Suropati'], ['Atlantis Water Adventures Ancol'], ['Ancol beach'], ['Tebet Eco Park'], ['Museum of Textile'], [' Merdeka Square'], [' Taman Wisata Alam Mangrove'], ['Waterbom Pantai Indah Kapuk'], ['Museum of Fine Art and Ceramics'], ['Ocean Dream Samudra - Ancol'], ['Kidzania Jakarta'], ['Taman Ismail Marzuki'], ['Sekretariat Backpacker Jakarta'], ['Museum Mandiri'], ['Setu Babakan'], ['Allianz Eco Park'], ['Jakarta Aquarium & Safari'], ['Gallery for contemporary Indonesian art'], ['Site of the independence proclamation'], ['History displays in a stately building'], ['Small island with ruins & a museum'], ['City park for jogging & fountain shows'], [' Surfing'], ['Large park with a playground & sports'], ['Amusement park and park'], ['Late-1700s Dutch cemetery & museum'], ['Exhibits & activities devoted to kites'], ['Indonesian military history museum'], ['Indonesian National Awakening museum'], ['Domed mosque with an elegant courtyard'], [' Nature', ' and architecture '], ['Old town area with colonial architecture'], ['Well-known monument in a fountain'], ['History of a national youth movement'], [' Centuries-old'], ['Venue with space exhibits & observatory'], ['Theme park with rides & a dino zone'], ['Arts & crafts center open since 1977'], ['Works by a renowned painter & puppeteer'], [' Monument', ' and history '], ['Arts venue in a Dutch colonial building'], ['Urban park with a swimming pool'], ['Small island with Dutch trading relics'], ['Landmark honoring a historic event'], ['Zoo with shows & animal interaction'], ['Monument'], [' Stalls for food'], ['Arts hub for exhibitions & performances'], ['Cultural exhibits & Balinese-style decor'], ['Sasmita Loka Ahmad Yani Museum'], ['MOJA Museum'], ['Taman Situ Lembang'], ['Mangrove Ecotourism Centre PIK'], ["Gedung Joang '45"], ['Kawasan Ancol'], [' Art', ' and visual arts '], ['Winter sport center with chairlift rides'], [' 10 floors of vendors'], ['Modern art center with exhibits & a cafe'], ['Street food in an old-school Chinatown'], [' Zoo', ' orangutans'], ['19th-century church with a pipe organ'], ['Masjid Ramlie Musofa'], ['Unit Pengelola Kawasan Perkampungan Budaya Betawi Setu Babakan'], ['Diamant Kasteel Brug'], ['Barito Park'], ['Dinosaur Adventure'], ['Salihara Arts Center'], ['Alive Museum Ancol'], ['Museum di Tengah Kebun']]
#make a function that replace " " to be "%20" for url
def replace(destination):
    for i in range(len(destination)):
        for j in range(len(destination[i])):
            destination[i][j] = destination[i][j].replace(" ", "%20")
    return destination 
print(replace(destination))