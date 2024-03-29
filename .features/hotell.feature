Feature: Inloggning - Hotell

    "Som anställd ska jag kunna logga in som admin, så jag kan få tillgång till det administrativa"

    Scenario: Logga in på hotellets webbportal
    Givet att jag är på hotellets startsida
    Och har giltigt konto för hotellets bokningsystem
    När jag klickar på 'login'-knappen
    Och jag skriver in användarmnamn i 'användarfältet'
    Och jag skriver in lösenord i 'lösenordsfältet'
    Och jag klickar på 'logga in'-knappen
    Så ska jag loggas in
    Och få tillgång till Administration-sidan

Feature: Administration för rum hantering - Hotell
        
    Background:
    Givet att jag har giltigt konto
    Och att jag är inloggad
    
        "Som anställd ska jag kunna se vilka rum som är bokade på ett visst datum så att jag kan planera inför kundens ankomst."

    Scenario: Se bokade rum
    Givet att jag är på hotelletssida
    När jag klickar på 'Se bokade rum' -knappen
    Så ska jag se en lista över bokade rum
    


        "Som anställd kan jag se vilka rum som är tillgängliga så att jag kan se hur stor beläggning verksamheten har."

    Scenario: se tillgängliga rum
    Givet att jag är hotelletssida 
    När jag klickar på 'se tillgängliga rum' -knappen
    Så vill jag se en lista över tillgängliga rum
    
        
        'Som anställd kan jag göra en bokning åt kunden så att jag kan förmedla service till drop-in gäster.'

    Scenario: Göra en bokning
    Givet att jag är på bokningssidan
    Och att det finns tillgängliga rum
    Och att en kund vill göra en bokning
    Och att det finns en bokningsformulär
    När jag klickar på 'se tillgängliga rum' knappen
    Och jag får upp en lista över tillgängliga rum
    Och att klickar på det rum som kunden önskat
    Och jag klickar på 'fyll i bokningsformulär' knappen
    Och jag fyller i kundens uppgifter
    Så klickar jag 'boka rum' knappen
    Och få en bekräftelse på bokningen av kunden

    
        'Som anställd kan jag redigera en bokning så att jag kan anpassa efter kundensönskemål.'  

    Scenario: Redigera en bokning
    Givet att jag är på bokningssidan
    Och det finns en aktiv bokning
    Och det finns en kund som önskar att redigera sin bokning
    När jag klickar på 'se bokning' knappen
    Och jag klickar på 'redigera bokning' knappen
    Så kan jag redigera bokningen baserat på kundens önskemål
    Och få en bekräftelse av kunden



        'Som anställd kan jag göra en avbokning av ett rum så att kunden kan ha fler avbokningsalternativ.'

    Scenario: Avbokning av ett rum
    Givet att jag är på bookningssidan
    Och det finns en aktiv bokning
    Och det finns en kund som önskar att göra en avbokning
    När jag klickar på 'se bokning' knappen 
    Så kan jag klicka på 'avboka rum' knappen
    Och få en bekräftelse av kunden


        'Som anställd kan jag göra en ombokning av ett rum så att jag kan anpassa servicen efter behov.'

    Scenario: Ombokning av ett rum
    Givet att jag är på bokningssidan
    Och det finns en aktiv bokning
    Och det finns en kund som önskar att göra en ombokning
    När jag klickar på 'se bokning' knappen 
    Så kan jag klicka på 'omboka rum' knappen
    Och få en bekräftelse av kunden

    

    
        User story: 
            
            
            
            Som anställd kan jag göra en bokning åt kunden så att jag kan förmedla service till drop-in gäster.
            Som anställd kan jag redigera en bokning så att jag kan anpassa efter kundensönskemål.  
            Som anställd kan jag göra en avbokning av ett rum så att kunden kan ha fler avbokningsalternativ.
            Som anställd kan jag göra en ombokning av ett rum så att jag kan anpassa servicen efter behov. 

        
Frågor till gruppen
"Som anställd kan jag se vilka rum som är tillgängliga så att jag kan se hur stor beläggning verksamheten har."
 Som anställd ska jag kunna se en lista över tillgängliga rum Så att jag kan göra en bokning.

Feature: Tillval - Hotell
