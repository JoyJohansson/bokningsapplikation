Feature: Bokningssystem - Kund

    Scenario: Söka efter tillgängliga rum 
    Scenario: Filtrera tillgängliga rum efter preferenser
    Scenario: Tillägsval - bokning
    Scenario: Boka ett rum
    Scenario: Bekräfta bokning
    Scenario: Redigera en bokning (först relevant efter tillval??)
    Scenario: Avboka ett rum
    Scenario: Bekräfta avbokning
    Scenario: Omboka ett rum
    Scenario: Bekräfta ombokning
    Scenario: Redigera tillval i en bokning


        User Story:
            Som kund kan jag söka efter rum så att jag kan se tillgängligheten.
            Som kund kan jag filtrera tillgängliga rum efter mina preferenser så att jag kan se rum som passar mig.
            Som kund kan jag göra tillägsval i min bokning så att jag får med de bekvämligheter jag vill ha
            Som kund kan jag boka ett rum så att jag har någonstans att övernatta.
            Som kund kan jag bekräfta en bokning så att jag får rummet jag önskar.
            Som kund kan jag redigera en bokning så att jag kan ändra mina preferenser. 
            Som kund kan jag avboka ett rum så att jag inte debiteras.
            Som kund kan jag bekräfta avbokning så att jag inte debiteras.
            Som kund kan jag göra en ombokning så att jag kan ändra min bokning.    
            Som kund kan jag bekräfta min ombokning så att jag vet att ändringen är gjord.
            Som kund kan jag redigera en bokning så att jag kan ändra mina preferenser. 
            
Scenario: Söka efter tillgängliga rum 

Som kund kan jag söka efter rum så att jag kan se tillgängligheten.

    Givet att jag är på hotellets hemsida
    Och att jag vill söka efter rum att boka
    När jag fyller i fältet "incheckningsdatum" 
    Och  jag fyller i fältet"utcheckningsdatum"
    Och jag fyller i fältet "antal personer"
    Och jag klickar på "Sök"-knappen
    Så visas en lista med tillgängliga rum
   

Scenario: Filtrera tillgängliga rum efter preferenser

Som kund kan jag filtrera tillgängliga rum efter mina preferenser så att jag kan se rum som passar mig.

    Givet att jag ser en lista över tillgängliga rum 
    Och att jag presenteras med alternativa preferenser som jag kan kryssa i     * infoga boxalternativ*
    När jag kryssa i boxen/boxarna "alternativ 1" (osv)  *infoga valalternativen*
    Och jag klickar på "Filtrera"-knappen
    Så presenteras jag med en ny lista med lediga rum efter mina valda preferenser
    Och jag väljer ett rum jag vill boka


Scenario: Tilläggsval - bokning

Som kund kan jag göra tillägsval i min bokning så att jag får med de bekvämligheter jag vill ha

    Givet att jag har valt ett rum
    När jag lagt till mina önskemål om tillval *infoga tabell*
    Och trycker på "Gå vidare"-knappen
    Så ser jag mina tillagda val i bokningssammanfattningen


Scenario: Boka ett rum

Som kund kan jag boka ett rum så att jag har någonstans att övernatta.

    Givet att jag ser bokningssammanfattningen
    Och att jag vill boka rummet med tillvalen
    När jag fyller i min emailaddress i "E-mail"-fältet
    Och jag trycker på "boka rum"-knappen
    Så skickas ett mail till min emailadress med länk för att bekräfta bokningen
    

Scenario: Bekräfta bokning

Som kund kan jag bekräfta en bokning så att jag får rummet jag önskar.

    Givet att jag fyllt i rätt emailaddress
    Och att jag vill genomföra bokningen
    Och att jag tryckt på länken i mailet
    Och omdirigerats till sidan för bekräftelse av bokning 
    När jag trycker på "Bekräfta Bokning"-knappen 
    Så ser jag ett meddelande "Bokningen är bekräftad"
    Och får ett email med bekräftelse och bokningsreferens.

    
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


Scenario: Hämta bokingingsreferens för att redigera en bokning

Som kund kan jag hämta bokingingsreferens så att jag kan redigera en bokning.

    Givet att jag är på hotellets redigeringshemsida
    Och att jag har en bekräftad bokning
    Och att jag vill göra ändringar i min bokning
    Och att jag har en bokningsreferens
    När jag fyller i min bokningsreferens i fältet "Bokningsreferens"
    Och jag trycker på "Redigera"-knappen
    Så ser jag en sida med fält med alternativa tillägg för bokningen  *tabell*

                "kan man ha två sekvenser till en user story"

Scenario: Redigera tillval i en bokning (efter tillval?)

Som kund kan jag redigera en bokning så att jag kan ändra mina preferenser. 


    Givet att jag är på sidan med alternativa tillägg för bokningen
    När jag fyller i fälten med det som jag vill ändra på i bokningen *tabell*
    Och trycker på "Spara"-knappen
    Så får jag ett meddelande "Ändringar sparat" på skärmen
    Och jag får en bekräftelse på mina ändringar per mail.     
