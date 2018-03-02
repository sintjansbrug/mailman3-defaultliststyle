### Omschrijving

Deze python-module bevat een Mailman3-plugin met SJB-specifieke toevoegingen.
Huidige content:

* SJBStyle, default style voor nieuwe lijsten met goede configuratie

De module zit automatisch in het python3.6 path vanwege een symlink in /usr/local/lib/python3.6/site-packages/ naar deze repo.

### Vereisten

* Mailman 3.2.0a1, draaiend op python3.6

### Installatieprocedure
Om te installeren, volg de volgende stappen:

1. Clone deze repo naar je favoriete folder
2. Zorg dat deze in je python3.6 path komt, bijvoorbeeld met een symlink naar deze repo:
   * Commando: `ln -s /pad/naar/je/folder /python3.6/library/path/sjb-mailman3`
3. Voeg het volgende toe aan je mailman3 config:
   * Om de plugin te laden: 
      ```
      # Imports SJB-plugin
      [plugin.sjb-mailman3]
      class: sjb-mailman3.plugin.SJBMM3Plugin
      enabled: yes
      ```
      Om de lijst default ook te gebruiken:
      ```
      # Sets default list style to sjb-style
      [styles]
      default: sjb-list-style
      ```
4. Herstart mailman
