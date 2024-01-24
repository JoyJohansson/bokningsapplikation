Feature: Bokningssystem - Kund

    Scenario: Söka efter tillgängliga rum 
    Scenario: Filtrera tillgängliga rum efter preferenser
    Scenario: Boka ett rum
    Scenario: Fyller i kunduppgifter
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
            Som kund kan jag fylla i mina uppgifter så att jag får min bokningsreferens.
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
    När jag trycker på "boka rum"-knappen
    Så kommer jag till en sammanfattning av min bokning

Scenario: Fyller i kunduppgifter

Som kund kan jag fylla i mina uppgifter så att jag får min bokningsreferens.

    Givet att jag ser sammanfattning av min bokning
    Och att jag ser ett fält där jag kan fylla i min emailaddress
    Och att jag har en emailaddress
    När jag fyller i min emailaddress i fältet
    Så får jag alternativ att bekräfta bokning
    

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

Som kund kan jag avboka ett rum så att jag inte längre behöver betala för ett rum jag inte övernattar i.

    Givet att jag har en bekräftad bokning
    Och är på hotellets avbokningshemsida
    Och att jag önskar att avboka
    Och att jag har bokningsreferens
    När jag trycker på "Avbokning"-knappen
    Så presenteras ett fält där jag kan fylla i bokningsreferens


Scenario: Göra tillval "extra"

