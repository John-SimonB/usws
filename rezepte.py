from importlib_metadata import re
import pandas as pd
import numpy as np

def preisRechnung():
    # Es ist sinnvoll eine Liste mit Dictionaries zu erstellen, da die vorherige Form doppelte keywords (z.B. 2 mal "name") beinhaltete. Deshalb die [] Klammern :)
    rezepte =[
        {"name": "Potato salad", "beschreibung" : {
                "zubereitung" : "Wash potatoes and bring to the boil in a saucepan covered with salted water. Cover and cook until tender, about 20 minutes. Cut onion in half, peel and finely dice. Wash chives, shake dry and cut into rolls. In a pot, bring vegetable broth to a boil and cook onions in it for about 3 minutes. Let broth cool slightly and mix oil, vinegar and mustard. Season with salt and pepper. Drain potato, peel and slice into thin slices while still lukewarm. In a bowl, pour lukewarm dressing over potato slices, mix and let sit for at least 20 minutes. Season Classic Potato Salad to taste and serve sprinkled with chives. Enjoy your meal! Tip: Prepare the potato salad and let it sit for at least an hour. Then it tastes even better.",
                "nährwerte" : "calories: 273 kcal, carbohydrates: 45 g, protein: 7 g, fiber: 4 g, fats: 7 g",
                "menge" : ["1kg", "1S", "15g", "1g", "1g", "5ml", "5ml", "5g", "300ml"],
                "zutaten" : ["Bio Kartoffeln vorw. festkochend 1.5kg (Deutschland)", "Bio Zwiebel 1 Stk. (Deutschland)", "Schnittlauch 15g (Deutschland)", "Bad Reichenhaller Alpensalz 500g","REWE Beste Wahl Cayenne Pfeffer gemahlen 39g", "Thomy Reines Sonnenblumenöl 750ml", "Bio Weinessig Balsamico Balance 500ml", "Bautzner Senf Mittelscharf 250g", "Jürgen Langbein Gemüse-Fond 500ml"],
                "link" : [],
                "ernaehrungsform" : "vegan",
                "bild" : "https://images.pexels.com/photos/2349277/pexels-photo-2349277.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"}},

                {"name": "Pasta alla Norma", "beschreibung" : {
                "zubereitung" : "Heat some olive oil in a pot and sweat the garlic in it. Then add the peeled tomatoes. Simmer over low heat for 10-15 minutes. Heat a pot with plenty of salted water and cook the pasta al dente according to package instructions. Cut the eggplants into slices. Heat a pan with plenty of sunflower oil. Fry the eggplant slices on both sides. Put them on a baking tray covered with kitchen roll and let them drain. Season with salt and pepper. Grate the ricotta salata with a kitchen grater. Add the finished pasta to the pot with the tomato sauce. Add the fried eggplant and a few basil leaves and stir everything well. Divide the pasta among deep plates and sprinkle the ricotta salata on top. Buon appetito!",
                "nährwerte" : "Calories: 102kcal, Carbohydrates: 13.4g, Protein: 2.7g, Fat: 1.8g",
                "menge" : ["500g", "3g", "200g", "5ml", "5g", "1g", "1g"],
                "zutaten" : ["Barilla Penne Rigate 500g", "Iglo Knoblauch-Duo 60g", "Marziale Tortelloni Ricotta Spinaci 250g", "Thomy Reines Sonnenblumenöl 750ml", "Iglo Basilikum 50g", "Bad Reichenhaller Alpensalz 500g", "REWE Beste Wahl Cayenne Pfeffer gemahlen 39g"],
                "link" : [],
                "ernaehrungsform" : "vegetarisch",
                "bild" : "https://images.pexels.com/photos/432072/pexels-photo-432072.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1%22%7D%7D"}},
                
                {"name": "Greek salad", "beschreibung" : {
                "zubereitung" : "Wash cucumber, remove ends, quarter lengthwise and cut into pieces. Wash and quarter tomatoes. Halve the shallot, peel and cut into rings. Dice the feta. Wash lemon, cut in half and squeeze juice. Wash parsley, shake dry, pluck leaves from stems and chop finely. In a bowl, mix olive oil with 2 tablespoons lemon juice, season with salt and pepper. Mix the cucumber, tomatoes, shallot, feta, parsley and black olives with the dressing and serve. Enjoy your meal! Tip: This goes well with herb bread sticks.",
                "nährwerte" : "kalorien: 226 kcal, kohlenhydrate: 17 g, eiweiß: 10 g, ballaststoffe: 2 g, fette: 15 g",
                "menge" : ["1S", "500g", "2S", "200g", "1S", "20g", "5ml", "1g", "1g", "40g"],
                "zutaten" : ["Bio Gurke 1 Stk. (Deutschland)", "Cherrytomaten 250g (Deutschland)", "Zwiebel Gelb 1 Stk. (Deutschland)", "Patros Feta Leicht 150g", "Zitrone 1 Stk. (Italien)", "Petersilie glatt 15g (Deutschland)", "Bertolli Gentile Natives Olivenöl 500ml", "Bad Reichenhaller Alpensalz 500g", "REWE Beste Wahl Cayenne Pfeffer gemahlen 39g", "Deli Genuss Oliven mit Basilikum 165g"],
                "link" : [],
                "ernaehrungsform" : "vegetarisch",
                "bild" : "https://images.pexels.com/photos/1059905/pexels-photo-1059905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"}},
                
                {"name": "Geschnetzeltes in cream with mushrooms and spaetzle", "beschreibung" : {
                "zubereitung" : "Wash chicken fillet, pat dry, cut in half lengthwise, cut into strips about 1 cm thick and set aside to temper. Peel, halve and finely dice onions. Wash scallions, remove root ends and outer skin layer, if any, and cut white and green parts separately into thin rings. Clean mushrooms with paper towels, if necessary, and cut into quarters or eighths, depending on size. In a saucepan, bring about 4 l of salted water to a boil, covered. In a frying pan, heat 2 tablespoons of oil on high heat. Sear chicken fillet strips with salt on all sides for about 2 minutes and then set aside on a plate. Do not clean the pan. Add 3 tablespoons oil to the drippings in the pan and sauté mushrooms with salt on medium-high heat until golden brown all around, about 2-3 minutes. Add white parts of scallions and diced onion and sauté on medium heat for about 2-3 min. Pour in cream and 75 ml water and simmer for approx. 4-5 min. Then stir in the cutlets including the meat juice and the green part of the spring onions and just keep warm. Do not cook the creamed meat now, otherwise the fillet pieces would become too dry. In the meantime, add spaetzle to boiling salted water (it is important that the water is no longer bubbling) and cook for about 2-3 minutes. Stir occasionally. When the spaetzle come to the surface, they are done and can be drained into a colander. Season the Geschnetzelte with mushrooms with salt and pepper, arrange on plates with the Spätzle and serve. Enjoy your meal!",
                "nährwerte" : "calories: 604 kcal, carbohydrates: 51 g, protein: 45 g, fiber: 3 g, fats: 22 g",
                "menge" : ["600g", "2S", "500g", "250g", "480g", "5ml", "1g", "1g"],
                "zutaten" : ["Wilhelm Brandenburg Hähnchen Innenbrustfilet 350g", "Bio Zwiebel 1 Stk. (Deutschland)", "Bio Champignons Weiß 250g (Deutschland)", "Hansano Schlagsahne 30% Fett. 250g", "Herr Kächele Lieblings-Spätzle 480g", "Bertolli Gentile Natives Olivenöl 500ml", "Bad Reichenhaller Alpensalz 500g", "REWE Beste Wahl Cayenne Pfeffer gemahlen 39g"],
                "link" : [],
                "ernaehrungsform" : "fleisch",
                "bild" : "https://tarasmulticulturaltable.com/wp-content/uploads/2014/04/Spatzle-mit-Pilzen-German-Spaetzle-with-Mushrooms-5-of-5-500x500.jpg"}},

                {"name": "Cucumber salad", "beschreibung" : {
                "zubereitung" : "Wash cucumbers, remove ends and cut into thin slices or shave. Put cucumber slices in a colander, mix with about 1 tsp of salt and let stand for about 30 min. In a bowl, mix yogurt, crème fraîche, vinegar, mustard and sugar and season with salt and pepper. Halve, peel and finely dice the onion and add to the dressing. Wash dill, shake dry, pluck tips and chop finely. Squeeze cucumber slices and add to dressing. Fold in dill and season to taste with salt and pepper. Serve cucumber salad immediately or refrigerate. Enjoy your meal!",
                "nährwerte" : "calories: 66 kcal, carbohydrates: 11 g, protein: 3 g, fiber: 2 g, fats: 2 g",
                "menge" : ["2S", "50g", "50g", "10ml", "10g", "1S", "15g", "1g", "1g"],
                "zutaten" : ["Bio Gurke 1 Stk. (Deutschland)", "Andechser Natur Bio Joghurt 3.8% Fett. 100g", "Dr. Oetker Creme Fraiche 30% Fett. 150g", "Bio Apfelessig Balsamo 500ml", "Bautzner Senf Mittelscharf 250g", "Bio Zwiebel 1 Stk. (Deutschland)", "Dill 15g (Deutschland)", "Bad Reichenhaller Alpensalz 500g", "REWE Beste Wahl Cayenne Pfeffer gemahlen 39g"],
                "link" : [],
                "ernaehrungsform" : "vegetarisch",
                "bild" : "https://www.afarmgirlsdabbles.com/wp-content/uploads/2021/08/creamy-cucumber-salad_afarmgirlsdabbles_01s.jpg"}},

                {"name": "Pasta with salmon cream sauce", "beschreibung" : {
                "zubereitung" : "Defrost salmon preferably overnight in the refrigerator, wash and pat dry. In a saucepan, bring salted water to a boil, covered. Add farfalle to boiling salted water and cook on medium heat until al dente, about 13-15 minutes. Halve, peel and finely dice onion. Cut lemon in half and squeeze juice. Heat oil in a frying pan over medium heat and sauté onion until translucent, about 3 minutes. Add 1 tablespoon lemon juice and cream, bring to a boil and season lightly with salt and pepper. Simmer sauce on medium-high heat for approx. 3-4 min. until creamy. Meanwhile, dice salmon about 2 cm in size. Wash dill, shake dry, remove coarse stems and chop finely. Add salmon to sauce, reduce heat and gently cook salmon with lid closed on low heat for approx. 3 min. Drain farfalle in a colander and allow to drain slightly. In the pot, mix farfalle with salmon sauce and dill and season with a little of the remaining lemon juice, salt and pepper. Arrange quick pasta with salmon cream sauce on plates and serve. Enjoy your meal!",
                "nährwerte" : "calories: 757 kcal, carbohydrates: 99 g, protein: 38 g, fiber: 2 g, fats: 23 g",
                "menge" : ["500g", "500g", "1S", "1S", "250g", "15g", "5ml", "1g", "1g"],
                "zutaten" : ["REWE Bio Portionen vom Lachsfilet 250g", "Barilla Collezione Farfalle 500g", "Bio Zwiebel 1 Stk. (Deutschland)", "Zitrone 1 Stk. (Italien)", "Hansano Schlagsahne 30% Fett. 250g", "Dill 15g (Deutschland)", "Bertolli Gentile Natives Olivenöl 500ml", "Bad Reichenhaller Alpensalz 500g", "REWE Beste Wahl Cayenne Pfeffer gemahlen 39g"],
                "link" : [],
                "ernaehrungsform" : "fisch",
                "bild" : "https://www.lavenderandmacarons.com/wp-content/uploads/2019/12/Easy-Creamy-Salmon-Pasta-Recipe-2.jpg"}},

                {"name": "Rosemary potatoes", "beschreibung" : {
                "zubereitung" : "Preheat oven to 220 °C (convection oven). Wash the potatoes and cut into wedges. Wash rosemary, shake dry and remove needles from stems. Thoroughly mix potatoes with olive oil, rosemary, salt and pepper on a tray with baking paper. Bake in oven for about 20-25 minutes until golden brown. Enjoy your meal!",
                "nährwerte" : "calories: 218 kcal, carbohydrates: 40 g, protein: 5 g, fiber: 4 g, fats: 4 g",
                "menge" : ["1kg", "24g", "10ml", "1g", "1g"],
                "zutaten" : ["Bio Kartoffeln Festkochend 2kg (Deutschland)", "REWE Beste Wahl Rosmarin geschnitten 24g", "Bertolli Olivenöl Cucina 500ml", "Bad Reichenhaller Alpensalz 500g", "REWE Beste Wahl Cayenne Pfeffer gemahlen 39g"],
                "link" : [],
                "ernaehrungsform" : "vegan",
                "bild" : "https://images.themodernproper.com/billowy-turkey/production/posts/2020/Roasted-Rosemary-Potatoes-10.jpg?w=1067&auto=compress%2Cformat&fit=crop&dm=1607484193&s=2237da4882efee52eec852fdfcc9be5a"}},

                {"name": "Chocolate strawberries", "beschreibung" : {
                "zubereitung" : "In a saucepan, bring about 500 ml of water to a boil. Wash strawberries and pat dry. Chop light and dark couverture separately. In a bowl, melt white couverture over a water bath. Place white couverture in a freezer bag. In another bowl, melt dark couverture over water bath as well. Then place in a bowl. Gradually hold strawberries by the green and dip in dark chocolate coating. Then place chocolate strawberries on a baking sheet lined with parchment paper. Decorate chocolate strawberries with white stripes as desired. Serve the chocolate strawberries. Enjoy!",
                "nährwerte" : "calories: 449 kcal, carbohydrates: 42 g, protein: 4 g, fiber: 1 g, fats: 29 g",
                "menge" : ["150g", "200g"],
                "zutaten" : ["Dr. Oetker Kuvertüre Vollmilch 150g", "REWE Beste Wahl Erdbeeren 500g"],
                "link" : [],
                "ernaehrungsform" : "vegetarisch",
                "bild" : "https://lilluna.com/wp-content/uploads/2021/01/chocolate-covered-strawberries3-resize-10.jpg"}},

                {"name": "Broccoli cream soup", "beschreibung" : {
                "zubereitung" : "Cook broccoli in vegetable broth until done, then remove from broth. Puree broccoli florets with crème fraîche. Gradually add vegetable broth. Enjoy!",
                "nährwerte" : "",
                "menge" : ["300g", "10g", "500ml"],
                "zutaten" : ["REWE Bio Broccoli 300g", "Dr. Oetker Creme Fraiche 30% Fett. 150g", "Jürgen Langbein Gemüse-Fond 500ml"],
                "link" : [],
                "ernaehrungsform" : "vegetarisch",
                "bild" : "https://assets.epicurious.com/photos/57b3390706de447f4e6d9316/master/pass/cream-of-broccoli-soup.jpg"}},

                {"name": "vegan pancakes", "beschreibung" : {
                "zubereitung" : "Put all the ingredients for the pancakes in the blender and puree until fine. Heat a little oil in a non-stick frying pan. Put 1-2 tablespoons of batter per pancake into the pan and bake the pancakes on both sides for about 2 minutes Garnish the finished pancakes with maple syrup and berries as desired or simply enjoy them plain. Enjoy!",
                "nährwerte" : "",
                "menge" : ["1S", "0.2l", "100g"],
                "zutaten" : ["Banane 1 Stk. (Brasilien)", "Alpro Mandeldrink 1l", "Kölln Bio Haferflocken Zart 500g"],
                "link" : [],
                "ernaehrungsform" : "vegan",
                "bild" : "http://carry-on-cooking.com/wp-content/uploads/2021/01/vegane-pancakes-apfelmus-tassenrezept-fluffige-pfannkuchen-ohne-ei-carryoncooking-foodfotografie-foodblog3.jpg"}},
            

                {"name": "Lentils with spinach and pomegranate", "beschreibung" : {
                "zubereitung" : "Prepare lentils according to package directions. Cut the pomegranate in half and break out the seeds with a wooden spoon (best done over a bowl of water, the seeds will fall to the bottom and can be removed more easily). Prepare the Iglo spinach leaf according to package directions. Add the cooked lentils and pomegranate seeds to the spinach, mix everything in - done! Enjoy!",
                "nährwerte" : "",
                "menge" : ["500g", "1S", "30g"],
                "zutaten" : ["Iglo Rahm-Spinat 500g", "Granatapfel 1 Stk. (Türkei)", "Müller's Mühle Teller-Linsen 500g"],
                "link" : [],
                "ernaehrungsform" : "vegetarisch",
                "bild" : "https://cdn.nomadfoodscdn.com/-/media/project/bluesteel/iglo-de/2018_iglo_bilder/04_rezepte/linsengranat_web_20180314.jpg"}},

                {"name": "Spinach sandwich with fried egg", "beschreibung" : {
                "zubereitung" : "Prepare the iglo creamed spinach in a pot as described on the package. Put a pan on the stove and let it get hot, toast the slices of crusty bread in the hot pan without oil. Wipe out the pan with a cloth and heat again, add the oil and then fry the eggs. Spread the iglo creamed spinach on the bread slices and arrange the fried eggs on top.",
                "nährwerte" : "",
                "menge" : ["100g", "100g", "2er"],
                "zutaten" : ["Iglo Rahm-Spinat 500g", "1 Stk. - Dick's Krustenbrot 500g", "Rewe Eier Freilandhaltung 6er"],
                "link" : [],
                "ernaehrungsform" : "vegetarisch",
                "bild" : "https://image.brigitte.de/10888982/t/GD/v4/w1440/r1/-/spinatbrot-mit-pochiertem-ei.jpg"}},

                {"name": "Mac and Cheese", "beschreibung" : {
                "zubereitung" : "Prepare the iglo creamed spinach in a pot as described on the package. Put a pan on the stove and let it get hot, toast the slices of crusty bread in the hot pan without oil. Wipe out the pan with a cloth and heat again, add the oil and then fry the eggs. Spread the iglo creamed spinach on the bread slices and arrange the fried eggs on top.",
                "nährwerte" : "",
                "menge" : ["100g", "100g", "2er"],
                "zutaten" : ["Iglo Rahm-Spinat 500g", "1 Stk. - Dick's Krustenbrot 500g", "Rewe Eier Freilandhaltung 6er"],
                "link" : [],
                "ernaehrungsform" : "vegetarisch",
                "bild" : "https://image.brigitte.de/10888982/t/GD/v4/w1440/r1/-/spinatbrot-mit-pochiertem-ei.jpg"}},
            ]



    # productname,size,newprice,oldprice,link
    angeboteArray = np.transpose(np.array(pd.read_csv('angebote.csv')))
    allproductsArray = np.transpose(np.array(pd.read_csv('allproducts.csv')))

    # Überprüfe, ob mindestens 1 Zutat sich in der angebote.csv befindet
    for i in rezepte:
        if(i["beschreibung"]["ernaehrungsform"] == "vegan"):
            bild = "data:image/png;base64,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"
        elif(i["beschreibung"]["ernaehrungsform"] == "fleisch"):
            bild = "https://thumbs.dreamstime.com/b/steak-meat-icon-over-white-background-nutritive-fresh-food-design-vector-illustration-79898335.jpg"
        elif(i["beschreibung"]["ernaehrungsform"] == "fisch"):
            bild = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAABOFBMVEX/////VyI3R0/mShk+JyP/SwDoShj/VR//VBz/TAD/SAD/UhgvR1DrShYzREz/URT/TgwwR1AkOEIvQEknR1H/+vgpPEX/8u7u7/AbMjzvShPZ3N3Mz9H/WiX/q5f/4dk9TVXcSx7/mYAsJCMzJSOzuLvfShyzSS5daW+iqKv/5+H/jXD/zcD/uaj/1cr/xbf/cUn/gF4aRlH/oYlQXWRzfYK/w8ZvSELTSiCRSDmWnaDCSSd6g4j0ViWDSD3/ZTn/fFv/YTCdV0jkakjuZz//kXdOR0k/R0tYSEafSDaqSTBlSEQROUTGVjjFRR+GkZbHOgB5Rz04MzhxOCx1MSKNW1LQUi61l5FSU1beyMNOKyPEYklkVVRaLSOVPCOCY1y0W0iENyPSnZG1ZledNhuHd3Xps6bMa1N+IuKsAAAMJUlEQVR4nO2cfVfbyhGHkRxbsizZliyEXxMrgGwgJIQYYzBgaBMMgcKlyW170zRt+vr9v0H1YmtX0kpaC7AMZ54/cnJyUNifZnZmdrS7S0sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFcvVZn99vVlNexyPRHVjj60piqYptfZtM+3RPDzVo4pWLLIOxYrS66c9ogemr1VYD0Wl10h7UA/JRo0NUKwdpj2sh2NdCQo0UbrPJeZUK0WiQrbSfiaeulchC7Q89VkE1SphEiJPfQ4xdUObypFVdVccj1l1VxXliRW1ZyCxN5mFonpxOTQyFoPOwYWoyk7aePqO6sxCUT4Y1KVczlaYy0n1TGefVe25+NTDTcN2UnV/UHfUuUj1wcHY1FhsP/Gk0bSSoXop+fTZppSMA1VkK920x0im2mg2m4341983FaodKajP0ajvq6x2O4fxzkjztm2uExSlVmO7h9HLIVOh+rlOFmhprHdYsbY+r4FT0uwqFbRO0JRidyM8WvQV9STEgpP5qF+pymJNxQ3FX4VVNK23ETLIpnKeIcxB3Iy5g92FmoqkhYKVumt7xMzWuB46JsRl+iTXO9cLtNBoaiSBTvImGbJ6Uc8YupHRTTLHx8zx8bH9V+vfXK3SUFucrNgLWSg4hmwfBjT+wTBFtRg/LUuqYQwMW6V0szB+6lvryWatqYomsmz+Yf79Wrv1atwsB8R5hLZ0w7RoRvplUeIpbkJRZc/3LzvDG9MWGdPtBsPO54O7qz967Pi6FKnQwTRn7mYx4im2FFLZu85AMsm51aZZb0pSPTe4eec+sNLiKBRaxiy8TFEXYn0aZ9TxZ0MKlmLmP+h6S3jlPrCdpxPIMPnNFHUhjiYrBfaSIM9EN44Zht9BD+zwlAJLr9NTheNMQ/VKJ5Uphn5sD7aM/O2VQGtCYcV9aOVliuZsWwrVkxzBPfWJPlMhclKqOGOb8BP6Ja+F8um75RTUmVRtC54QHFQ33MHyI/QAvQnRW9kscUwhz3x6RRjAo1M1TShf+T00Z7jms02InPRNllJg4T36JVu23bmSMErBkFUz0Ih6LkqfxxxbBUqF2TfuM5vuW+GzrQ/znpGmDc3lum/+HftH6/74MkOZDLkz9DvwqcuVS1vzddZqsTg2PCYM6MPDPrWTlj+4zyx7py5Xyu68nafEtuhZzgb1mZkbFTSfaCNpFhnqZaCOLQg7b0hjeRx66hCZ0DCCSwY8sS2PKNM97qRnBMcuCKdzs2N3jOKMTtKHFzTU6R6Lvm/JVV4hfzqn+Xh7LkU4qAU2DYMOF4KAImZo9C0IWyukET006/vSJEMQDch44v57ylyBOWnUUqRUfjmH/Nj8IkUZ0FLo2mOZdlmBVWxvohyby4/mEHK+SlaFHT4KfuS+Z+ppmKWOvnz2/b1ctb/XrintvYjm59LSr/UoA5rT5dT9UeppiFaG8SVCCUtGs9Ls2X3eojb+0852qMP/uR46A22wsEhbss0WfbnEEaevOR0Y+S8jns+3wib1bzFJHAs0JcqSDau6A2ZvZQaBN1o6S5QcG9NGtvjRGphZEJK9Ie4to7XhCm2gKW+7/7s/+g6/ra6urX41vP/KC0laOu2JQPWvkzqEE05Jdf129OTiGNf2b2mL0iwyiff1tb6svrBYWx36H9maOW9M26Dyd+QThdJ28Ac/RHsp10LvgtaGBfdNrngVfll7MWH1xvdMeWfWyYhMiE0eLvs+8Kpisjg2p2gbGFi+965FhqsvEP6nSmezSWxOO9ljb+FbKvgndYzrYaGUtsvGoaaHdwr8DRMY8FOmwM20OJ40CVnxV9+wOMHnqXGBBv047cICM7sn3xtrmMK1n8HnRjNYcblHclKHrKePuRmjEOXjFdIyiEQJrX49ZtdxJ33xhfDgaImaxtRJd0fBYZWxJlHsqh31aF7RVjRhZvcoXCMoZMpb1ArdXn2b9N7LOyjexCQLbPlLXZXmXYXLHrMf4yZc+0F6NEtdwR1OFMp/J84d7F3F1ZoCtbWRQuTY3qXTT2wirg5Ij/JntGlxuntQ/B1x7mAt3ph0iCmMs7YLqvM2vZnIQG669jXkWULGJuIGmn+QFaLSeCsm4Zeore0iuAnJP3XdhLj2LaTax78BRULM9whsRRST5LDfSP3FAgtO/iro5tvq2os1szANXa8JlBnDDaW/JytE8zAmBWC5jbrdjRQGK9nW8OeXrz+Ic9D/cCTuh93dj0QBWJch5osu9i4eRGH8w3SFDVJISIeMp332GArRPKT+XjyFK9MF04arkOzv9Aoxa9M22rDFE3WR4IJ/srqXQlRXxSlE74JeIcoWHGWh5yJQpnxUtJEVlh9VYWjGjwdr7C2yDfG6dEaFWdr2abrzEFtS0i64pr+NchamHUux//2U9hkbLku9QEw3H2J10IeZgqkwQ4s/1ZoG69PQb6Ayyc/SUoyrS9G4H6Eu5VqzNyCZmZa/SymvLZi8W7YtU2+/YUq0qwqHGdaH1Ctg6vUhHvN52nRR2pmtJRyzxufD+n1RCqnX+Hi6pXXt0qwNYdSnISrEPhM8Qp8GX35SGr40SyPRJrLXxuHfQeJiQYJemxlM3fGuUL2W8owualKN6JfyZby6jRtCgn6pZxlL0yjPB781xBPa82YKjLev//A9b0/dFtfpYvwtalrCvlsweb/Hx3z2TPDdwlNRxM5eLtG3w6WwnM/nP/h/MKZUwYoDCnNMEVy3i9tGVSgl3Y0xPayLfz9kyoTPyY/w/dCTEaMTbnmUfGcU6/8GzPDCa8KMjhl3km/AntI+MgQLSWLMlOZ0fdF2EgafHRH3A7yNSQLoOz71hiEG35IaMX35PG2Hm8z6ZKuC/N0MNoXsKOR/+2cuajdNor0YJnn01Lsw09/HQx36RWe/ifj9oxC+Vf5f9fAtbfY4sP009KEG75mRNw1xwqf7b2qrHlpHX2u17kZEm/XfkmdffnCsp+6P0tfeDMejpESc6SX+gXa0VRsxZ5cbP6TwraUWSfa1MR7TLwf7CHyC3SVJWf/p7L4MN2OCvYneF7P00v9c+WyOu6AP7+J20CbYX2qBNV28n4KtrDWXrbMT9i6mB8/DNtEm2SPMeL8EbmPhlAvJWo9Gr4idJyGaMck+bwsBE4JKtzJzvxw4O238egTCaRIm0V59vxGnr6aQn6uDWlRZed9zZIbgqknOW1hgG/iWXlv+zQvv53+4yzoVNPAeezL8UTXJmRm/EZfPeH7OZ2WQQnHff8mF7jtYkuDckw2+weytsJN8t/N9sE7nqUPf6bycr8hJcnbNAmsNmxJTUGdRtStXnXDAEgs5Sc4fOg8uwFFg+wypfG4QDjkPXDsmOkNqQ7mz4lGxux3i+SB40DnnnOO2bZHgHPDk3aR0+heja7upzHb8tz45vuo4a6Kz3Dal31LU5nA7aTuq+zrxPL4ddBKdx7fuAjH+k56yKf1p21HcvbvJkS8d0I8T3KlgyjOGxRSVTcHuxRDVi4OhUbfvxbDO5+fQvRi//Nd9gGp/RetYN3K5g+uFuJwOv+ZRFtXx1cllZzgY6IahD26GnY51t0kXH2lsrLGuqcnk6jfn1xupqcJp+u5QksXJBTWicz+Net31WmIz0k31jJ6xL247UbWjlCT5Cb+rk7WuxApeFvW/DOmOIeuGoczkIiUpc8mKlV4aakg0imHXKBU17YhwsG/vszS9J8qw7okyrL9MxE30nasLdbdgv0aSWKzUWPKFZrfXJzkpE7jfayKvrjuXJ1YW5yYswsXO1vXV7FFYIFzX1PGQfG2iZHSudkV20QSaKWNP0YpInab0jiJuFrS+3Kn7Q0/ytK/3HHzelyeXmC6YQJPGbc++N1Gp1XpH643IatJOobJ67iRPK2Ga4oaXd+eTO1oXUqBFtdHs95s0Q3M+ocuiyJ5f3d3dXV2Mrft2ZRSAn/yV0OgiYVaWRVlG2my0p3+tdzUqg7LKoiT6+3AbetUiW1EW5aq9e1FthxQJRaX35D3UoRG48dSZgexi1NoPQbMSnIuaErwn8wlT7XpqPbMIqjwrfRbNLqtoFQtN0dqhNd6TptrcuD3aO7o97D/1DA8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPC0+D/d6ktfNAlPjAAAAABJRU5ErkJggg=="
        elif(i["beschreibung"]["ernaehrungsform"] == "vegetarisch"):
            bild = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyyb7j_f6najkw56miIuVRPmeEnfUYC8pg9g&usqp=CAU"
        else:
            bild = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Solid_white.svg/2048px-Solid_white.svg.png"

        i.update({'pic': bild})
        preis = 0
        zutatenCount = 0
        for j in i["beschreibung"]["zutaten"]:
            # finde mengenangabe
            # WENN: Suche alle Produkte für das Rezept in der CSV und berechne den Preis für das fertige Gericht.
            if j in angeboteArray[0]:
                # find size, wenn es sich um eine Liste handelt, index, keine Liste, kein Index
                if type(angeboteArray[1][np.where(angeboteArray[0] == j)]).__module__ == np.__name__:
                    sizeProd = angeboteArray[1][np.where(angeboteArray[0] == j)][0]
                else:
                    sizeProd = angeboteArray[1][np.where(angeboteArray[0] == j)]
                sizeRez = i["beschreibung"]["menge"][zutatenCount]
            
                # mögliche Einheiten sind g oder kg, l oder ml
                if sizeRez[-1] == "g" or sizeRez[-1] == "l" or sizeRez[-1] == "S":
                    if sizeRez[-2] == "k" or sizeRez[-2] == "m":
                        sizeRezNum = float(sizeRez[:-2])
                    else:
                        sizeRezNum = float(sizeRez[:-1])
                
                if sizeProd[-1] == "g" or sizeProd[-1] == "l" or sizeRez[-1] == "S":
                    if sizeProd[-2] == "k" or sizeProd[-2] == "m":
                        sizeProdNum = float(sizeProd[:-2])
                    else:
                        sizeProdNum = float(sizeProd[:-1])
                
                
                # [0], da es sich nur um ein Element handelt
                preis += float(angeboteArray[2][np.where(angeboteArray[0] == j)][0].replace(",", "."))*sizeRezNum/sizeProdNum

                index = np.where(angeboteArray[0] == j)
                link = angeboteArray[4][index]
                i["beschreibung"]["link"].append(link[0])
                


            # Befindet sich das gesuchte Produkt nicht in der Angebote.csv, dann suche das Produkt in der allproducts.csv für den Preis.
            else:
                # find size (hier wird sonst array an sizeProd ausgegeben, deshalb [0])
                sizeProd = allproductsArray[1][np.where(allproductsArray[0] == j)][0]
                sizeRez = i["beschreibung"]["menge"][zutatenCount]

                # mögliche Einheiten sind g oder kg, l oder ml
                if sizeRez[-1] == "g" or sizeRez[-1] == "l" or sizeRez[-1] == "S":
                    if sizeRez[-2] == "k" or sizeRez[-2] == "m":
                        if sizeRez[-2] == "k" or sizeRez[-2] == "m":
                            sizeRezNum = float(sizeRez[:-2])
                    else:
                        sizeRezNum = float(sizeRez[:-1])
                
                if sizeProd[-1] == "g" or sizeProd[-1] == "l" or sizeRez[-1] == "S":
                    if sizeProd[-2] == "k" or sizeProd[-2] == "m" :
                        sizeProdNum = float(sizeProd[:-2])
                    else:
                        sizeProdNum = float(sizeProd[:-1])
                
                preis += float(allproductsArray[2][np.where(allproductsArray[0] == j)][0].replace(",", "."))*sizeRezNum/sizeProdNum
                
                index = np.where(allproductsArray[0] == j)
                link = allproductsArray[4][index]
                i["beschreibung"]["link"].append(link[0])
            i.update({'preis': round(preis, 2)})

            zutatenCount += 1
        #print(rezepte)
    return rezepte


