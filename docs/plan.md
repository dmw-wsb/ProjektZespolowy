<!-- _class: lead -->
# Techniczne aspekty i role w projekcie
DevOps Dominik Gadomski<br />
FrontEnd Filip Jakubczak<br />
BackEnd Damian Wyrbiński 
<!-- _class: lead -->
## Podstawowe pytania
<br />

Chcemy stworzyć aplikację dla alergików, aby ci mieli łatwy dostęp do infomacji czy powinni dzisiaj wziąć leki czy też może lepiej żeby zostali w domu.<br />
Chcemy ją stworzyć żeby ułatwić życie alergiką <br />
Chcemy to stworzyć z wykorzystaniem Serverlessowych serwisów w AWSie
- -&gt; design doc.

---
<!-- _class: lead -->
## Metody wytwarzania oprogramowania
<br>

- Scrum
- Narzędzia do trackowania tasków (nie wiem),

---
<!-- _class: lead -->
# Komunikacja

Ustalenie:

- chat (discord)
- syncs, project meetings,
- github (workflow),
- board.

---
<!-- _class: lead -->
## Metoda dostarczania nowych wersji
<br />

- CI/CD with circleCI,
- github workflow.

---
<!-- _class: lead -->
## Podstawowa architektura aplikacji
<br />

- Wstępne ustalenie stacku technologicznego:
- AWS Lambda, Amazon S3, Amazon DynamboDB, html
- AWS Lambda,
- Serverless
- -&gt; architektura (draw.io),
- -&gt; design doc.

---
<!-- _class: lead -->
## Skalowalność
<br />

- Czy spodziewamy się zmiennej ilości użytkowników?
- TAK aplikacja jest serverlessowa więc dla nas skalowalność jest high priority
- Czy zmienność może mieć charakter okresowy, czy raczej będzie to jednorodny trend?
- Będzie to okresowa zmienność ze względu na sezony pyleń
- Czy potrzebujemy niezależnego skalowania komponentów aplikacji?
- Nie
- Napkin math &amp; perf testing

-&gt; design doc

---
<!-- _class: lead -->
## Elementy aplikacji
<br />

- Frontend HTML
- Backend AWS Lambda
- Bazy Danych DynamoDB
- Warstwa serwerowa Brak
- Warstwa sieciowa Brak

---
<!-- _class: lead -->
# Podział na role
DevOps
FrontEnd
BackEnd
---
<!-- _class: lead -->
## Role w projekcie
<br />

DevOps Dominik Gadomski<br />
FrontEnd Filip Jakubczak<br />
BackEnd Damian Wyrbiński 

---
<!-- _class: lead -->
## Dziękuję za uwagę
<br />
