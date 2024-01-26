Feature: Bokningssystem - Kund

    Scenario: Söka efter tillgängliga rum 
    Scenario: Filtrera tillgängliga rum efter preferenser
    Scenario: Redigera en bokning
    Scenario: Avboka ett rum
    Scenario: Omboka ett rum
    
    Scenario: 

        User Story:
            Som kund kan jag söka efter rum så att jag kan se tillgängligheten.
            Som kund kan jag filtrera tillgängliga rum efter mina preferenser så att jag kan se rum som passar mig.
            Som kund kan jag boka ett rum så att jag har någonstans att övernatta.
            Som kund kan jag redigera en bokning så att jag kan ändra mina preferenser. 
            Som kund kan jag avboka ett rum så att jag inte längre behöver betala för ett rum jag inte övernattar i.
            Som kund kan jag göra en ombokning så att jag kan ändra min bokning.    
            
Feature: Kund söker rum

Som kund kan jag söka efter rum så att jag kan se tillgängliga rum.

    Givet att jag är på hotellets hemsida
    När jag fyller i mellan vilka datum min vistelse gäller
    Och hur många personer som ska bo i rummet
    Och klickar på "Sök"
    Så visas en lista med tillgängliga rum

Feature: Kund väljer rum




Feature: Kund bokar rum

Som kund kan jag boka ett rum så att jag har någonstans att övernatta.

Scenario: Boka ett rum

    Givet att jag har valt ett lämpligt rum
    Och angivit mina preferenser 
    När jag trycker på "boka rum"-knappen
    Så ska en ny sida med en sammanfattning av min bokning visas 









Scenario: Göra tillval "extra"

