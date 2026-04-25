"""otázky pro testování ISTQB Foundation Level C"""

QUESTIONS: list = [
    # {
    #     "id": 1,
    #     "text": ("Která z následujících možností je typickým cílem testování?\n"),
    #     "options": {
    #         "a": "Validace, že jsou splněny zdokumentované požadavky",
    #         "b": "Vyvolání selhání a identifikace defektů.",
    #         "c": "Iniciování chyb a identifikace kořenových příčin",
    #         "d": "Ověření, že testovaný objekt splňuje očekávání uživatele.",
    #     },
    #     "correct": ["b"],
    #     "points": 1,
    #     "explanation": (
    #         "(a) Není správně. Použití termínu validace pro kontrolu splnění zdokumentovaných požadavků je nesprávné, protože validace se zabývá naplněním potřeb a očekávání uživatelů, zatímco verifikace(ověření) se zabývá splněním specifikovaných požadavků. Správně byto tedy bylo, pokud bychom slovo „validace“ nahradili slovem„verifikace“ (ověření).\n"
    #         "[gold1](b) Je správně.[/gold1] [white bold]Vyvolávání selhání a identifikace defektů je nejčastějším cílem dynamického testování.[/white bold]\n"
    #         "(c) Není správně. Iniciování chyb a identifikace jejich kořenových příčin je nesprávně, protože testeři chyby neiniciují, snaží se vyvolat selhání. Chyby jsou obvykle způsobeny vývojáři (a opravdu je nelze iniciovat) a vedou k defektům, které se testeři snaží identifikovat buď přímo pomocí statického testování, nebo nepřímo prostřednictvím selhání při dynamickém testování. Identifikace kořenových příčin je užitečná, ale je součástí ladění, což není testovací činnost.\n"
    #         "(d) Není správně. Verifikace (ověření), že testovaný objekt splňuje očekávání uživatelů, je nesprávné, protože ověření se zabývá kontrolou, zda jsou splněny specifikované (zdokumentované) požadavky. Splněním potřeb a očekávání uživatelů se naopak zabývá validace. Tvrzení by tedy bylo správné, pokud bychom nahradili pojem „ověření“ pojmem „validace“.\n"
    #     ),
    # },
    # {
    #     "id": 2,
    #     "text": (
    #         "Které z následujících tvrzení [green]NEJLÉPE[/green] vystihuje rozdíl mezi [bold]testováním[/bold] a [bold]laděním[/bold]?\n"
    #     ),
    #     "options": {
    #         "a": "Testování způsobuje selhání, zatímco ladění selhání napravuje",
    #         "b": "Testování je negativní činnost, zatímco ladění je pozitivní činnost. ",
    #         "c": "Testováním se zjišťuje, zda defekty existují, zatímco laděním se defekty odstraňují.",
    #         "d": "Testování zjišťuje příčinu defektů, zatímco ladění ji odstraňuje.",
    #     },
    #     "correct": ["c"],
    #     "points": 1,
    #     "explanation": (
    #         "(a) Není správně. Dynamické testování skutečně vyvolává selhání (na jejichž základě lze následně lokalizovat a opravit defekty). Ladění se však zabývá lokalizací defektů a jejich opravou. Ladění tedy neopravuje selhání.\n"
    #         "(b) Není správně. Jak testování, tak ladění přispívají ke zlepšení kvality testovaného objektu, a proto by měly být obě tyto činnosti považovány za pozitivní. Ladění je obecně považováno za pozitivní činnost, protože se při ní něco opravuje. Dynamické testování zahrnuje záměrné vyvolání selhání testovaného objektu, což je důvod, proč jej někteří lidé považují za negativní aktivitu. To je ale velmi zúžený pohled (který testeři obvykle nezastávají). Jsou možné jak pozitivní, tak negativní testovací případy. Pozitivní testovací případy kontrolují, zda testovaný objekt správně provádí to, co má, zatímco negativní testování kontroluje, zda testovaný objekt nedělá to, co dělat nemá.\n"
    #         "[gold1](c) Je správně.[/gold1] [white bold]Testování zjišťuje existenci defektů buď přímo pozorováním defektu při revizích (nebo pomocí nástroje při statické analýze), nebo nepřímo vyvoláním selhání při dynamickém testování. Ladění je činnost odlišná od testování (obvykle prováděná vývojáři) a zabývá se vyhledáváním defektů (pouze u dynamického testování) a jejich odstraňováním.[/white bold]\n"
    #         "(d) Není správně. Příčinou defektů jsou obvykle lidské chyby. Testování odhaluje defekty buď přímo prostřednictvím statického testování, nebo nepřímo tím, že vyvolává selhání při dynamickém testování. Ladění odstraňuje přímo defekty. Testování tedy nezjistí a ladění neodstraní příčinu defektů.\n"
    #     ),
    # },
    # {
    #     "id": 3,
    #     "text": (
    #         "Jeden z principů testování říká: [white]Nepřítomnost defektů je klam[/white]. Které z následujících tvrzení je příkladem praktického uplatnění tohoto principu? \n"
    #     ),
    #     "options": {
    #         "a": "Vysvětlení, že testování nemůže prokázat neexistenci defektů.",
    #         "b": "Podpora koncových uživatelů při provádění akceptačního testování. ",
    #         "c": "Zajištění toho, že v dodaném systému nezůstanou žádné defekty v implementaci",
    #         "d": "Úprava testů, které již selhání nevyvolávají, aby se zajistilo, že zůstane jen malé množství defektů.",
    #     },
    #     "correct": ["b"],
    #     "points": 1,
    #     "explanation": (
    #         "Princip [white bold]nepřítomnost defektů je klam[/white bold] se týká myšlenky, že zajištění správnosti v návaznosti na požadavky (tj. ověření absence defektů implementace) nezaručuje spokojenost uživatele se systémem. Je také nutno ověřit, že systém splňuje potřeby a očekávání uživatelů, plní byznysové cíle a překonává konkurenční systémy.\n\n"
    #         "a) Není správně. Princip [white bold]testování prokazuje přítomnost defektů, nikoli jejich nepřítomnost[/white bold] ukazuje, že testování sice může odhalit existenci defektů v testovaném objektu, ale nedokazuje, že v něm žádné defekty neexistují, a nemůže tedy zaručit jeho správnost. Vysvětlení, že testování nemůže prokázat neexistenci defektů, by se tedy částečně odkazovalo na tento princip, nikoliv ale na princip [white bold]nepřítomnost defektů je klam[/white bold].\n"
    #         "[gold1](b) Je správně.[/gold1] [white bold]Využitím koncových uživatelů při provádění akceptačních testů by mělo být možné ověřit, že systém splňuje potřeby a očekávání uživatelů.[/white bold]\n"
    #         "(c) Není správně. Není možné zajistit, aby v dodaném systému nezůstaly žádné implementační defekty, protože princip [white bold]testování prokazuje přítomnost defektů, nikoli jejich nepřítomnost.[/white bold] vysvětluje, že testování sice může odhalit existenci defektů v testovaném objektu, ale není možné prokázat, že v něm žádné defekty nejsou, a tedy ani zaručit jeho správnost.\n"
    #         "(d) Není správně. Jedním ze způsobů, jak řešit princip [white bold]testy se opotřebovávají[/white bold], je úprava testů, které nezpůsobují žádné selhání tak, aby se nějaké defekty objevily. Tento princip se týká myšlenky, že opakování stejných testů na nezměněném kódu pravděpodobně neodhalí nové defekty, a proto může být důležité tyto testy upravit. Tím se ovšem nepotvrdí, že systém splňuje potřeby a očekávání uživatelů.\n"
    #     ),
    # },
    # {
    #     "id": 4,
    #     "text": (
    #         "Které z následujících testovacích činností budou s [green]NEJVĚTŠÍ[/green] pravděpodobností zahrnovat použití [white bold]analýzy hraničních hodnot a rozdělení tříd ekvivalence[/white bold]?\n"
    #     ),
    #     "options": {
    #         "a": "Implementace testování.",
    #         "b": "Návrh testů.",
    #         "c": "Provedení testů.",
    #         "d": "Monitoring testování.",
    #         "e": "Testovací analýza",
    #     },
    #     "correct": ["b", "e"],
    #     "points": 1,
    #     "explanation": (
    #         "Testovací analýza je popsána takto: [bold]Pro identifikaci funkcionalit, které vyžadují testování, je analyzována testovací báze, a výstupem této analýzy jsou prioritizované testovací podmínky spolu se souvisejícími riziky. Systematická identifikace testovacích podmínek jako položek pokrytí často zahrnuje použití technik testování jak během testovací analýzy, tak během činností návrhu testů.[/bold] Z výše uvedeného popisu vyplývá, že techniky testování se často používají v činnostech testovací analýzy a návrhu testů. Technikami testování jsou analýza hraničních hodnot a rozdělení tříd ekvivalence.\n\n"
    #         "(a) Není správně. V rámci implementace testování se pravděpodobně nebudou používat techniky testování, protože implementace testování se většinou zabývá sestavením testovacích případů do testovacích procedur, zatímco výstupem technik testování jsou testovací případy\n"
    #         "[gold1](b) Je správně.[/gold1] [white bold]V rámci návrhu testů se pravděpodobně budou používat techniky testování s cílem vytvořit testovací případy z testovacích podmínek a položek pokrytí.[/white bold]\n"
    #         "(c) Není správně. V rámci provedení testů se pravděpodobně nebudou používat techniky testování, protože provedení testování se většinou zabývá provedením testovacích procedur (a tím testovacích případů), zatímco výstupem technik testování jsou testovací případy.\n"
    #         "(d) Není správně. V rámci monitorování testování se pravděpodobně nebudou používat techniky testování. Monitorování testování se většinou zabývá průběžnými kontrolami s cílem zajistit dodržování plánu, zatímco výstupem technik testování jsou testovací případy.\n"
    #         "[gold1](e) Je správně.[/gold1] [white bold]Testovací analýza používá testovací techniky k identifikaci testovacích podmínek.[/white bold]\n"
    #     ),
    # },
    # {
    #     "id": 5,
    #     "text": (
    #         "Máte k dispozici následující testware:\n"
    #         "1. Položky pokrytí.\n"
    #         "2. Požadavek na změnu.\n"
    #         "3. Harmonogram provádění testů.\n"
    #         "4. Prioritizované testovací podmínky.\n\n"
    #         "A následující testovací činnosti:\n"
    #         "A. Testovací analýza.\n"
    #         "B. Návrh testů.\n"
    #         "C. Implementace testování.\n"
    #         "D. Dokončení testování.\n\n"
    #         "Která z následujících možností [green]NEJLÉPE[/green] vystihuje fakt, že je výše uvedený testware výstupem těchto testovacích činností?\n"
    #     ),
    #     "options": {
    #         "a": "1B, 2D, 3C, 4A",
    #         "b": "1B, 2D, 3A, 4C",
    #         "c": "1D, 2C, 3A, 4B",
    #         "d": "1D, 2C, 3B, 4A",
    #     },
    #     "correct": ["a"],
    #     "points": 1,
    #     "explanation": (
    #         "Výstupní testware testovacích činností je definován takto:\n"
    #         "A. Testovací analýza - prioritizované testovací podmínky (4) (např. akceptační kritéria) a reporty o defektech v testovací bázi.\n"
    #         "B. Návrh testů - prioritizované testovací případy, testovací listiny, položky pokrytí (1), požadavky na testovací data a požadavky na testovací prostředí.\n"
    #         "C. Implementace testování - testovací procedury, automatizované testovací skripty, testovací sady, testovací data, harmonogram provádění testů (3) a prvky testovacího prostředí jako jsou stuby, ovladače, simulátory a virtualizace služeb.\n"
    #         "D. Dokončení testování - souhrnný report z testování, zdokumentovaná ponaučení (lessons learned), akce pro zlepšení a požadavky na změny (2) obvykle ve formě jako položek produktového backlogu.\n\n"
    #         "Pak tedy:\n"
    #         "[gold1](a) Je správně.[/gold1] [white bold]Správná kombinace je: 1B, 2D, 3C, 4A[/white bold]\n"
    #         "(b) Není správně\n"
    #         "(c) Není správně\n"
    #         "(d) Není správně\n"
    #     ),
    # },
    # {
    #     "id": 6,
    #     "text": (
    #         "Které z následujících tvrzení o různých testovacích rolích je s [white bold]NEJVĚTŠÍ pravděpodobností SPRÁVNÉ?[/white bold]\n"
    #     ),
    #     "options": {
    #         "a": "Role manažera testování je v agilním vývoji softwaru primárně odpovědností týmu, zatímco role testera je primárně odpovědností jednotlivce mimo tým.",
    #         "b": "Role testera je primárně zodpovědná za monitoring testování a řízení testování, zatímco role manažera testování je primárně zodpovědná za plánování testování a dokončení testování.",
    #         "c": "V agilním vývoji softwaru jsou činnosti managementu testování, probíhající napříč více týmy, vykonávány manažerem testování mimo tým, zatímco některé úkoly managementu testování jsou vykonávány týmem samotným.",
    #         "d": "Role manažera testování je primárně zodpovědná za testovací analýzu a návrh testů, zatímco role testera je primárně zodpovědná za implementaci testování a provedení testů.",
    #     },
    #     "correct": ["c"],
    #     "points": 1,
    #     "explanation": (
    #         "(a) Není správně. Ačkoli je správné říci, že v agilním vývoji softwaru může některé úkoly spojené s rolí manažera testování vykonávat samotný agilní tým, není role testera primárně odpovědností jednoho člověka mimo tým. Místo toho je pravděpodobnější, že budou tuto roli zastávat různí členové týmu dle týmového přístupu.\n"
    #         "(b) Není správně. Role manažera testování se primárně zaměřuje na činnosti související s plánováním testování, monitoringem testování, řízením testování a dokončením testování. Ačkoli je tedy toto tvrzení částečně správné, je nesprávné tvrdit, že role testera je primárně zodpovědná za monitorování a řízení testování.\n"
    #         "[gold1](c) Je správně.[/gold1] [white bold]V agilním vývoji jsou některé úkoly manažera testování vykonávány celým agilním týmem. U testovacích činností, které zasahují do více týmů v rámci organizace, mohou tyto úkoly vykonávat manažeři testování mimo vývojový tým.[/white bold]\n"
    #         "(d) Není správně. Role manažera testování se primárně zaměřuje na činnosti související s plánováním testování, monitorováním testování, řízením testování a dokončením testování, zatímco role testera je primárně zodpovědná za technické a inženýrské aspekty testování, jako je testovací analýza, návrh testů, implementace testování a provedení testů. Role manažera testování tedy obvykle neodpovídá za testovací analýzu a návrh testů (ačkoli tvrzení, že role testera odpovídá především za implementaci a provedení testů je správné).\n"
    #     ),
    # },
    {
        "id": 7,
        "text": ("Která z následujících možností je výhodou týmového přístupu?\n"),
        "options": {
            "a": "Týmy bez testerů.",
            "b": "Zlepšení týmové dynamiky.",
            "c": "Specializace členů týmu.",
            "d": "Větší velikost týmu.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. V týmovém přístupu hrají testeři důležitou roli tím, že sdílejí své odborné znalosti v oblasti testování s týmem a usměrňují vývoj produktu. Spolupracují s ostatními členy týmu na dosažení požadované úrovně kvality a také se zástupci byznysu na vytváření akceptačních testů. Testeři také spolupracují s vývojáři při určování optimální testovací strategie a přístupů k automatizaci testů.\n"
            "[gold1](b) Je správně.[/gold1] [white bold]Je správně. Tím, že co nejefektivněji využívá rozmanité dovednosti každého člena týmu, týmový přístup podporuje týmovou dynamiku, podporuje komunikaci a spolupráci, a vytváří týmovou synergii, která je přínosem pro celý projekt. [/white bold]\n"
            "(c) Není správně. Týmový přístup umožňuje každému členovi týmu s potřebnými dovednostmi a znalostmi převzít jakýkoli úkol, takže specializovaní členové týmu nejsou v tomto přístupu výhodou.\n"
            "(d) Není správně. Neexistuje žádné konkrétní doporučení ohledně optimální velikosti týmů využívajících týmový přístup a nic nenaznačuje tomu, že větší týmy jsou lepší.\n"
        ),
    },
    {
        "id": 8,
        "text": ("\n"),
        "options": {
            "a": "",
            "b": "",
            "c": "",
            "d": "",
        },
        "correct": [""],
        "points": 1,
        "explanation": (""),
    },
    {
        "id": 9,
        "text": ("\n"),
        "options": {
            "a": "",
            "b": "",
            "c": "",
            "d": "",
        },
        "correct": [""],
        "points": 1,
        "explanation": (""),
    },
    {
        "id": 10,
        "text": ("\n"),
        "options": {
            "a": "",
            "b": "",
            "c": "",
            "d": "",
        },
        "correct": [""],
        "points": 1,
        "explanation": (""),
    },
    {
        "id": 11,
        "text": ("\n"),
        "options": {
            "a": "",
            "b": "",
            "c": "",
            "d": "",
        },
        "correct": [""],
        "points": 1,
        "explanation": (""),
    },
    {
        "id": 12,
        "text": ("\n"),
        "options": {
            "a": "",
            "b": "",
            "c": "",
            "d": "",
        },
        "correct": [""],
        "points": 1,
        "explanation": (""),
    },
]
