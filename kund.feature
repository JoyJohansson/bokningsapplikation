Feature: Bokningssystem - Kund

    Scenario: Söka efter tillgängliga rum 
    Scenario: Filtrera tillgängliga rum efter preferenser
    Scenario: Boka ett rum
    Scenario: Bekräfta bokning
    Scenario: Redigera en bokning (först relevant efter tillval??)
    Scenario: Avboka ett rum
    Scenario: Bekräfta avbokning
    Scenario: Omboka ett rum
    Scenario: Bekräfta ombokning
    
    Scenario: 

        User Story:
            Som kund kan jag söka efter rum så att jag kan se tillgängligheten.
            Som kund kan jag filtrera tillgängliga rum efter mina preferenser så att jag kan se rum som passar mig.
            Som kund kan jag boka ett rum så att jag har någonstans att övernatta.
            Som kund kan jag bekräfta en bokning så att jag får rummet jag önskar.
            Som kund kan jag redigera en bokning så att jag kan ändra mina preferenser. 
            Som kund kan jag avboka ett rum så att jag inte debiteras.
            Som kund kan jag bekräfta avbokning så att jag inte debiteras.
            Som kund kan jag göra en ombokning så att jag kan ändra min bokning.    
            Som kund kan jag bekräfta min ombokning så att jag vet att ändringen är gjord.
            
Scenario: Söka efter tillgängliga rum 

Som kund kan jag söka efter rum så att jag kan se tillgängligheten.

    Givet att jag är på hotellets hemsida
    När jag fyller i mellan vilka datum min vistelse gäller
    Och hur många personer som ska bo i rummet
    Och klickar på "Sök"-knappen
    Så visas en lista med tillgängliga rum
    Och alternativ för preferenser presenteras

Scenario: Filtrera tillgängliga rum efter preferenser

Som kund kan jag filtrera tillgängliga rum efter mina preferenser så att jag kan se rum som passar mig.

    Givet att jag ser en lista över tillgängliga rum med alternativ för preferenser
    När jag fyller i mina preferenser *infoga tabell*
    Och klickar på "Filtrera"-knappen
    Så ser jag en ny lista med lediga rum efter mina preferenser



Scenario: Boka ett rum

Som kund kan jag boka ett rum så att jag har någonstans att övernatta.

    Givet att jag ser en lista med lediga rum efter mina preferenser
    Och att jag har hittat ett rum jag vill boka
    Och har markerat önskat rum
    När jag fyller i min emailaddress i "E-mail"-fältet
    Och jag trycker på "boka rum"-knappen
    Så kommer jag till en sammanfattning av min bokning
    

Scenario: Bekräfta bokning

Som kund kan jag bekräfta en bokning så att jag får rummet jag önskar.

    Givet att jag fyllt i rätt emailaddress
    Och att jag vill genomföra bokningen
    När jag trycker på "Bekräfta Bokning"-knappen
    Så ser jag ett meddelande "Bokningen är bekräftad"
    Och får ett email med bekräftelse och bokningsreferens.

Scenario: Redigera en bokning (efter tillval?)

Som kund kan jag redigera en bokning så att jag kan ändra mina preferenser. 

    Givet att jag har en bekräftad bokning
    

Scenario: Avboka ett rum

Som kund kan jag avboka ett rum så att jag inte debiteras.

    Givet att jag har en bekräftad bokning
    Och är på hotellets avbokningshemsida
    Och att jag önskar att avboka
    Och att jag har bokningsreferens
    När jag fyllt i min emailadress i fältet för "E-mail"
    Och jag fyllt i min bokningsreferens i fältet "Bokningsreferens"
    Och jag trycker på "Avboka"-knappen
    Så ser jag detaljer från bokningen.

Scenario: Bekräfta avbokning

Som kund kan jag bekräfta avbokning så att jag inte debiteras.

    Givet att jag ser detljerna för bokningen
    Och att jag vill avboka
    När jag trycker på "Bekräfta avbokning"-knappen
    Så ser jag ett meddelande "Avbokat"
    Och får ett email med bekräftelse på avbokningen.

Scenario: Omboka ett rum

Som kund kan jag göra en ombokning så att jag kan ändra min bokning. 

    Givet att jag är på hotellets ombokningssida
    Och att jag har en bekräftad bokning
    Och att jag vill göra en ombokning
    Och att det finns passande rum tillgängliga
    Och att jag vet hur många gäster vi är
    När jag fyller i bokningsreferens i fältet "Bokningsreferens"
    Och jag fyller i önskad vistelseperiod i "När vill du boka"
    Och jag fyller i antal gäster i fältet "Antal gäster"
    Och trycker på knappen "Omboka"
    Så ser jag en lista över rum som överensstämmer med mina preferenser som är tillgängliga

Scenario: Göra tillval "extra"

