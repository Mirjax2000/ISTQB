"""otázky pro testování ISTQB Foundation Level A"""

QUESTIONS = [
    {
        "id": 1,
        "text": "Které z následujících tvrzení popisuje [bold]správný cíl[/bold] testování?",
        "options": {
            "a": "[bold]Prokázat[/bold], že testovaný systém neobsahuje žádné neopravené defekty.",
            "b": "[bold]Prokázat[/bold], že po nasazení systému do produkce nedojde k selháním.",
            "c": "[bold]Snížit[/bold] úroveň rizika testovaného objektu a vybudovat důvěru v úroveň kvality.",
            "d": "[bold]Ověřit[/bold], že neexistují žádné netestované kombinace vstupů.",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": "(a) Není správně. Není možné prokázat, že v testovaném systému již nejsou žádné další defekty. (viz princip testování 1)\n"
        "(b) Není správně. (viz princip testování 7)\n"
        "[gold1](c) Je správně.[/gold1]  [white bold]Testování odhaluje defekty a selhání, což snižuje míru rizika a zároveň dává větší důvěru v úroveň kvality testovaného objektu[/white bold]\n"
        "(d) Není správně. Není možné otestovat všechny kombinace vstupů (viz princip testování 2)\n",
    },
    {
        "id": 2,
        "text": (
            "Které z následujících tvrzení je příkladem [bold]testovacích[/bold] činností, které přispívají k úspěchu?"
        ),
        "options": {
            "a": (
                "Zapojení testerů do různých činností životního cyklu vývoje softwaru (SDLC) pomůže odhalit defekty v pracovních produktech."
            ),
            "b": (
                "Testeři se snaží nerušit vývojáře při programování, takže vývojáři vytváří lepší kód."
            ),
            "c": (
                "Testeři spolupracující s koncovými uživateli pomáhají zlepšovat kvalitu reportů o defektech během integračního testování komponent a systémového testování."
            ),
            "d": (
                "Certifikovaní testeři navrhnou mnohem lepší testovací případy než necertifikovaní testeři."
            ),
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1]  [white bold]Je důležité, aby testeři byli zapojeni v rámci životního "
            "cyklu vývoje softwaru (SDLC) od samotného začátku, což umožňuje lépe porozumět rozhodnutím souvisejících s návrhem a zároveň včas odhalit defekty.[/white bold]\n"
            "(b) Není správně. Vývojáři i testeři budou lépe rozumět svým pracovním produktům a způsobu testování kódu.\n"
            "(c) Není správně. Koncoví uživatelé nepomohou testerům zvýšit kvalitu reportů o defektech, zároveň se obvykle neúčastní testování v nízkých úrovních jako je například integrační testování\n"
            "(d) Není správně. Certifikace automaticky neznamená, že tester bude lepší při návrhu testů\n"
        ),
    },
    {
        "id": 3,
        "text": (
            "Byli jste přiřazeni jako tester do týmu, který inkrementálně vytváří nový systém. Všimli jste si, že [bold]nebyly[/bold] po několik iterací provedeny "
            "žádné změny ve stávajících testovacích případech regresních testů a [bold]nebyly[/bold] identifikovány žádné nové regresní defekty. "
            "Váš manažer je spokojený, ale vy ne. Který [bold]princip testování[/bold] vysvětluje vaši skepsi?"
        ),
        "options": {
            "a": "Testy se opotřebovávají.",
            "b": "Nepřítomnost defektů je klam.",
            "c": "Shlukování defektů.",
            "d": "Kompletní testování není možné.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": "[gold1](a) Je správně.[/gold1]  [white bold]Tento princip říká, že pokud se stejné testy opakují stále dokola, nenajdou nakonec žádné nové defekty. To je pravděpodobně důvod, proč v tomto vydání všechny testy prošly.\n[/white bold]"
        "(b) Není správně. Tento princip říká, že pouhé nalezení a oprava velkého počtu defektů nezajistí úspěch systému.\n"
        "(c) Není správně. Tento princip říká, že malý počet komponent obvykle obsahuje většinu defektů.\n"
        "(d) Není správně. Tento princip říká, že otestování všech kombinací vstupů a vstupních podmínek není proveditelné.\n",
    },
    {
        "id": 4,
        "text": (
            "Pracujete v týmu, který vyvíjí mobilní aplikaci pro objednávání jídla. V aktuální iteraci se tým rozhodl implementovat funkcionalitu platby. Která z [bold]následujících činností je součástí testovací analýzy?[/bold]"
        ),
        "options": {
            "a": (
                "Odhad, že testování integrace s platební službou bude trvat 8 člověkodnů."
            ),
            "b": (
                "Rozhodnutí, že by tým měl otestovat, zda je možné korektně rozdělit platbu mezi více uživatelů."
            ),
            "c": (
                "Použití analýzy hraničních hodnot (BVA) k odvození testovacích dat pro testovací případy, které kontrolují správné zpracování plateb pro minimální povolenou částku pro placení."
            ),
            "d": (
                "Analýza rozporu mezi skutečným výsledkem a očekávaným výsledkem a nahlášení defektu po provedení testovacího případu, který kontroluje proces platby kreditní kartou."
            ),
        },
        "correct": ["b"],
        "points": 1,
        "explanation": "(a) Není správně. Odhad pracnosti testování je součástí [bold]plánování testování.[/bold]\n"
        "[gold1](b) Je správně.[/gold1]  [white bold]Toto je příklad definice testovacích podmínek, které jsou součástí testovací analýzy.[/white bold]\n"
        "(c) Není správně. Použití technik testování k odvození položek pokrytí je součástí [bold]návrhu testů.[/bold]\n"
        "(d) Není správně. Reportování defektů zjištěných při dynamickém testování je součástí [bold]provedení testů.[/bold]\n",
    },
    {
        "id": 5,
        "text": (
            "Který z následujících faktorů má [bold]VÝZNAMNÝ vliv[/bold] na přístup k testování?\n\n"
            "  [white bold]I.[/white bold] SDLC (životní cyklus vývoje softwaru).\n"
            " [white bold]II.[/white bold] Počet nalezených defektů v předchozích projektech.\n"
            "[white bold]III.[/white bold] Identifikovaná produktová rizika.\n"
            " [white bold]IV.[/white bold] Nové regulatorní požadavky vyžadující formální testování bílé skříňky.\n"
            "  [white bold]V.[/white bold] Nastavení testovacího prostředí.\n"
        ),
        "options": {
            "a": "[white bold]I, II [/white bold]     mají významný vliv.",
            "b": "[white bold]I, III, IV[/white bold] mají významný vliv.",
            "c": "[white bold]II, IV, V[/white bold]  mají významný vliv.",
            "d": "[white bold]III, V[/white bold]     mají významný vliv.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": "[gold1]  I. Je správně.[/gold1] [white bold]Zvolený SDLC má významný vliv na přístup k testování.[/white bold]\n"
        " II. Není správně. Počet zjištěných defektů v předchozích projektech může mít určitý vliv, ale ne tak významný jako I, III a IV.\n"
        "[gold1]III. Je správně[/gold1]. [white bold]Identifikovaná produktová rizika jsou jedním z nejdůležitějších faktorů ovlivňujících přístup k testování.[/white bold]\n"
        "[gold1] IV. Je správně[/gold1]. [white bold]Regulatorní požadavky jsou důležitými faktory ovlivňujícími přístup k testování.[/white bold]\n"
        "  V. Není správně.Testovací prostředí nemá významný vliv na přístup k testování.\n\n"
        "Pak tedy:\n"
        "(a) Není správně\n"
        "[gold1](b) Je správně.[/gold1]\n"
        "(c) Není správně\n"
        "(d) Není správně\n",
    },
    {
        "id": 6,
        "text": "Které [bold]DVA[/bold] z následujících úkolů jsou [bold]HLAVNÍ[/bold] náplní role testera?",
        "options": {
            "a": "[bold]Konfigurace[/bold] testovacích prostředí.",
            "b": "[bold]Udržování[/bold] produktového backlogu.",
            "c": "[bold]Návrh[/bold] řešení nových požadavků.",
            "d": "[bold]Vytvoření[/bold] plánu testování.",
            "e": "[bold]Analýza[/bold] testovací báze",
        },
        "correct": ["a", "e"],
        "points": 1,
        "explanation": "[gold1](a) Je správně[/gold1]. [white bold]Toto je prováděno testery.[/white bold]\n"
        "(b) Není správně. Produktový backlog je vytvořen a udržován vlastníkem produktu.\n"
        "(c) Není správně. Toto provádí vývojový tým.\n"
        "(d) Není správně. Jedná se o manažerskou roli.\n"
        "[gold1](e) Je správně.[/gold1] [white bold]Tuto činnost provádějí testeři, protože je to technický úkol prováděný v rámci testovací analýzy.\n[/white bold]",
    },
    {
        "id": 7,
        "text": (
            "Které z následujících dovedností (I-V) jsou [bold]NEJVÍCE[/bold] důležité dovednosti "
            "testera?\n"
            "  [white bold]I.[/white bold] Znalost domény.\n"
            " [white bold]II.[/white bold] Vytvoření vize produktu.\n"
            "[white bold]III.[/white bold] Být dobrým týmovým hráčem.\n"
            " [white bold]IV.[/white bold] Plánování a organizace práce týmu.\n"
            "  [white bold]V.[/white bold] Kritické myšlení.\n"
        ),
        "options": {
            "a": "[bold]II a IV[/bold]    jsou důležité.",
            "b": "[bold]I, III a V[/bold] jsou důležité.",
            "c": "[bold]I, II a V[/bold]  jsou důležité.",
            "d": "[bold]III a IV[/bold]   jsou důležité.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": "  [gold1]I. Je správně[/gold1]. [white bold]Znalost domény je důležitou dovedností testera.[/white bold]\n"
        " II. Není správně. To je úkolem byznysového analytika společně se zástupcem byznysu.\n"
        "[gold1]III. Je správně[/gold1]. [white bold]Být dobrým týmovým hráčem je důležitá dovednost.[/white bold]\n"
        " IV. Není správně. Plánování a organizace práce týmu je úkolem manažera testování nebo (v agilním projektu) celého týmu (tedy nejen testera).\n"
        "  [gold1]V. Je správně[/gold1]. [white bold]Kritické myšlení je jednou z nejdůležitějších dovedností testerů.[/white bold]\n\n"
        "Pak tedy:\n"
        "(a) Není správně\n"
        "[gold1](b) Je správně.[/gold1]\n"
        "(c) Není správně\n"
        "(d) Není správně\n",
    },
    {
        "id": 8,
        "text": (
            "Jak se [bold]týmový přístup[/bold] projevuje v interakcích mezi [bold]testery a zástupci "
            "byznysu?"
        ),
        "options": {
            "a": "[bold]Zástupci[/bold] byznysu rozhodují o přístupu k automatizaci testů.",
            "b": "[bold]Testeři [/bold]pomáhají zástupcům byznysu definovat strategii testování.",
            "c": "[bold]Zástupci[/bold] byznysu nejsou součástí týmového přístupu.",
            "d": "[bold]Testeři [/bold]pomáhají zástupcům byznysu vytvořit vhodné akceptační testy",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": "(a) Není správně. Přístup k automatizaci testování definují testeři za podpory vývojářů a zástupců byznysu.\n"
        "(b) Není správně. O strategii testování se rozhoduje ve spolupráci s vývojáři.\n"
        "(c) Není správně. Testeři, vývojáři a zástupci byznysu jsou součástí týmového přístupu.\n"
        "[gold1](d) Je správně.[/gold1]  [white bold]Testeři úzce spolupracují se zástupci byznysu, aby zajistili dosažení požadované úrovně kvality, což zahrnuje vzájemnou podporu a spolupráci tak, aby jim pomohli vytvořit vhodné akceptační testy.[/white bold]\n",
    },
    {
        "id": 9,
        "text": (
            "Pro které SDLC modely je platné pravidlo [bold]'pro každou činnost SDLC existuje odpovídající testovací činnost'[/bold]?"
        ),
        "options": {
            "a": "Pouze v [bold]sekvenčních[/bold] vývojových modelech",
            "b": "Pouze v [bold]iterativních[/bold] vývojových modelech",
            "c": "Pouze v [bold]iterativních a inkrementálních[/bold] vývojových modelech.",
            "d": "V [bold]sekvenčních, inkrementálních a iterativních[/bold] vývojových modelech.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": "(a) Není správně\n"
        "(b) Není správně\n"
        "(c) Není správně\n"
        "[gold1](d) Je správně.[/gold1]  [white bold]Toto tvrzení platí pro všechny modely SDLC.[/white bold]\n",
    },
    {
        "id": 10,
        "text": (
            "Které z následujících tvrzení [bold]NEJLÉPE[/bold] vystihuje přístup k vývoji řízenému [bold]akceptačními testy (ATDD)?[/bold]"
        ),
        "options": {
            "a": (
                "V [bold]ATDD[/bold] jsou akceptační kritéria obvykle vytvářena s využitím formátu [bold]Given/When/Then[/bold]."
            ),
            "b": (
                "V [bold]ATDD[/bold] jsou testovací případy vytvářeny hlavně při testování komponent [bold]a jsou orientovány na kód[/bold]."
            ),
            "c": (
                "V [bold]ATDD[/bold] jsou testy vytvářeny na základě akceptačních kritérií s cílem [bold]řídit vývoj daného softwaru[/bold]."
            ),
            "d": (
                "V [bold]ATDD[/bold] jsou testy založeny na požadovaném chování softwaru, což členům [bold]týmu usnadňuje jejich pochopení[/bold]."
            ),
        },
        "correct": ["c"],
        "points": 1,
        "explanation": "(a) Není správně. Častěji se používá při vývoji řízeném chováním (BDD).\n"
        "(b) Není správně. Jedná se o popis vývoje řízeného testy (TDD).\n"
        "[gold1](c) Je správně.[/gold1]  [white bold]Při vývoji řízeném akceptačními testy (ATDD) se testy tvoří na základě akceptačních kritérií jako součást procesu návrhu softwaru.[/white bold]\n"
        "(d) Není správně. Používá se při BDD.\n",
    },
    {
        "id": 11,
        "text": "Která z následujících možností [bold]NENÍ[/bold] příkladem přístupu [bold]'shift left'[/bold]?",
        "options": {
            "a": (
                "Revize uživatelských požadavků předtím, než jsou formálně akceptovány zainteresovanými stranami."
            ),
            "b": "Tvorba testů komponent před tvorbou odpovídajícího kódu.",
            "c": (
                "Provedení testů výkonnostní efektivity (výkonnosti) během testování komponent."
            ),
            "d": (
                "Tvorba testovacího skriptu před nastavením procesu konfiguračního managementu."
            ),
        },
        "correct": ["d"],
        "points": 1,
        "explanation": "(a) Není správně. Včasná revize je příkladem přístupu shift left.\n"
        "(b) Není správně. TDD je příkladem přístupu shift left.\n"
        "(c) Není správně. Včasné nefunkcionální testování je příkladem přístupu shift left.\n"
        "[gold1](d) Je správně.[/gold1]  [white bold]Testovací skripty by měly podléhat konfiguračnímu managementu, takže nemá smysl vytvářet testovací skripty před jeho zavedením.[/white bold]\n",
    },
    {
        "id": 12,
        "text": (
            "Který z níže uvedených argumentů byste použili, abyste přesvědčili svého manažera, aby po dokončení prací na novém vydání (release) uspořádal [bold]retrospektivu[/bold]?"
        ),
        "options": {
            "a": (
                "[bold]Retrospektivy[/bold] jsou v dnešní době velmi populární a klienti by ocenili, kdybychom je přidali do našich procesů."
            ),
            "b": (
                "Organizování [bold]retrospektiv[/bold] ušetří organizaci peníze, protože bez nich zástupci koncových uživatelů neposkytnou okamžitou zpětnou vazbu o produktu."
            ),
            "c": (
                "Slabé stránky procesů identifikované během [bold]retrospektivy[/bold] lze analyzovat a mohou následně sloužit jako seznam úkolů v rámci kontinuálního zlepšování procesů organizace."
            ),
            "d": (
                "[bold]Retrospektivy[/bold] zdůrazňují pět hodnot včetně odvahy a respektu, které jsou klíčové pro udržení trendu kontinuálního zlepšování v organizaci."
            ),
        },
        "correct": ["c"],
        "points": 1,
        "explanation": "(a) Není správně. Retrospektivy jsou vhodné spíše pro identifikaci příležitostí ke zlepšení a pro klienty mají malý význam.\n"
        "(b) Není správně. Cílem retrospektivy není shromažďovat zpětnou vazbu o produktu, ale o procesu. Retrospektivy jsou navíc interní aktivitou týmu a neměli by se jich účastnit zástupci koncových uživatelů.\n"
        "[gold1](c) Je správně.[/gold1]  [white bold]Pravidelně prováděné retrospektivy (pokud jsou následně zahájeny příslušné navazující činnosti) jsou zásadní pro kontinuální zlepšování procesů vývoje a procesů testování.[/white bold]\n"
        "(d) Není správně. Odvaha a respekt jsou hodnoty extrémního programování a s retrospektivami souvisejí nepřímo.",
    },
    {
        "id": 13,
        "text": (
            "Které typy selhání (1-4) nejlépe vyhovují daným úrovním testování (A-D)?\n"
            "-------------------------------------------------------------------------\n"
            "\n"
            "1. [bold]Selhání[/bold] v chování systému, protože se odchyluje od byznysových potřeb uživatelů.\n"
            "2. [bold]Selhání[/bold] v komunikaci mezi komponentami.\n"
            "3. [bold]Selhání[/bold] v logice kódu.\n"
            "4. [bold]Selhání[/bold] v nesprávně implementovaných byznysových pravidlech.\n"
            "\n"
            "[orange1]A.[/orange1] Testování komponent.\n"
            "[orange1]B.[/orange1] Integrační testování komponent.\n"
            "[orange1]C.[/orange1] Systémové testování.\n"
            "[orange1]D.[/orange1] Akceptační testování.\n"
        ),
        "options": {
            "a": "[bold]1D, 2B, 3A, 4C[/bold]",
            "b": "[bold]1D, 2B, 3C, 4A[/bold]",
            "c": "[bold]1B, 2A, 3D, 4C[/bold]",
            "d": "[bold]1C, 2B, 3A, 4D[/bold]",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": "Platí, že:\n"
        "• Testovací bázi pro [bold white]akceptační testování[/bold white] tvoří byznysové potřeby uživatelů ([cyan]1[/cyan][orange3]D[/orange3]).\n"
        "• Komunikace mezi komponentami je testována během [bold white]integračního testování[/bold white] komponent ([cyan]2[/cyan][orange3]B[/orange3]).\n"
        "• Selhání v logice mohou být nalezeny během [bold white]testování komponent[/bold white] ([cyan]3[/cyan][orange3]A[/orange3]).\n"
        "• Byznysová pravidla tvoří testovací bází pro [bold white]systémové testování[/bold white] ([cyan]4[/cyan][orange3]C[/orange3]).\n"
        "\n"
        "Pak tedy:\n"
        "[gold1](a) Je správně.[/gold1]\n"
        "(b) Není správně\n"
        "(c) Není správně\n"
        "(d) Není správně\n",
    },
    {
        "id": 14,
        "text": (
            "Testujete uživatelský scénář se [bold]třemi[/bold] akceptačními kritérii:\n"
            "[bold white]AC1, AC2 a AC3.[/bold white]\n\n"
            "[bold white]AC1[/bold white] je pokryt testovacím případem [bold white]TC1[/bold white]\n"
            "[bold white]AC2[/bold white] je pokryt testovacím případem [bold white]TC2[/bold white]\n"
            "[bold white]AC3[/bold white] je pokryt testovacím případem [bold white]TC3[/bold white]\n\n"
            "Při dosavadním provádění testů proběhly tři testovací běhy ve [bold white]třech[/bold white] po sobě jdoucích verzích softwaru následujícím způsobem:\n\n"
            "          |    run 1   |    run 2   |    run 3   |\n"
            "    |-----|------------|------------|------------|\n"
            "    | [bold white]TC1[/bold white] | (1) Selhal | (4) Prosel | (7) Prosel |\n"
            "    |-----|------------|------------|------------|\n"
            "    | [bold white]TC2[/bold white] | (2) Prosel | (5) Selhal | (8) Prosel |\n"
            "    |-----|------------|------------|------------|\n"
            "    | [bold white]TC3[/bold white] | (3) Selhal | (6) Selhal | (9) Prosel |\n"
            "    |-----|------------|------------|------------|\n\n"
            "Testy budou zopakovány po informaci, že všechny [bold white]defekty[/bold white] zjištěné při běhu [bold white]testu[/bold white] jsou opraveny a je k dispozici [bold white]nová verze softwaru[/bold white].\n"
            "Které z výše uvedených testů budou prováděny jako [bold white]regresní testy[/bold white]?\n"
        ),
        "options": {
            "a": "Pouze 4, 7, 8, 9",
            "b": "Pouze 5, 7",
            "c": "Pouze 4, 6, 8, 9",
            "d": "Pouze 5, 6",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": "Vzhledem k tomu, že [bold white]TC1[/bold white] a [bold white]TC3[/bold white] selhaly při běhu 1 (tj. [bold white]test 1[/bold white] a [bold white]test 3[/bold white]), [bold white]test 4[/bold white] a [bold white]test 6[/bold white] jsou při běhu 2 konfirmačními testy.\n"
        "Vzhledem k tomu, že [bold white]TC2[/bold white] a [bold white]TC3[/bold white] selhaly při běhu 2 (tj. [bold white]test 5[/bold white] a [bold white]test 6[/bold white]), [bold white]test 8[/bold white] a [bold white]test 9[/bold white] jsou při běhu 3 také konfirmačními testy.\n"
        "[bold white]TC2[/bold white] prošel při běhu 1 (tj. [bold white]test 2[/bold white]), takže [bold white]test 5[/bold white] je regresní test.\n"
        "[bold white]TC1[/bold white] prošel při běhu 2 (tj. [bold white]test 4[/bold white]), takže [bold white]test 7[/bold white] je také regresní test.\n\n"
        "Pak tedy:\n"
        "(a) Není správně\n"
        "[gold1](b) Je správně.[/gold1]\n"
        "(c) Není správně\n"
        "(d) Není správně\n",
    },
    {
        "id": 15,
        "text": "Která z následujících možností [bold red]NENÍ[/bold red] výhodou [bold white]statického testování[/bold white]?",
        "options": {
            "a": (
                "Levnější management defektů díky jejich snadné detekci v pozdějších fázích SDLC."
            ),
            "b": (
                "Oprava defektů zjištěných během statického testování je obecně mnohem levnější než oprava defektů zjištěných během dynamického testování."
            ),
            "c": (
                "Hledání defektů v kódu, které by nemusely být nalezeny pouze dynamickým testováním."
            ),
            "d": "Detekce nedostatků a nesrovnalostí v požadavcích.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": "[gold1](a) Je správně.[/gold1]  [white bold]Management defektů [red bold]není[/red bold] levnější. Vyhledávání a oprava defektů v pozdější fázi SDLC je[/white bold] [bold orange1]nákladnější.[/bold orange1]\n"
        "(b) Není správně. Toto [bold]je[/bold] výhoda [bold]statického testování[/bold].\n"
        "(c) Není správně. Toto [bold]je[/bold] výhoda [bold]statického testování[/bold].\n"
        "(d) Není správně. Toto [bold]je[/bold] výhoda [bold]statického testování[/bold].\n",
    },
    {
        "id": 16,
        "text": (
            "Která z následujících možností je výhodou včasné a časté zpětné vazby?"
        ),
        "options": {
            "a": (
                "[bold white]Zlepšuje[/bold white] proces testování pro budoucí projekty."
            ),
            "b": (
                "[bold white]Nutí[/bold white] zákazníky stanovit si priority svých požadavků na základě odsouhlasených rizik."
            ),
            "c": ("[bold white]Poskytuje[/bold white] míru kvality změn."),
            "d": (
                "[bold white]Pomáhá[/bold white] předcházet nedorozuměním v požadavcích"
            ),
        },
        "correct": ["d"],
        "points": 1,
        "explanation": "(a) Není správně. Zpětná vazba může zlepšit proces testování, ale pokud má dojít ke zlepšení pouze budoucích projektů, nemusí zpětná vazba přijít ani včas, ani dostatečně často.\n"
        "(b) Není správně. Zpětná vazba se nepoužívá ke stanovení priorit požadavků.\n"
        "(c) Není správně. Neexistuje univerzální doporučený způsob měření kvality změn. Navíc to není také jedna z výhod včasné zpětné vazby (viz kapitola 3.2.1).\n"
        "(d) [gold1]Je správně.[/gold1]  [white bold]Včasná a častá zpětná vazba může zabránit nedorozuměním ohledně požadavků.[/white bold]\n",
    },
    {
        "id": 17,
        "text": (
            "Revize, které se používají ve vaší organizaci, mají následující atributy:\n"
            "• existuje role zapisovatele\n"
            "• hlavním účelem je hodnocení kvality\n"
            "• revizní schůzky vede autor pracovního produktu\n"
            "• je prováděna individuální příprava\n"
            "• je vypracována revizní zpráva.\n\n"
            "Který z následujících typů revize se s NEJVĚTŠÍ pravděpodobností používá?\n"
        ),
        "options": {
            "a": ("Neformální revize."),
            "b": ("Předvedení (walkthrough)."),
            "c": ("Technická revize"),
            "d": ("Inspekce."),
        },
        "correct": ["b"],
        "points": 1,
        "explanation": "Na základě uvedených rysů je možno odvodit následující:\n"
        "• Zapisovatel bývá přítomen při předvedení, technické revizi a inspekci, takže se nejedná o neformální revizi.\n"
        "• Hodnocení kvality je jedním z nejdůležitějších cílů při předvedení.\n"
        "• To není povoleno pro inspekce a obvykle se to neprovádí při technických revizích. Moderátor je potřeba při předvedení a je povolen pro neformální revize.\n"
        "• Všechny typy revizí mohou zahrnovat individuální přípravu (i neformální revize).\n"
        "• Revizní zprávu lze vypracovat u všech typů revizí, i když neformální revize dokumentaci nevyžadují.\n\n"
        "Pak tedy:\n"
        "(a) Není správně\n"
        "[gold1](b) Je správně.[/gold1]\n"
        "(c) Není správně\n"
        "(d) Není správně\n",
    },
    {
        "id": 18,
        "text": (
            "Které z těchto tvrzení [bold red]NENÍ[/bold red] faktorem, který přispívá k [bold white]úspěšným revizím?[/bold white]"
        ),
        "options": {
            "a": ("Účastníci by měli revizím věnovat dostatek času."),
            "b": (
                "Rozdělení velkých pracovních produktů na menší části vede k tomu, že práce probíhá méně intenzivně."
            ),
            "c": (
                "Účastníci by se měli vyvarovat chování, které by mohlo naznačovat [bold]nudu, podráždění nebo nepřátelství[/bold] vůči ostatním účastníkům."
            ),
            "d": ("Zjištěná selhání by měla být uznána, oceněna a řešena objektivně."),
        },
        "correct": ["d"],
        "points": 1,
        "explanation": "(a) Není správně. [bold]Dostatek času[/bold] pro účastníky je faktorem úspěchu.\n"
        "(b) Není správně. [bold]Rozdělení pracovních produktů na menší části[/bold] je faktorem úspěchu.\n"
        "(c) Není správně. [bold]Vyvarování se chování, které by mohlo naznačovat nudu, podráždění atd[/bold]., je faktorem úspěchu.\n"
        "[gold1](d) Je správně.[/gold1]  [white bold]Při revizích lze identifikovat defekty, nikoli selhání.[/white bold]\n",
    },
    {
        "id": 19,
        "text": (
            "[bold]Která z[/bold] následujících [bold]vlastností[/bold] je charakteristická pro techniky testování založené na [bold]zkušenostech[/bold]?"
        ),
        "options": {
            "a": (
                "Testovací případy jsou vytvářeny na základě podrobných informací o návrhu"
            ),
            "b": (
                "Položky testované v rámci kódu rozhraní se používají k měření pokrytí."
            ),
            "c": (
                "Testovací techniky se do značné míry spoléhají na znalosti testera o softwaru a byznysové doméně"
            ),
            "d": (
                "Testovací případy se používají k identifikaci odchylek od požadavků."
            ),
        },
        "correct": ["c"],
        "points": 1,
        "explanation": "(a) Není správně. To je běžná charakteristika technik testování [bold]bílé skříňky[/bold]. Testovací podmínky, testovací případy a testovací data jsou odvozeny z testovací báze, která může zahrnovat kód, architekturu softwaru, detailní návrh nebo jakýkoli jiný zdroj informací týkající se struktury softwaru.\n"
        "(b) Není správně. To je běžná charakteristika technik testování [bold]bílé skříňky[/bold]. Pokrytí se měří na základě položek testovaných v rámci zvolené struktury a testovací techniky aplikované na testovací bázi.\n"
        "[gold1](c) Je správně.[/gold1]  [white bold]Toto je obecná charakteristika technik testování založených na zkušenostech. Tyto znalosti a zkušenosti zahrnující očekávané použití softwaru, jeho prostředí, pravděpodobné defekty a distribuci těchto defektů se používají k definování testů.[/white bold]\n"
        "(d) Není správně. To je obecná charakteristika technik testování [bold]černé skříňky[/bold]. Testovací případy lze použít k odhalení nedostatků v požadavcích, v jejich implementaci a také odchylek od požadavků.\n",
    },
    {
        "id": 20,
        "text": (
            "Testujete zjednodušený formulář pro vyhledávání bytů, který má pouze [bold]dvě kritéria vyhledávání[/bold]:\n\n"
            "[orange1]• patro[/orange1] (se třemi možnými variantami: [bold white]přízemí[/bold white], [bold white]první patro[/bold white], [bold white]druhé nebo vyšší patro[/bold white]),\n"
            "[orange1]• typ zahrady[/orange1] (se třemi možnými variantami: [bold white]žádná zahrada[/bold white], [bold white]malá zahrada[/bold white], [bold white]velká zahrada[/bold white])\n\n"
            "Každý z bytů v [bold white]přízemí[/bold white] má zahradu, byty ve vyšších patrech ji [bold white]nemají[/bold white]. Formulář má vestavěný [bold white]validační mechanismus[/bold white], který vám nedovolí použít kritéria vyhledávání, která porušují toto pravidlo.\n"
            "Každý test má dvě vstupní hodnoty: patro a typ zahrady. Chcete použít rozdělení tříd ekvivalence [bold white](EP)[/bold white] tak, aby testy pokryly všechny typy pater a všechny typy zahrad.\n"
            "[bold white]Jaký[/bold white] je [bold white]minimální počet testovacích případů[/bold white] pro dosažení 100% pokrytí [orange1]platných tříd ekvivalence[/orange1]?\n"
        ),
        "options": {
            "a": "3",
            "b": "4",
            "c": "5",
            "d": "6",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": "Situace uvedená v otázce je v učebních osnovách popsána jako pokrytí všech možností.\n\n"
        "Hodnoty [bold white]'malá zahrada'[/bold white] a [bold white]'velká zahrada'[/bold white] kritéria [bold white]'zahrada'[/bold white] mohou být použity pouze s hodnotou [bold white]'přízemí'[/bold white] kritéria [bold white]'patro'[/bold white], takže potřebujeme dva testovací případy s hodnotou [bold white]'přízemí'[/bold white], které pokrývají tyto dvě třídy u kritéria [bold white]'zahrada'[/bold white]."
        "Potřebujeme další dva testovací případy, abychom pokryli další dvě podlahové třídy. Zbývající třída [bold white]'bez zahrady'[/bold white] kritéria [bold white]'zahrada'[/bold white] je těmito testy pokryta.\n"
        "Potřebujeme tak celkem čtyři testovací případy:\n\n"
        "[orange1]TC1[/orange1] (přízemí, malá zahrada),"
        "[orange1]TC2[/orange1] (přízemí, velká zahrada),"
        "[orange1]TC3[/orange1] (první patro, bez zahrady),"
        "[orange1]TC4[/orange1] (druhé nebo vyšší patro, bez zahrady).\n\n"
        "Pak tedy:\n"
        "(a) Není správně\n"
        "[gold1](b) Je správně.[/gold1]\n"
        "(c) Není správně\n"
        "(d) Není správně",
    },
    {
        "id": 21,
        "text": (
            "Testujete systém, který vypočítává pro daného studenta jeho [bold white]celkovou známku[/bold white] z určitého předmětu.\n\n"
            "Celková známka je přidělena na základě konečného výsledku podle následujících pravidel:\n"
            "[bold white]•  0 - 50[/bold white]  bodů: [bold]neprospěl[/bold]\n"
            "[bold white]• 51 - 60[/bold white]  bodů: [bold]dostatečně[/bold]\n"
            "[bold white]• 61 - 70[/bold white]  bodů: [bold]uspokojivě[/bold]\n"
            "[bold white]• 71 - 80[/bold white]  bodů: [bold]dobře[/bold]\n"
            "[bold white]• 81 - 90[/bold white]  bodů: [bold]velmi dobře[/bold]\n"
            "[bold white]• 91 - 100[/bold white] bodů: [bold]výborně[/bold]\n\n"
            "Připravili jste následující sadu testovacích případů:\n\n"
            "Konečný výsledek | Očekávaná známka\n"
            "----------------------------------------\n"
            "[orange1]TC1[/orange1] - (91 bodů)  |  výborně\n"
            "[orange1]TC2[/orange1] - (50 bodů)  |  neprospěl\n"
            "[orange1]TC3[/orange1] - (81 bodů)  |  velmi dobře\n"
            "[orange1]TC4[/orange1] - (60 bodů)  |  dostatečně\n"
            "[orange1]TC5[/orange1] - (70 bodů)  |  uspokojivě\n"
            "[orange1]TC6[/orange1] - (80 bodů)  |  dobře\n\n"
            "[bold white]Jaké[/bold white] je pokrytí [bold white]hraničních hodnot[/bold white] při užití 2-hodnotové analýzy hraničních hodnot, kterého je dosaženo pomocí výše definovaných testovacích případů?\n"
        ),
        "options": {
            "a": "50%",
            "b": "60%",
            "c": "33,3%",
            "d": "100%",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": "Existuje 12 hraničních hodnot:\n"
        " 0, 50, 51, 60, 61, 70, 71, 80, 81, 90, 91 a 100.\n\n"
        "Testovací případy pokrývají šest z nich\n"
        "TC1 - 91, TC2 - 50, TC3 - 81,\n"
        "TC4 - 60, TC5 - 70 a TC7 - 51.\n"
        "Testovací případy tedy pokrývají [bold white]6/12 = 50 %[/bold white].\n"
        "Pak tedy:\n"
        "[gold1](a) Je správně.[/gold1]\n"
        "(b) Není správně\n"
        "(c) Není správně\n"
        "(d) Není správně\n",
    },
    {
        "id": 22,
        "text": (
            "Vaše oblíbená půjčovna kol právě představila nový CRM systém [bold](systém pro řízení vztahů se zákazníky)[/bold] a požádala vás jako jednoho z jejich nejvěrnějších členů, abyste jej otestovali.\n\n"
            "Implementované funkcionality jsou následující:\n"
            "• Kolo si může půjčit kdokoliv, ale členové mají 20% slevu.\n"
            "• Pokud dojde k překročení lhůty pro vrácení, nárok na slevu zaniká.\n"
            "• Po 15 výpůjčkách dostanou členové dárek (tričko).\n"
            "Rozhodovací tabulka popisující implementované funkcionality vypadá takto [green bold](T-true/pravda[/green bold], [red bold]F-false/nepravda[/red bold]):\n\n"
            "Podmínky          | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |\n"
            "-----------------------------------------------------------\n"
            "Členství          | [green bold]T[/green bold]  | [green bold]T[/green bold]  | [green bold]T[/green bold]  | [green bold]T[/green bold]  | [red bold]F[/red bold]  | [red bold]F[/red bold]  | [red bold]F[/red bold]  | [red bold]F[/red bold]  |\n"
            "překročení lhůty  | [green bold]T[/green bold]  | [red bold]F[/red bold]  | [green bold]T[/green bold]  | [red bold]F[/red bold]  | [green bold]T[/green bold]  | [red bold]F[/red bold]  | [red bold]F[/red bold]  | [green bold]T[/green bold]  |\n"
            "15. výpůjčka      | [red bold]F[/red bold]  | [red bold]F[/red bold]  | [green bold]T[/green bold]  | [green bold]T[/green bold]  | [red bold]F[/red bold]  | [red bold]F[/red bold]  | [green bold]T[/green bold]  | [green bold]T[/green bold]  |\n\n"
            "-----------------------------------------------------------\n"
            "Akce\n"
            "-----------------------------------------------------------\n"
            "sleva 20%         |    | [white bold]X[/white bold]  |    | [white bold]X[/white bold]  |    |    |    |    |\n"
            "dárek (tričko)    |    |    | [white bold]X[/white bold]  | [white bold]X[/white bold]  |    |    |    | [white bold]X[/white bold]  |\n"
            "-----------------------------------------------------------\n\n"
            "[bold]Které z výše uvedených pravidel[/bold] popisuje [white bold]POUZE[/white bold] na základě výše uvedeného popisu funkcionalit systému [orange1]nemožnou situaci?[/orange1]\n\n"
        ),
        "options": {
            "a": "R4",
            "b": "R2",
            "c": "R6",
            "d": "R8",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": "(a) Není správně. Člen, který nezmešká termín vrácení, může po 15 výpůjčkách kola získat slevu a dárkové tričko.\n"
        "(b) Není správně. Člen, který nezmešká termín vrácení, může získat slevu, ale nedostane dárkové tričko, dokud si 15krát nepůjčí kolo.\n"
        "(c) Není správně. Nečlenové nemohou získat slevu, a to ani v případě, že ještě nezmeškali termín vrácení.\n"
        "[gold1](d) Je správně.[/gold1]  [white bold]Pro nečleny, kteří zmeškali termín vrácení, není k dispozici žádná sleva, ale ani tričko (pouze členové mohou získat dárkové tričko). Výsledná akce (tričko) tedy není správně.\n[/white bold]",
    },
    {
        "id": 23,
        "text": (
            "Testujete systém, jehož životní cyklus je znázorněn na níže uvedeném diagramu přechodů stavů uvedeným níže. Systém se spustí ve stavu INIT a ukončí svou činnost ve stavu OFF.\n\n"
            "        [white bold]test[/white bold]   ┌────────────┐       [blue]done[/blue]       ┌─────┐\n"
            "     ┌────────>| DEBUG MODE |─────────────────>| OFF |\n"
            "     |         └────────────┘                  └─────┘\n"
            "┌────────┐           ↑                            ↑\n"
            "|  INIT  |           | [red]error[/red]                      | [blue]done[/blue]\n"
            "└────────┘           |             [cyan]pause[/cyan]          |\n"
            "     |         ┌──────────────┐─────────────>┌─────────┐\n"
            "     └────────>| IN operation |              | ON HOLD |\n"
            "        [green]run[/green]    └──────────────┘<─────────────└─────────┘\n"
            "                                   [yellow]resume[/yellow]\n\n"
            "Jaký je minimální počet testovacích případů pro dosažení pokrytí všech platných přechodů?\n"
        ),
        "options": {
            "a": 4,
            "b": 2,
            "c": 7,
            "d": 3,
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "Přechody [white bold]test[/white bold] a [red bold]error[/red bold] se nemohou vyskytovat v jednom testovacím případě.\n"
            "Ani jeden z těchto testů pokrývající přechody [white bold]test[/white bold] a [red bold]error[/red bold] nemůže zároveň přejít přes přechod [blue bold]done[/blue bold].\n"
            "To znamená, že pro dosažení pokrytí přechodů potřebujeme alespoň [white bold]tři testovací případy[/white bold]. Například:\n"
            "TC1: [white bold]test[/white bold], [blue]done[/blue]\n"
            "TC2: [green]run[/green], [red]error[/red], [blue]done[/blue]\n"
            "TC3: [green]run[/green], [cyan]pause[/cyan], [yellow]resume[/yellow], [cyan]pause[/cyan], [blue]done[/blue]\n\n"
            "Pak tedy:\n"
            "(a) Není správně\n"
            "(b) Není správně\n"
            "(c) Není správně\n"
            "[gold1](d) Je správně.[/gold1]\n"
        ),
    },
    {
        "id": 24,
        "text": (
            "Vaše testovací sada dosáhla 100% pokrytí příkazů. Co je důsledkem této skutečnosti?\n\n"
        ),
        "options": {
            "a": "Každá instrukce v kódu obsahující defekt byla provedena alespoň jednou.",
            "b": "Jakákoli testovací sada obsahující více testovacích případů než vaše testovací sada dosáhne také 100% pokrytí příkazů.",
            "c": "Každá cesta v kódu byla spuštěna alespoň jednou.",
            "d": "Každá kombinace vstupních hodnot byla alespoň jednou testována.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1]  [white bold]Vzhledem k tomu, že je dosaženo 100% pokrytí příkazů, musí být každý příkaz (včetně těch, ve kterých se vyskytují defekty) proveden a vyhodnocen alespoň jednou.[/white bold]\n"
            "(b) Není správně. Pokrytí závisí na tom, co se prověřuje testy, ne na počtu testovacích případů. Například pro kód 'if (x==0) y=1' je dosaženo 100 % pokrytí příkazů jedním testovacím případem (x=0), ale dva testovací případy (x=1) a (x=2) společně dosáhnou pouze 50% pokrytí příkazů.\n"
            "(c) Není správně. Pokud je v kódu smyčka, může existovat nekonečný počet možných cest, takže není možné projít všechny možné cesty v kódu.\n"
            "(d) Není správně. Kompletní testování není možné (viz kapitola Principy testování v učebních osnovách). Například pro kód 'input x'; 'print x'; platí,že libovolný jednotlivý test s libovolným x dosahuje 100 % pokrytí příkazů, ale pokrývá jednu vstupní hodnotu.\n"
        ),
    },
    {
        "id": 25,
        "text": (
            "Která z následujících možností [bold red]NENÍ[/bold red] pravdivá pro testování [white]bílé skříňky[/white]?\n"
        ),
        "options": {
            "a": "Při testování bílé skříňky je analyzována celá implementace softwaru.",
            "b": "Metriky pokrytí bílé skříňky mohou pomoci identifikovat další testy a zvýšit tak pokrytí kódu",
            "c": "Techniky bílé skříňky mohou být použity při statickém testování.",
            "d": "Testování bílé skříňky může pomoci identifikovat chyby v implementaci požadavků.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Význam technik testování bílé skříňky spočívá v tom, že se při testování bere v úvahu celá implementace softwaru.\n"
            "(b) Není správně. Míra pokrytí technikou testování bílé skříňky poskytuje objektivní měření pokrytí a poskytují nezbytné informace umožňující vytváření dalších testů s cílem zvýšení tohoto pokrytí.\n"
            "(c) Není správně. Techniky testování bílé skříňky mohou být využity k provádění revizí (což je forma statického testování).\n"
            "[gold1](d) Je správně.[/gold1]  [white bold]Toto je slabina technik testování bílé skříňky. Tyto techniky nejsou schopny identifikovat chybějící implementaci, protože jsou založeny pouze na struktuře testovaného objektu, nikoli na specifikaci požadavků.[/white bold]\n"
        ),
    },
    {
        "id": 26,
        "text": (
            "Které z následujících vyjádření [white bold]NEJLÉPE[/white bold] vystihuje koncept odhadování chyb?"
        ),
        "options": {
            "a": "Odhadování chyb zahrnuje využití vašich znalostí a zkušeností s defekty nalezenými v minulosti a typickými chybami vývojářů.",
            "b": "Odhadování chyb zahrnuje využití vašich osobních zkušeností s vývojem a s chybami,kterých jste se jako vývojáři dopustili.",
            "c": "Odhadování chyb vyžaduje, abyste si představili, že jste uživatelem testovaného objektu, a abyste odhadli chyby, kterých by se uživatel mohl dopustit při interakci s ním.",
            "d": "Odhadování chyb vyžaduje, abyste rychle duplikovali úkol pro vývojáře s cílem identifikace druhu chyby, kterou může vývojář udělat.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1]  [white bold]Základní koncept odhadování chyb spočívá v tom, že se tester snaží odhadnout na základě předchozích zkušeností (a někdy i kontrolních seznamů), jakých chyb se vývojář mohl dopustit a jaké defekty mohou být v testovaném objektu.[/white bold]\n"
            "(b) Není správně. Ačkoli může tester, který býval vývojářem, využít své osobní zkušenosti při odhadování chyb, testovací technika není založena na předchozích znalostech o vývoji softwaru.\n"
            "(c) Není správně. Odhadování chyb není technika použitelnosti, tzn. nedá se použít pro odhad toho, jakým způsobem může dojít k selhání při interakci uživatelů s testovaným objektem.\n"
            "(d) Není správně. Duplikování vývojového úkolu má několik nedostatků, které jej činí nepraktickým, například to, že tester má stejné dovednosti jako vývojář a nebo čas (navíc) potřebný k provedení vývojové aktivity. Nejedná se o odhadování chyb.\n"
        ),
    },
    {
        "id": 27,
        "text": (
            "Ve vašem projektu došlo ke zpoždění ve vydání zcela nové aplikace a testování začalo později než mělo. Vy ale máte velmi dobré a podrobné znalosti z byznysové domény a dobré analytické dovednosti. Týmu ještě nebyl dodán úplný seznam požadavků, přesto vedení žádá o předložení výsledků nějakých testů.\n\n"
            "[bold white]Která testovací technika se v této situaci hodí NEJLÉPE?[/bold white]\n\n"
        ),
        "options": {
            "a": "[bold]Testování[/bold] založené na kontrolních seznamech.",
            "b": "[bold]Odhadování[/bold] chyb.",
            "c": "[bold]Průzkumné[/bold] testování.",
            "d": "[bold]Testování[/bold] větví.",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Jedná se o nový produkt, proto pravděpodobně ještě není k dispozici kontrolní seznam ani testovací podmínky z důvodu chybějících požadavků.\n"
            "(b) Není správně. Jedná se o nový produkt, proto pravděpodobně ještě není k dispozici dostatek informací k tomu, aby bylo možno správně provést odhadování chyb.\n"
            "[gold1](c) Je správně.[/gold1]  [white bold]Průzkumné testování je nejvhodnější v situaci, kdy nejsou k dispozici detailnější požadavky a/nebo je testování pod tlakem vzhledem k termínům.[/white bold]\n"
            "(d) Není správně. Testování větví je časově náročné a vaše vedení požaduje nějaké výsledků testů co nejdříve (hned). Navíc testování větví nezohledňuje znalost domény.\n"
        ),
    },
    {
        "id": 28,
        "text": (
            "Které z následujících tvrzení [green bold]NEJLÉPE[/green bold] popisuje způsob, jakým lze dokumentovat [bold white]akceptační kritéria?[/bold white]"
        ),
        "options": {
            "a": "Provádění [bold]retrospektiv[/bold] za účelem zjištění skutečných potřeb zainteresovaných stran týkajících se daného uživatelského scénáře",
            "b": "Použití formátu [bold]Given/When/Then[/bold] k popisu ukázkové testovací podmínky související s daným uživatelským scénářem.",
            "c": "Používání [bold]verbální komunikace[/bold] ke snížení rizika nepochopení akceptačních kritérií ostatními.",
            "d": "[bold]Dokumentace rizik[/bold] souvisejících s daným uživatelským scénářem v testovacím plánu s cílem usnadnit testování daného uživatelského scénáře na základě rizik.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. [bold]Retrospektivy[/bold] se používají k zachycení získaných poznatků a ke zlepšování procesů vývoje a testování,nikoli k dokumentaci akceptačních kritérií.\n"
            "[gold1](b) Je správně.[/gold1]  [white bold]Jedná se o standardní způsob dokumentace akceptačních kritérií.[/white bold]\n"
            '(c) Není správně. [bold]Verbální komunikace[/bold] neumožňuje fyzicky zdokumentovat akceptační kritéria jako součást uživatelského scénáře, viz element "karta" (card) v technice 3C.\n'
            "(d) Není správně. [bold]Akceptační kritéria[/bold] souvisejí s uživatelským scénářem, nikoli s plánem testování. Akceptační kritéria jsou také podmínky, při jejichž splnění je možno prohlásit uživatelský scénář za kompletní. Rizika nejsou takovými podmínkami.\n"
        ),
    },
    {
        "id": 29,
        "text": (
            "Předpokládejme existenci následujícího [bold]uživatelského scénáře:[/bold]\n\n"
            "Jako [bold]editor[/bold] chci zkontrolovat obsah (článku) před jeho zveřejněním, abych se mohl ujistit, že je gramaticky správně.\n\n"
            "Akceptační kritéria tohoto scénáře byla definována takto:\n\n"
            "• [bold white]Uživatel se může přihlásit[/bold white] do redakčního systému v roli [bold white]Editor[/bold white].\n"
            "• [bold white]Editor může zobrazit[/bold white] existující seznam článků.\n"
            "• [bold white]Editor může upravovat[/bold white] obsah článku.\n"
            "• [bold white]Editor může přidávat[/bold white] revizní poznámky.\n"
            "• [bold white]Editor může ukládat[/bold white] změny.\n"
            "• [bold white]Editor může článek vrátit[/bold white] k přepracování autorovi článku za účelem aktualizace.\n\n"
            "Který z následujících příkladů je [green bold]NEJLEPŠÍM příkladem[/green bold] testu při použití přístupu vývoj řízený [bold white]akceptačními testy (ATDD)?[/bold white]\n"
        ),
        "options": {
            "a": "Test, zda [white]editor[/white] může článek uložit po jeho úpravě",
            "b": "Test, zda se [white]autor článku[/white] může přihlásit a provádět aktualizace jeho obsahu.",
            "c": "Test, zda [white]editor[/white] může naplánovat upravený článek k publikaci.",
            "d": "Test, zda [white]editor[/white] může článek přiřadit jinému [white]editoru[/white], aby provedl aktualizace.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1]  [white bold]Tento test pokrývá dvě akceptační kritéria: jedno se týká úprav dokumentu a druhé ukládání změn.[/white bold]\n"
            "(b) Není správně. Akceptační kritéria pokrývají aktivity editora, nikoli aktivity autora článku.\n"
            "(c) Není správně. Naplánování zveřejnění upraveného obsahu může být hezká funkcionalita, ale nevztahují se na ni akceptační kritéria.\n"
            "(d) Není správně. Akceptační kritéria uvádějí změnu přiřazení z editora na autora článku, nikoli na jiného editora."
        ),
    },
    {
        "id": 30,
        "text": (
            "Jakou přidanou hodnotou má přítomnost testera pro plánování iterací a plánování vydání?\n\n"
        ),
        "options": {
            "a": "[bold]Testeři[/bold] určují prioritu uživatelských scénářů, které mají být implementovány.",
            "b": "[bold]Testeři[/bold] se zaměřují pouze na funkcionální aspekty testovaného systému.",
            "c": "[bold]Testeři[/bold] se podílejí na detailní identifikaci a ohodnocení rizik uživatelských scénářů.",
            "d": "[bold]Testeři[/bold] garantují vydání vysoce kvalitního softwaru prostřednictvím včasného návrhu testů během plánování vydání.",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "(a) Není správně. [bold]Priority[/bold] uživatelských scénářů [bold]určují zástupci byznysu společně s vývojovým týmem.[/bold]\n"
            "(b) Není správně. Testeři se zaměřují na [bold]funkcionální i nefunkcionální aspekty testovaného systému.[/bold]\n"
            "[gold1](c) Je správně.[/gold1]  [white bold]Podle učebních osnov je to jeden z přínosů testerů zapojených do plánování iterací a plánování vydání.[/white bold]\n"
            "(d) Není správně. Včasný návrh testů není součástí plánování vydání. [bold]Včasný návrh testů automaticky nezaručuje vydání kvalitního softwaru.[/bold]\n"
        ),
    },
    {
        "id": 31,
        "text": (
            "Které [bold]DVĚ[/bold] z následujících možností jsou [white bold]výstupními kritérii[/white bold] pro testování systému?\n"
        ),
        "options": {
            "a": "Připravenost testovacího prostředí",
            "b": "Schopnost přihlásit se do testovanému objektu testerem",
            "c": "Odhadovaná hustota defektů je dosažena",
            "d": "Požadavky jsou přeloženy do formátu [bold]Given/When/Then[/bold]",
            "e": "Regresní testy jsou automatizovány",
        },
        "correct": ["c", "e"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Připravenost testovacího prostředí je kritériem [bold]dostupnosti zdrojů[/bold] a patří tedy mezi vstupní kritéria.\n"
            "(b) Není správně. Jedná se také o kritérium [bold]dostupnosti zdrojů[/bold], patří tedy také mezi vstupní kritéria.\n"
            "[gold1](c) Je správně.[/gold1] [white bold]Odhadovaná hustota defektů je mírou důkladnosti, a proto patří mezi výstupní kritéria.[/white bold]\n"
            "(d) Není správně. Požadavky přeložené do daného formátu vedou k testovatelným požadavkům, a proto patří mezi vstupní kritéria.\n"
            "[gold1](e) Je správně.[/gold1]  [white bold]Automatizace regresních testů je kritériem dokončení, patří mezi výstupní kritéria.[/white bold]\n"
        ),
    },
    {
        "id": 32,
        "text": (
            "Váš tým používá techniku [bold]tříbodového odhadu[/bold] k odhadu pracnosti při testování nové vysoce rizikové užitné vlastnosti (feature). Byly provedeny následující odhady:\n\n"
            "[bold]• Nejoptimističtější  [bold]odhad: 2 člověko-hodiny.[/bold]\n"
            "[bold]• Nejpravděpodobnější [bold]odhad: 11 člověko-hodin.[/bold]\n"
            "[bold]• Nejpesimističtější  [bold]odhad: 14 člověko-hodin.[/bold]\n\n"
            "Jaký je konečný odhad?\n"
        ),
        "options": {
            "a": " 9 člověko-hodin.",
            "b": "14 člověko-hodin",
            "c": "11 člověko-hodin",
            "d": "10 člověko-hodin",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "U techniky tříbodového odhadu platí:\n"
            "[bold]E = (optimistický + 4 * nejpravděpodobnější + pesimistický) / 6[/bold]\n"
            "[bold]E = (2 + (4 * 11) + 14) / 6 = 10[/bold]\n\n"
            "(a) Není správně. Toto je pouze nejpravděpodobnější odhad.\n"
            "(b) Není správně. Toto je pouze nejpesimističtější odhad.\n"
            "(c) Není správně. Toto je pouze nejpravděpodobnější odhad.\n"
            "[gold1](d) Je správně.[/gold1][white bold]\n"
        ),
    },
    {
        "id": 33,
        "text": (
            "Testujete mobilní aplikaci, která uživatelům umožňuje najít restauraci v okolí na základě typu jídla,které chtějí jíst. Máme definován následující seznam testovacích případů, priorit (menší číslo znamená vyšší prioritu) a závislostí:\n\n"
            "┌──────────────────┬────────────────────────────┬──────────┬────────────┐\n"
            "│ Testovací případ │ Pokrytá testovací podmínka │ Priorita │ Závislosti │\n"
            "├──────────────────┼────────────────────────────┼──────────┼────────────┤\n"
            "│ TC001            │  Vyber druh jídla          │    3     │ žádná      │\n"
            "│ TC002            │  Vyber restauraci          │    2     │ TC001      │\n"
            "│ TC003            │  Získej adresu             │    1     │ TC002      │\n"
            "│ TC004            │  Zavolej do restaurace     │    2     │ TC002      │\n"
            "│ TC005            │  Vytvoř rezervaci          │    3     │ TC002      │\n"
            "└──────────────────┴────────────────────────────┴──────────┴────────────┘\n\n"
            "Který z následujících testovacích případů by měl být proveden jako třetí?\n"
        ),
        "options": {
            "a": "TC003",
            "b": "TC005",
            "c": "TC002",
            "d": "TC001",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "Z důvodu splnění závislosti musí být test TC 001 proveden jako první, TC 002 jako druhý. Následně TC 003 (z důvodu dodržení priorit), poté TC 004 a nakonec TC 005. \n\n"
            "[gold1](a) Je správně.[/gold1] [white bold]   TC003 by měl být proveden jako třetí, protože má nejvyšší prioritu mezi testy, které jsou závislé na [bold]TC002[/bold], který musí být proveden jako druhý.[/white bold]\n"
            "(b) Není správně. [bold]TC005[/bold] by měl být proveden jako poslední, protože má nejnižší prioritu mezi testy, které jsou závislé na [bold]TC002[/bold], který musí být proveden jako druhý.\n"
            "(c) Není správně. [bold]TC002[/bold] musí být proveden jako druhý, protože je závislý na [bold]TC001[/bold], který musí být proveden jako první.\n"
            "(d) Není správně. [bold]TC001[/bold] musí být proveden jako první, protože nemá žádné závislosti. [bold]TC002[/bold] musí být proveden jako druhý, protože je závislý na [bold]TC001[/bold], který musí být proveden jako první.\n"
        ),
    },
    {
        "id": 34,
        "text": (
            "Uvažujme následující kategorie testů (1-4) a agilní testovací kvadranty (A-D):\n\n"
            "1. 1 Testování použitelnosti.\n"
            "2. 2 Testování komponent.\n"
            "3. 3 Funkcionální testování.\n"
            "4. 4 Testování spolehlivosti.\n"
            "--------------------------------------------------------------------------\n"
            "A. A Agilní testovací kvadrant Q1: zaměřený na [white]technologii, podporující tým[/white].\n"
            "B. B Agilní testovací kvadrant Q2: zaměřený na [white]byznys, podporující tým[/white].\n"
            "C. C Kvadrant Q3: zaměřený na [white]byznys, revidující produkt[/white].\n"
            "D. D Kvadrant Q4: zaměřený na [white]technologii, revidující produkt[/white].\n\n"
            "Do kterých [white]kvadrantů[/white] byste výše uvedené testy zařadili?\n"
        ),
        "options": {
            "a": "1C, 2A, 3B, 4D",
            "b": "1D, 2A, 3C, 4B",
            "c": "1C, 2B, 3D, 4A",
            "d": "1D, 2B, 3C, 4A",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "Platí, že:\n"
            "    [white]• Testování použitelnosti[/white] je zařazeno v [green1]Q3 (1 - C)[/green1].\n"
            "    [white]• Testování komponent[/white]     je zařazeno v [bright_green]Q1 (2 - A)[/bright_green].\n"
            "    [white]• Funkcionální testování [/white] je zařazeno v [green3]Q2 (3 - B)[/green3].\n"
            "    [white]• Testování spolehlivosti[/white] je zařazeno v [green4]Q4 (4 - D)[/green4].\n\n"
            "Pak tedy:\n"
            "[gold1](a) Je správně.[/gold1]\n"
            "(b) Není správně\n"
            "(c) Není správně\n"
            "(d) Není správně\n"
        ),
    },
    {
        "id": 35,
        "text": (
            "Během analýzy rizik byla identifikována a ohodnocena následující rizika:\n\n"
            "• Riziko [red1]Doba odezvy je příliš dlouhá[/red1] na to, aby bylo možné vygenerovat sestavu.\n"
            "• Pravděpodobnost rizika: [orange1]střední[/orange1]; dopad rizika: [red]vysoký[/red]\n"
            "• Reakce na riziko:\n"
            "   [white]- Nezávislý testovací tým provádí během systémového testování testování výkonnostní efektivity (výkonnosti).[/white]\n"
            "   [white]- Vybraný vzorek koncových uživatelů provádí před vydáním alfa a beta testování.[/white]\n\n"
            "Jaký způsob reakce na toto analyzované riziko je zvolen?\n"
        ),
        "options": {
            "a": "Přijetí rizika",
            "b": "Záložní plán",
            "c": "Zmírnění rizika",
            "d": "Přenos rizika",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Riziko [red1]nemůže[/red1] být akceptováno. Jsou navrhována konkrétní opatření.\n"
            "(b) Není správně. Nejsou navrhovány žádné pohotovostní plány.\n"
            "[gold1](c) Je správně.[/gold1]  [white] Navrhovaná opatření souvisí s testováním, které je formou zmírňování rizik.[/white]\n"
            "(d) Není správně. Riziko se [orange1]nepřenáší[/orange1], ale [blue]zmírňuje[/blue]\n"
        ),
    },
    {
        "id": 36,
        "text": (
            "Který pracovní produkt může agilní tým použít k zobrazení množství dokončené práce a množství celkové zbývající práce pro danou iteraci?\n"
        ),
        "options": {
            "a": "Akceptační kritéria",
            "b": "Report o defektu",
            "c": "Souhrnný report z testování.",
            "d": "Graf burn-down.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Akceptační kritéria jsou podmínky, které se používají k rozhodnutí, zda je uživatelský scénář hotový a nejsou určena kzobrazení postupu prací.\n"
            "(b) Není správně. Reporty o defektu informují o defektech a taktéž nejsou určena k zobrazení postupu prací.\n"
            "(c) Není správně. Souhrnný report z testování se vytváří po dokončení iterace, takže nemůže zobrazovat postup prací v průběhu iterace.\n"
            "[gold1](d) Je správně.[/gold1]  [white] Grafy burndown jsou grafickým znázorněním zbývající práce (pracnosti) v závislosti na zbývajícím čase. Jsou denně aktualizovány, takže mohou průběžně ukazovat postup prací.[/white]\n"
        ),
    },
    {
        "id": 37,
        "text": (
            "Je třeba aktualizovat jeden z automatizovaných testovacích skriptů tak, aby byl v souladu s novým požadavkem. Který proces vyžaduje tvorbu nové verze testovacího skriptu v repozitáři testů?\n"
        ),
        "options": {
            "a": "Management trasovatelnosti",
            "b": "Testování údržby.",
            "c": "Konfigurační management.",
            "d": "Management požadavků.",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Trasovatelnost je vztah mezi dvěma nebo více pracovními produkty, nikoli mezi různými verzemi stejného pracovního produktu.\n"
            "(b) Není správně. Testování údržby se zabývá testováním změn a nesouvisí přímo s verzováním.\n"
            "[gold1](c) Je správně.[/gold1]  [white] Z důvodu podpory testování může konfigurační management zahrnovat také správu verzí všech položek testování.[/white]\n"
            "(d) Není správně. Řízení požadavků je získávání, dokumentace a správa požadavků a nesouvisí přímo s verzováním testovacích skriptů.\n"
        ),
    },
    {
        "id": 38,
        "text": (
            "Od vývojářů jste obdrželi vyjádření k následujícímu report o defektu, kde uvádí, že popsaná anomálie není reprodukovatelná.\n\n"
            "[italic]Aplikace zamrzne[/italic]\n\n"
            "[italic]3. května 2022 - John Doe - Odmítnuto[/italic]\n\n"
            "[italic]Aplikace zamrzne po zadání [bold]'Test input: $ä'[/bold] do pole Název na obrazovce pro vytvoření nového uživatele. Zkusil jsem se odhlásit a přihlásit pomocí účtu [bold]test_admin01[/bold], stejný problém. Zkusil jsem i s jinými testovacími účty správců, stejný problém. Nezobrazila se [bold]žádná chybová zpráva[/bold], log (viz příloha) obsahuje upozornění na [bold]závažnou chybu[/bold]. Na základě testovacího případu [bold]TC-1305[/bold] by aplikace měla akceptovat poskytnutý vstup a vytvořit uživatele. Prosím o opravu s vysokou prioritou, tato funkcionalita souvisí s [bold]REQ0012[/bold], což je nový kritický byznysový požadavek.[/italic]\n\n"
            "Jaké kritické informace, které by byly pro vývojáře užitečné, v tomto reportu CHYBÍ?\n"
        ),
        "options": {
            "a": "Očekávané a skutečné výsledky",
            "b": "Reference a stav defektu.",
            "c": "Testovací prostředí a položka testování.",
            "d": "Priorita a závažnost.",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Očekávaným výsledkem je: aplikace by měla přijmout zadaný vstup a vytvořit uživatele. Skutečný výsledek je: aplikace zamrzne po zadání [bold]'Test input: $ä'[/bold]\n"
            "(b) Není správně. V reportu je uveden odkaz na testovací případ a související požadavek, kdy je uvedeno, že defekt byl zamítnut. Stav defektu by také vývojářům příliš nepomohl.\n"
            "[gold1](c) Je správně.[/gold1]  [white] Nevíme, ve kterém testovacím prostředí byla anomálie detekována, a také nevíme, ve které aplikaci a verzi se objevila.[/white]\n"
            "(d) Není správně. Report o defektu uvádí, že vyřešení anomálie je urgentní a jedná se o globální problém (tj. je ovlivněno mnoho účtů správy testů, možná dokonce všechny) a uvádí, že dopad je pro byznysové zainteresované strany vysoký.\n"
        ),
    },
    {
        "id": 39,
        "text": ("Kterou testovací činnost podporuje nástroj pro přípravu dat?\n"),
        "options": {
            "a": "Monitoring testování a řízení testování",
            "b": "Testovací analýza. ",
            "c": "Návrh testů a implementace testování",
            "d": "Dokončení testování",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Monitoring testování zahrnuje průběžnou kontrolu všech činností testování a porovnávání skutečného stavu proti plánu. Řízení testování zahrnuje přijetí opatření nezbytných pro dosažení cílů testování definovaných v plánu testování. Během těchto činností se nepřipravují žádná testovací data.\n"
            "(b) Není správně. Testovací analýza zahrnuje analýzu testovací báze za účelem identifikace testovacích podmínek a stanovení jejich priorit. Testovací data se během této činnosti nepřipravují.\n"
            "[gold1](c) Je správně.[/gold1]  [white] Návrh testů i implementace testování mohou zahrnovat identifikaci, vytvoření nebo získání testwaru nezbytného pro provedení testů (např. testovací data).[/white]\n"
            "(d) Není správně. Aktivity dokončení testování se vyskytují v milnících projektu (např. vydání, konec iterace, dokončení úrovně testování), takže na přípravu testovacích dat je příliš pozdě.\n"
        ),
    },
    {
        "id": 40,
        "text": (
            "Která možnost správně identifikuje potenciální riziko automatizace testů?\n"
        ),
        "options": {
            "a": "Může způsobit neznámé regrese v produkčním prostředí",
            "b": "Na údržbu testwaru není alokována dostatečná pracnost.",
            "c": "Na testovací nástroje a související testware se nelze dostatečně spolehnout",
            "d": "Může zkrátit čas vyhrazený pro manuální testování",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Automatizace testování nezpůsobuje nové (neznámé) regrese v produkčním prostředí.\n"
            "[gold1](b) Je správně.[/gold1]  [white] Špatná (obvykle nízká) alokace pracnosti na údržbu testwaru je riziko[/white]\n"
            "(c) Není správně. Testovací nástroje musí být vybrány tak, aby se na ně a jejich testware dalo spolehnout.\n"
            "(d) Není správně. Primárním cílem automatizace testů je snížit množství manuálního testování. Jedná se tedy o výhodu, nikoli riziko.\n"
        ),
    },
]
