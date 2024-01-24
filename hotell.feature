Feature: Inloggning - Hotell

    "Som användare ska jag kunna logga in, så jag kan få tillgång till det administrativa"

    Scenario: Logga in på hotellets webbportal
    Givet att jag är på www.crazyfroghotellet.com startsida
    Och är ansluten till databasen för hotellets bokningsystem
    När jag klickar på 'login' -knappen
    Och jag skriver in giltigt användarmnamn
    Och giltigt lösenord
    Och klickar på 'logga in' -knappen
    Så ska jag loggas in

Feature: Administration för rum hantering - Hotell
    
    "Som användare ska jag kunna se vilka rum som är bokade på ett visst datum så att jag kan planera inför kundens ankomst."
    
    Background:
    Givet att jag har giltigt konto
    Och att jag är inloggad
    Och att jag är ansluten till databasen för hotellets bokningsystem
    

    Scenario: Se bokade rum
    När jag klickar på 'Se bokade rum' -knappen
    Så vill jag se en lista för bokade rum

    
    Scenario Outline: Visa lista över bokade rum
    Så bör jag se följande bokade rum:
    | Rumsnummer | Datum       | Gäst       |
    | <Rumsnummer>| <Datum>    | <Gäst>     |

    

    Scenario: Göra en bokning & se tillgängliga rum
    När jag klickar på 'Se tillgängliga rum' -knappen
    Så vill jag se en lista för lediga rum
    
    Scenario Outline: Visa lista över lediga rum
    Så bör jag se följande lediga rum:
    | Rumsnummer  | rumstyp  | pris   |
    | <Rumsnummer>| <rumstyp | <pris> |
    

    Scenario: Göra en bokning
    Givet att jag är på 'Se tillgänliga rum' -sidan
    När 
    Så kan jag göra en bokning på tillgänliga rum från listan
    Och


    Scenario: Redigera en bokning
    Scenario: Avbokning av ett rum
    Scenario: Ombokning av ett rum
    

    

    
        User story: 
            
            
            
            Som hotellreceptionist kan jag göra en bokning åt kunden så att jag kan förmedla service till drop-in gäster.
            Som hotellreceptionist kan jag redigera en bokning så att jag kan anpassa efter kundensönskemål.  
            Som hotellreceptionist kan jag göra en avbokning av ett rum så att kunden kan ha fler avbokningsalternativ.
            Som hotellreceptionist kan jag göra en ombokning av ett rum så att jag kan anpassa servicen efter behov. 

        
Frågor till gruppen
"Som användare kan jag se vilka rum som är tillgängliga så att jag kan se hur stor beläggning verksamheten har."

Feature: Tillval - Hotell
