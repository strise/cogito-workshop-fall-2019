# Workshop med Strise

Hver dag mottar Strise 3 millioner tekstdokumenter som en strøm av data. Bare noen få av disse viser seg å være relevant for et spesifikt tema. Gjennom oppgavene i denne workshopen skal du filtrere bort irrelevante dokumenter og til sist gjøre analyse på de gjenværende dokumentene.

Tema for denne analysen er Ole Gunnar Solskjær (OGS). I desember 2018 tok han over fotballaget Manchester United, som på den tiden var i dyp krise. De hadde tatt få poeng gjennom hele høsten og lå dårlig an. De første månedene med OGS gikk svært bra, men så snudde det.

Resultatet av analysen du skal gjennomfør skal forsøke å gi et innblikk i hvordan mediene har omtalet OGS det siste året. Men før vi kan analysere må vi filtrere bort støy, slik at vi får høyere presisjon på resultatet.

## Setup
Klon eller last ned dette repoet. Dette gjøres ved å klikke på den store grønne knappen oppe til høyre, eller ved å kjøre `git clone https://github.com/strise/workshop`. 
Du trenger minimum Python 3.6 for å kjøre koden. Dersom du ikke har det kan du laste det ned [her](https://www.python.org/downloads/). 

Naviger deretter til mappen med repoet i terminalen og kjør kommandoen `pip install -r requirements.txt` for å installere avhengigheter. Kjør til slutt `python -m textblob.download_corpora` for å laste ned nødvendige modeller. Hvis du står fast her, ikke nøl med å spørre!

Til slutt må du også unzippe dataset-fila, som ligger i `/data`, slik at `dataset.csv` får stien `/data/dataset.csv`. Passord vil bli utdelt under workshopen.

### Tips om `TimestampedText`
Vi har laget en klasse som heter `TimestampedText`. Hver instans av denne klassen inneholder et tidsstempel for når teksten ble publisert, samt teksten. Ved å kalle `.words()` eller `.sentences()` på en instans vil man kunne få ord og setninger inneholdt i teksten:
```
t = TimestampedText("This is a cool text. Hello everyone!", 1545214301000)
t.words() # returns ["This", "is", "a", "cool", "text", ".", "Hello", "everyone", "!"]
t.sentences() # returns ["This is a cool text.", "Hello everyone!"]
```

## Oppgave 1 - Identifisering av søppel
Ikke alle dokumenter vi mottar har interessant innhold, og innholdsleverandøren kan ha bugs i koden sin. Vi trenger derfor funksjonalitet for å filtrere bort dokumenter som har for høy grad av støy. Støy, i denne sammenhengen, kan for eksempel være CSS-kode eller tabeller med tall. Vi ønsker altså å fjerne alle dokumenter som inneholder for mye støy.


**Oppgave:** Implementer `is_junk()`-metoden. Dersom oppgaven er ish-korrekt utført skal det være rundt 1200 artikler igjen etter junk removal.

Du kan gjerne prøve deg fram med ulike fremgangsmåter. 

<details>
  <summary>Hint</summary>
  Her er én mulig løsning dersom du er tom for inspirasjon, eller bare vil komme deg raskest mulig videre.
  
  En artikkel er _junk_ dersom det oppfyller minst ett av følgende punkter:
  
  - Gjennomsnittlig ordlengde for dokumentet er lengre enn 20 karakterer
  - Mindre enn 50 % av karakterene i dokumentet er bokstaver (ikke medregnet mellomrom)
  - Mer enn 15 % av karakterene i dokumentet er tall (ikke medregnet mellomrom)
  - Mer enn 15 % av karakterer er hverken bokstaver eller tall (ikke medregnet mellomrom)
</details>

## Oppgave 2 - Identifisering av språk
Vi mottar dokumenter på en rekke forskjellige språk. På denne workshopen ønsker vi kun å beholde engelske dokumenter. 

For å identifisere språk i et dokument er det vanlig å bruke såkalte stoppord (stopwords). Stoppord er mye brukte ord: Typiske norske stoppord er “jeg”, “du”, “han”, “og” etc. I `filter_on_language()`-metoden ligger det en variabel som heter `eng_stopwords`, som inneholder noen av de vanligste engelske ordene. 

**Oppgave:** Implementer `is_english()`-metoden. Dersom oppgaven er riktig utført skal du nå stå igjen med omkring 800 artikler.

<details>
  <summary>Hint</summary>
  
  For en liste med ord inneholdt i en engelsk artikkel burde minst 20 % av disse være stoppord.
</details>

## Oppgave 3 - Relevante setninger
Nå har vi kun dokumenter av ypperste kvalitet. Likevel er det bare deler av disse som er interessant for vår analyse av OGS i nyhetsbildet. For å undersøke hvordan mediene har omtalt OGS er vi kun interessert i setninger som handler om han. 

En setning er definert til å handle om OGS dersom den inneholder en av følgende strenger: `{"Solskjær", "Solskjaer"}`

**Oppgave:** Gjør ferdig `relevant_sentences()`-metoden. Her skal du ha rundt 2100 setninger. Om det varierer litt er det ikke så farlig.

## Oppgave 4 - Analyse
Nå er det på tide å gjøre om setninger til innsikt. Her kan du gjøre hva du vil, men vi har også noen forslag.

### Forslag 1: Sentimentanalyse
Sentimentet til en setning er et tall mellom -1 og 1 som forteller hvor negativ eller positiv en setning er. Dette vil ikke nødvendigvis stemme så godt i hvert enkelt tilfelle, men når man tar gjennomsnittet av mange slike sentiment-scores kan man få noe som er interessant å se på. 

Videre er vi interessert i å plotte gjennomsnittlig sentiment for hver uke det siste året, og se om det er noe korrelasjon mellom Manchester Uniteds prestasjoner og sentimentet rundt OGS.

Det finnes massevis av avanserte metoder for å finne sentiment for en tekst, men vi holder oss til biblioteket TextBlob. Hvis du bruker PyCharm skal det bare være nødvendig å høyreklikke på import-statementet øverst i fila, og installere. Hvis ikke kan du kjøre `pip install textblob`. Gi oss beskjed om du sliter med å installere dette, så skal vi hjelpe deg.

Når vi har TextBlob installert kan sentimentet til en setning finnes  ved å kjøre
```
blob = TextBlob(sentence)
sentiment = blob.sentiment.polarity
``` 
Merk at `generate_sentiment_scores()`-metoden inneholder funksjonalitet for å filtrere bort artikler som ble publisert før OGS startet som manager, og etter sesongen som endte 13. Mai. Dette gjøres slik at man kan plotte sentimentet til OGS mot gjennomsnittlig poeng per uke for Manchester United. Dette kan gjøers ved hjelp av  `plot_sentiment_against_utd_results()`.

### Forslag 2: Top 20 adjektiv
Finn listen over de vanligste adjektivene som befinner seg i setninger sammen med OGS. For å identifisere adjektiv må man utføre POS-tagging (part-of-speech tagging). Resultatet av POS-tagging er at hvert ord blir plassert i en grammatisk kategori. 

For setningen “Ole is doing great”, vil resultatet være `[(Ole, NNS), (is, VBZ), (doing, VBG), (great, JJ)]`. Her er en liste som forklarer hver enkelt ordklasse, men i denne oppgaven trenger du kun å forholde deg til JJ, JJR, og JJS. Disse beskriver de tre bøyningsformene til adjektiv. 

For å gjøre POS-tagging anbefales nltk:
```
import nltk
words = nltk.word_tokenize(str)
pos_tagged = nltk.pos_tag(words)
```

Variabelen `pos_tagged` inneholder nå en liste med tupler med ord og tag. 

### Forslag 3: Oftest nevnte spillere
Hvilke spillere på Manchester United blir oftest nevnt? [Her](https://www.worldfootball.net/teams/manchester-united/2019/2/) er en liste over spillerstallen for fjorårets sesong. Merk at du her må bruke resultatet fra oppgave 2, og ikke 3, for å gjøre analysen på hele artikler, og ikke bare setninger om OGS. Her er det også muligheter til å være kreativ med plotting og se om antall ganger en fotballspiller blir nevnt har endret seg over tid.

### Forslag 4: Noe kult
Finn på noe kult selv, og fortell oss gjerne hva du har funnet ut.



