# Linux OS
I dag skal i have installeret Linux og i skal arbejde med operativsystemet gennem dets terminal.

**Motivation**: stort set alt vi kommer til at arbejde med dette semester bliver udført gennem jeres terminal. Linux er det rigtige sted at lære om brugen af denne. Alle servere vi kommer til at arbejde med er Linux servere og den eneste adgang til disse er gennem terminalen. 

## Learning Goals
* Installere Linux gennem Docker på din computer.
* Bruge Linux OS gennem dens terminal.
* Få et praktisk overblik over de hyppigst brugte shell kommandoer.
* Forstå Linux´s fil og mappestruktur.
* Kunne installere applikationer i dit linux system.
* Forstå hvad en package manager er og gør.
* Kunne bruge en terminal baseret texteditor (nano)
* Kunne eksevere applikationer (python) på din linux computer.

## Before Class

Den linux distibution vi skal bruge i undervisningen skal installeres gennem docker. Det kan godt tage lidt tid at få det hele downloaded, så derfor skal i køre denne kommando inden i møder op til undervisningen. 


```
docker run -d --name=webtop-ubuntu-mate --security-opt seccomp=unconfined  -e PUID=1000 -e PGID=1000 -e TZ=Etc/UTC -e SUBFOLDER=/  -e TITLE=ITADevOps -p 3000:3000 -p 3001:3001 -v /var/run/docker.sock:/var/run/docker.sock  --shm-size="1gb"  --restart unless-stopped lscr.io/linuxserver/webtop:ubuntu-mate
``` 


Se og følg tutorials i de tre videoer:

* [Linux for Hackers // EP 1](https://www.youtube.com/watch?v=VbEx7B_PTOE&list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL) (11:32)
* [the Linux File System explained in 1,233 seconds // Linux for Hackers // EP 2](https://www.youtube.com/watch?v=A3G-3hp88mo&list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL&index=2) (20:32)
* [HELP!! (for when you suck at Linux) // Linux for Hackers // EP3](https://www.youtube.com/watch?v=Y17KTiJLcyQ&list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL&index=3) (13:13)

## Today's Teachings

## Weekly DevOps Principle
### The Principle og Flow 
_(DevOps Handbook p. 54-61)_

* **Make your work visible**
    * Git
    * public GitHub and good commit messages
    * Kanban
    * Project
    * Release
    * groups.py
        * LECENSE
    * other? 
* **Limit Work in Process (WIP)**
    * Small tasks, and end them before going on to new one.
* Reduce Batch size

**Show your work!**

## Status
* Hvor langt er i kommet?
* Jeg har registret 3 grupper, mangler fra 2
    * [Den Danske Metode](https://github.com/DenDanskeMetode/legacyProject)
    * [TheRizzlers](https://github.com/TheRizzlersOrg4Semester/Rizzlerpies)
    * [LNS](https://github.com/Linus-nisse-segmentering/linus-kogebog)

1. Framework kode, konvertering?
2. Kanban?

**Opgave**: Opdater groups.py med jeres stack informationer, og lav et PR. 

OpennAPI specifikationerne fra sidst i forhold til Legacy projektet. 

* [OpenAPI](../02._decide_framework_convert_code/03._openapi.md)
* [api-schema.yaml](../02._decide_framework_convert_code/api-schema.yaml)
* [Awesome Recipe Cookbook](https://github.com/cookbookio/awsome_recipe_cookbook/tree/openapi) 

## Linux
Efter dette arbejder vi med Linux resten af dagen og på fredag.       

* [Linux terminal commands and file system](unix_commands.md)

**Opgave**: 

    * Gå til jeres "Documents" folder
    * lav en ny mappe og kald den "DevOps"
    * i denne mappe lave en txt fil med navnet "show_your_work.txt"
    * i samme mappe lav en markdownfil med navnet "WIP.md"
    * i samme mappe lav en imagefile  med navnet "cat_on_a_roof_top.png"
    * gå tilbage i Documents mapppen og copy DevOps mappen til Documents mappens "parrent" (Home)
    * gå til denne nye mappe og slet png filen
    * slet hele DevOps mappen i documents mappen

## After Class

Lav øvelserne: 

* Øvelse: [Unix Command Exercises](unix_commands_exercises.md)
* Øvelse: Kør din gruppes CookBook applikation på din linux computer
    * Du kan **ikke** køre docker containere i din Linux installation, da den allerede kører i en docker container. 
    * Men du kan godt køre din applikation lokalt på denne installation, så bare hop ud i det.
    * Lav en ændring i din kode (brug nano)
    * Push til github
* Øvelse: Stadig fra din linux maskine og stadig kun gennem terminalen
    * Tilføj en ny linje i jeres gruppes dictionary i groups.py filen med Key, value som dette: "linux": True
    * Lav et commit og push til jeres gruppes repository. (i kan godt alle gøre dette)
    * Stadig fra terminalen; lav et PR til "EK_ITA_Agil_Cloud_Ita_2026_Spring" (Hint: `gh`)
Hvis du skulle blive færdig før timen er overstået skal du blive ved med at lege med systemet indtil du rammer en time!

