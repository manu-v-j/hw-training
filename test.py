import requests

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json+protobuf',
    'origin': 'https://shop.rewe.de',
    'priority': 'u=1, i',
    'referer': 'https://shop.rewe.de/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-browser-channel': 'stable',
    'x-browser-copyright': 'Copyright 2025 Google LLC. All rights reserved.',
    'x-browser-validation': 'onHIqyUSYwlqe77GwAvZSAO7PjU=',
    'x-browser-year': '2025',
    'x-goog-api-key': 'AIzaSyATBXajvzQLTDHEQbcpq0Ihe0vWDHmO520',
}

data = '[[["rewe.de","Anmelden","PLZ 80331","Märkte &amp; Angebote","Lieferservice","ändern","Rezepte &amp; Ernährung","<a i=0>Liefertermin </a><a i=1>wählen</a>"," Favoriten\\n                                ","0,00 €","Sortiment","Deine Produkte","Angebote","Mengenrabatt","Tiefpreis","Bio","Regional","Neu","Shop Startseite","Fleisch &amp; Fisch","Fleisch","Fleischalternativen","Wurst &amp; Aufschnitt","Fisch &amp; Meeresfrüchte","<a i=0>653</a><a i=1> Produkte</a>","Alle Filter","REWE Bonus","2","9","125","76","Vegan","122","1","REWE Regional Hähnchen Innenbrustfilet 350g","W","350g (1 kg = 14,26 €)","4,99 €","Gesponsert","The Vegetarian Butcher Vegane Beflügel-Nuggets 180g","180g (1 kg = 17,72 €)","3,19 €","Regionale Fleisch- &amp; Wurstwaren","Entdecke Fleisch &amp; Wurst aus deiner Region","Toni M No Tuna Salad Brotaufstrich vegan 125g","125g (1 kg = 23,92 €)","2,99 €","REWE Bio Hähnchenbrustfilet 70g","70g (1 kg = 39,86 €)","Ab 3 Stück 5% sparen","2,79 €","The Vegetarian Butcher Veganes Hick-Hack-Hurra 180g","The Vegetarian Butcher Wie&#39;n Schnitzel vegan 180g","Toni M No Tuna Pflanzlicher Thunfisch vegan 125g","REWE Bio Rinderhackfleisch 400g","400g (1 kg = 22,48 €)","8,99 €","The Vegetarian Butcher Chick-Eria Filets vegan 180g","180g (1 kg = 16,61 €)","<a i=0>bis </a><a i=1>10.08.2025</a>","REWE Bio + vegan Tofu Natur 2x200g","2x200g (1 kg = 5,48 €)","2,19 €","REWE Beste Wahl Delikatess-Metzgerschinken 150g","150g (1 kg = 19,93 €)","REWE Bio Wiener Würstchen 200g","200g (1 kg = 16,45 €)","3,29 €","REWE Regional Hähnchen Geschnetzeltes 400g","400g (1 kg = 14,98 €)","5,99 €","REWE Regional Rinderhackfleisch 500g","500g (1 kg = 15,96 €)","7,98 €","REWE Bio Bacon-Würfel Schwein 80g","80g (1 kg = 19,88 €)","1,59 €","REWE Feine Welt Salami Ciatore 80g","80g (1 kg = 41,13 €)","REWE Regional Hähnchenbrustfilet 550g","550g (1 kg = 14,53 €)","7,99 €","Herta Finesse Hähnchenbrust ofengebacken 100g","100g (1 kg = 25,90 €)","2,59 €","REWE Bio Kochschinken 100g","100g (1 kg = 28,90 €)","2,89 €","Deutsche See Lachsfilet 250g","250g (1 kg = 25,96 €)","6,49 €","REWE Bio + vegan Räucher-Tofu 2x175g","2x175g (1 kg = 6,26 €)","Wiesenhof Geflügel-Mortadella 100g","100g (1 kg = 14,90 €)","1,49 €","REWE Bio Geflügel Wiener 200g","200g (1 kg = 19,95 €)","3,99 €","REWE Bio Bacon 100g","100g (1 kg = 19,90 €)","1,99 €","Herta Finesse Schinken hauchzart und feinwürzig 100g","REWE Bio Hähnchenbrustfilet ca. 320g","1 Stück ca. 320 g (1 kg = 34,90 €)","11,17 €","Einfach Bio Rinder-Hackfleisch 400g","400g (1 kg = 15,73 €)","6,29 €","Ponnath Prosciutto Cotto 150g","REWE Bio Salami 70g","70g (1 kg = 25 €)","1,75 €","REWE Bio Original Nürnberger Rostbratwürstchen 8 Stück 160g","160g (1 kg = 21,81 €)","3,49 €","REWE Bio Wurst Paprika Lyoner 100g","Zimmermann Münchner Weißwürste 5x60g","5x60g (1 kg = 11,30 €)","3,39 €","Wilhelm Brandenburg Wiener Würstchen 150g","150g (1 kg = 13,27 €)","Herta Finesse Putenbrust im Ofen gegrillt 100g","REWE Feine Welt Prosciutto Cotto 100g","100g (1 kg = 44,90 €)","4,49 €","Reinert Schinken Nuggetz 3x50g","REWE Regional Rinderhackfleisch 250g","250g (1 kg = 15,96 €)","Aoste Stickado Salami Sticks Classique 70g","70g (1 kg = 35,57 €)","2,49 €","<a i=0>Rügenwalder Mühle Veganer Schinken Spicker mit Grillgemüse 80g</a><a i=1>...</a>","Rügenwalder Mühle Veganer Schinken Spicker mit Grillgemüse 80g"],"de","en"],"te_lib"]'.encode()

response = requests.post('https://translate-pa.googleapis.com/v1/translateHtml', headers=headers, data=data)
print(response.text)