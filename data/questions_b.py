"""otázky pro testování ISTQB Foundation Level B"""

QUESTIONS: list = [
    {
        "id": 1,
        "text": (
            "Které z následujících tvrzení je příkladem toho, proč je testování nezbytné?\n"
        ),
        "options": {
            "a": "[bold]Dynamické testování[/bold] zvyšuje kvalitu tím, že způsobuje selhání testovaných objektů způsoby, ke kterým by se uživatelé nikdy nedostali.",
            "b": "Vývojáři nejprve používají [bold]statické testování[/bold] k nalezení selhání ve svém vlastním kódu, a teprve pak používají dynamické testování.",
            "c": "[bold]Statická analýza[/bold] poskytuje zákazníkům důkaz, že prvky systému, které nedávají žádné výstupy, jsou vhodné k vydání.",
            "d": "[bold]Revize[/bold] zvyšují kvalitu specifikací požadavků a vedou k menšímu počtu změn potřebných v navazujících pracovních produktech.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Často je možné využít [bold]dynamické testování[/bold] k vyvolání selhání testovaného objektu způsoby, ke kterým by se uživatelé nikdy nedostali, například pomocí vkládání chyb (fault injection). Nicméně, pokud se nemůže takové selhání nikdy vyskytnout u reálných koncových uživatelů, pak není jeho identifikace nijak zvlášť hodnotná, protože testování je v konečném důsledku zaměřeno na zlepšení pracovního produktu pro koncové uživatele. Trávit čas testováním takových selhání není efektivní využití času testerů.\n"
            '(b)Není správně. [bold]Statické testování[/bold] ve formě statické analýzy používají vývojáři k identifikaci defektů v jejich kódu dříve, než toho lze dosáhnout prostřednictvím dynamického testování. Pořád ale platí, že statické testování (a statická analýza) se používá k detekci defektů, nikoli selhání (která jsou identifikována dynamickým testováním). Důvodem, proč je tato odpověď nesprávná, je použití termínu "selhání".\n'
            "(c) Není správně. [bold]Statická analýza[/bold] přímo detekuje defekty v kódu, a její výsledky obvykle využívají vývojáři, nikoliv zákazník.\n"
            "[gold1](d) Je správně.[/gold1]  [white bold]Revize jsou formou statického testování, které lze aplikovat od úplného začátku životního cyklu vývoje softwaru. Nalezení a odstranění defektů v požadavcích tak ušetří pracnost, která by se vyplýtvala při činnostech vývoje, které by s těmito chybnými požadavky souvisely. Pokud by nebyly tyto defekty včas zjištěny a odstraněny a došlo by k jejich detekci v navazujících pracovních produktech (jako je návrh a kód), muselo by dojít ke změně požadavků.[/white bold]\n"
        ),
    },
    {
        "id": 2,
        "text": (
            "Které z následujících tvrzení o zajištění kvality (QA) a/nebo kontrole kvality (QC) je správné?\n"
        ),
        "options": {
            "a": "QA se provádí jako součást testování.",
            "b": "Testování se provádí jako součást QC.",
            "c": "Testování je jiný termín pro QC.",
            "d": "Testování se provádí v rámci QA. ",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. QA se zaměřuje na zlepšování a implementaci procesů s cílem vyhnout se chybám a defektům preventivním způsobem, zatímco testování je jednou z forem QC, která se používá k detekci defektů.\n"
            "[gold1](b) Je správně.[/gold1]  [white bold]QC se snaží dosáhnout odpovídající úrovně kvality zaměřením se na identifikaci a opravu defektů v produktu. Testování je významnou součástí QC a pomáhá tyto defekty odhalit.[/white bold]\n"
            "(c) Není správně. Ačkoli je testování významnou součástí QC a pomáhá odhalovat defekty, existují i další (netestovací) techniky používané v QC, které zahrnují formální metody jako jsou ověření modelu, důkazy správnosti, simulace nebo prototypování.\n"
            "(d) Není správně. QA se zaměřuje na zlepšování a implementaci procesů s cílem vyhnout se chybám a defektům preventivním způsobem, zatímco testování je jednou z forem QC, která se používá k detekci defektů.\n"
        ),
    },
    {
        "id": 3,
        "text": (
            "Jeden ze sedmi principů testování říká, že kompletní testování není možné. Které z následujících tvrzení je příkladem praktického uplatnění tohoto principu?\n"
        ),
        "options": {
            "a": "Vytváření testovacích případů, které pokrývají všechny možné výstupy",
            "b": "Dokumentace všech možných variant testovacích vstupů a stanovení priorit na základě jejich důležitosti.",
            "c": "Zahájení testování co nejdříve za pomoci revizí a dalších metod statického testování.",
            "d": "Použití technik rozdělení tříd ekvivalence a analýzy hraničních hodnot k tvorbě testovacích případů",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "Princip 'kompletní testování není možné' znamená, že není možné otestovat všechny možné kombinace testovacích vstupů za všech okolností s výjimkou triviálních případů. Je lepší zaměřit úsilí na vhodné techniky testování, stanovení priorit testovacích případů a testování založené na rizicích s cílem vybrat z celé množiny vstupů pouze určitévzorky.\n\n"
            "(a) Není správně. Tento princip říká, že není možné otestovat vše kromě triviálních případů. Testování všeho by vyžadovalo testování všech možných variant vstupů za všech okolností, což je obecně neproveditelné, protože existuje prakticky nekonečné množství možností. Testování každého možného očekávaného výsledku tento problém nevyřeší, protože vztah mezi vstupy a očekávanými výsledky se může u každého testovaného objektu lišit. Někdy může existovat prakticky nekonečný počet možných očekávaných výsledků (např. když existuje několik proměnných reprezentujících reálná čísla), zatímco jindy mohou být jen dva (například s jednou proměnnou, kdy je výsledek pravda nebo nepravda).\n"
            "(b) Není správně. Princip říká, že není možné testovat všechny možné varianty vstupů za všech okolností. Je to proto, že pro netriviální systémy existuje prakticky nekonečné množství kombinací. V praxi by proto bylo zdokumentování všech možných variant vstupů nereálné, protože by to trvalo nekonečně dlouho.\n"
            "(c)Není správně. Zahájení testování co nejdříve s využitím revizí a dalších technik statického testování nevyřeší problém s příliš mnoha možnými testovacími případy. Princip 'včasné testování šetří čas a peníze' se týká včasného odstranění defektů s cílem zabránit vzniku následných defektů odvozených pracovních produktů, čímž se sníží náklady a pravděpodobnost selhání.\n"
            "[gold1](d) Je správně.[/gold1] [white bold]Použití rozdělení tříd ekvivalence a analýzy hraničních hodnot ke tvorbě testovacích případů je jedním ze způsobů, jak tento princip uplatnit, protože tyto testovací techniky poskytují systematický návod, jak ze všech možných testovacích případů odvodit jejich konečnou podmnožinu.[/white bold]\n"
        ),
    },
    {
        "id": 4,
        "text": (
            "Která testovací činnost zahrnuje práci s požadavky na testovací data, testovacími podmínkami, požadavky testovacího prostředí a testovacími případy?\n"
        ),
        "options": {
            "a": "Návrh testů.",
            "b": "Provedení testů.",
            "c": "Testovací analýza.",
            "d": "Implementace testování.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1] [white bold]Návrh testů zahrnuje použití testovacích podmínek k vytvoření testovacích případů a dalšího testwaru jako jsou požadavky na testovací data a testovací listiny pro průzkumné testování. Specifikovány jsou také požadavky[/white bold]\n"
            "(b) Není správně. Provedení testů zahrnuje provedení testovacích případů (jako součást testovacích procedur), ale přímo nepokrývá ostatní testware uvedený v otázce, tzn. požadavky na testovací data, požadavky na testovací prostředí a testovací podmínky.\n"
            "(c) Není správně. Testovací analýza se používá k identifikaci funkcionalit, které vyžadují testování. Je analyzována a definována testovací báze, kdy výstupem jsou prioritizované testovací podmínky spolu se souvisejícími riziky. I když tato aktivita zahrnuje práci s testovacími podmínkami, nepokrývá další testware zmíněný v otázce, tzn. požadavky na testovací data, požadavky na testovací prostředí a testovací případy.\n"
            "(d) Není správně. Implementace testování zahrnuje vytváření testovacích procedur jako jsou manuální a automatizované testovací skripty, které se vytvářejí z testovacích případů a mohou být sestaveny do testovacích sad. Testovací procedury jsou prioritizovány a uspořádány v harmonogramu provádění testů. Vytváří se testovací data, nastaví se testovací prostředí a ověří se jeho nastavení. Přestože tato aktivita explicitně pracuje s testovacími případy a může využívat požadavky na testovací data a testovací prostředí k jejich vytvoření, nezahrnuje testovací podmínky.\n"
        ),
    },
    {
        "id": 5,
        "text": (
            "Která z následujících možností bude mít [green]NEJVĚTŠÍ[/green] vliv na testování určitého objektu?\n"
        ),
        "options": {
            "a": "Průměrná úroveň zkušeností marketingového týmu organizace.",
            "b": "Povědomí uživatelů o tom, že je pro ně vyvíjen nový systém.",
            "c": "Délka praxe členů testovacího týmu v testování.",
            "d": "Organizační struktura koncového uživatele pro komerční aplikaci pro streamování hudby.",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Je nepravděpodobné, že by marketingový tým organizace prováděl testování (i když v některých organizacích může být zapojen do akceptačního testování), takže jeho průměrná úroveň zkušeností (která by byla většinově v oblasti marketingu) pravděpodobně nebude mít vliv na to, jak se provádí testování pro daný testovaný objekt.\n"
            "(b) Není správně. Je nepravděpodobné, že úroveň znalostí uživatelů, pro které je systém vyvíjen, ovlivní způsob provádění testování. Jakékoli zapojení uživatelů, které by mohlo ovlivnit způsob provádění testování, bude s větší pravděpodobností výsledkem rozhodnutí učiněných testery, zákazníkem a projektovým manažerem.\n"
            "[gold1](c) Je správně.[/gold1] [white bold]Délka praxe členů testovacího týmu pomůže určit potřebné schopnosti a znalosti (např. různých nástrojů a typů defektů), které členové týmu uplatní při testování.[/white bold]\n"
            "(d) Není správně. Organizační struktura různých koncových uživatelů (kteří se mohou měnit) může být odlišná. Při testování aplikace tedy nemusí být známo, kdo bude koncovým uživatelem, a organizační struktura tohoto uživatele tak může mít jen malý vliv na způsob provádění testování.\n"
        ),
    },
    {
        "id": 6,
        "text": (
            "Které z následujících tvrzení je [green]SPRÁVNÝM[/green] příkladem přínosu trasovatelnosti?\n"
        ),
        "options": {
            "a": "Trasovatelnost mezi zmírněnými riziky a úspěšnými (passed) testovacími případy pomáhá určit úroveň zbytkového rizika.",
            "b": "Trasovatelnost mezi uživatelskými požadavky a výsledky testů pomáhá měřit postup prací v projektu v porovnání s byznysovými cíli.",
            "c": "Trasovatelnost mezi testery a neúspěšnými (failed) testovacími případy pomáhá určit úroveň dovedností testerů.",
            "d": "Trasovatelnost mezi zjištěnými riziky a sepsanými testovacími podmínkami pomáhá určit, která rizika stojí za to testovat.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Trasovatelnost mezi zmírněnými riziky a úspěšnými (passed) testovacími případy neposkytuje dostatek informací. Aby byla rizika testováním zmírněna, musel by k nim být přiřazen úspěšný (passed) testovací případ. Pro posouzení zbytkového (reziduálního) rizika je nezbytná sledovatelnost mezi všemi riziky a výsledky testů, což umožňuje identifikovat jako zbytková ta rizika, která nejsou pokryta žádným úspěšným testem.\n"
            "[gold1](b) Je správně.[/gold1] [bold white]Trasovatelnost mezi uživatelskými požadavky a výsledky testů poskytuje informace o tom, které požadavky uživatelů již byly testovány. Tím měří postup projektových prací (v kontextu testování) oproti byznysovým cílům.[/bold white]\n"
            "(c) Není správně. Není jasné, zda neúspěšné testovací případy vypovídají o schopnostech testera více než úspěšné testovací případy. Částečně by to záviselo na cílech testování (např. budování důvěry nebo vyvolání selhání). Měření testerů ve smyslu úspěšných a neúspěšných testovacích případů může být také kontraproduktivní, protože by mohlo způsobit to, že testeři optimalizují své testování podle této metriky a nikoliv podle cílů testování.\n"
            "(d) Není správně. Trasovatelnost mezi identifikovanými riziky a vytvořenými testovacími podmínkami umožňuje určit, jaké další testovací podmínky je nutné napsat. Určení, která rizika stojí za to testovat, je součástí managementu rizik, zejména pak zmírňování rizik.\n"
        ),
    },
    {
        "id": 7,
        "text": (
            "Která z následujících možností je [green]NEJPRAVDĚPODOBNĚJŠÍM[/green] příkladem toho, že tester při testování používá nějakou [bold]obecnou dovednost[/bold], která je užitečná z hlediska testování?\n"
        ),
        "options": {
            "a": "Díky hlubokým znalostem různých počítačových her si tester dobře rozumí s jedním z vývojářů, který se také věnuje hrám.",
            "b": "Tester je bývalý pilot a je schopen lépe porozumět akceptačním kritériím řídicího systému helikoptéry.",
            "c": "Tester dříve pracoval jako programátor a své dovednosti v této oblasti využil k lepší komunikaci s byznysovými analytiky.",
            "d": " Tester před zahájením průzkumného testování vytvoří seznam testovacích případů, protože je velmi opatrný a nechce dělat chyby.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Dobré komunikační dovednosti, schopnost aktivního naslouchání a týmové spolupráce umožňují testerovi efektivně komunikovat se všemi zainteresovanými stranami, nicméně hluboká znalost různých počítačových her, která pomáhá dobře vycházet s jedním z vývojářů, není příkladem obecné dovednosti užitečné pro testery.\n"
            "[gold1](b) Je správně.[/gold1] [bold white]Znalost oboru, kterou lze využít pro porozumění a komunikaci s koncovými uživateli a zástupci byznysu, je jednou z obecných dovedností požadovaných po testerech. Tester se zkušenostmi pilota může být schopen lépe posoudit akceptační kritéria řídicího systému vrtulníku.[/bold white]\n"
            "(c) Není správně. Ačkoli by schopnost programovat mohla být považována za technickou znalost, která může zvýšit efektivitu používání některých testovacích nástrojů, je nepravděpodobné, že by tato dovednost zlepšila komunikaci s byznysovými analytiky.\n"
            "(d) Není správně. Ačkoli důkladnost, smysl pro detail, zvídavost a metodický přístup k identifikaci těžko zjistitelných defektů jsou pro testery užitečné obecné dovednosti, lze pochybovat o tom, že by testeři vygenerovali testovací případy již před zahájením průzkumného testování. Je to proto, že jednou z hlavních zásad průzkumného testování je, že testovací případy jsou generovány během testování (nejsou napsány předem).\n"
        ),
    },
    {
        "id": 8,
        "text": (
            "Které z následujících tvrzení je [bold]výhodou týmového přístupu?[/bold]\n"
        ),
        "options": {
            "a": "Umožňuje členům týmu kdykoliv převzít jakoukoliv roli",
            "b": "K podpoře kompletního vývojového projektu je potřeba pouze jeden tým.",
            "c": "Začleňuje zástupce byznysu a vývojáře do jednoho týmu.",
            "d": "Vytváří týmovou soudržnost (synergii), což prospívá celému projektu.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Týmový přístup znamená, že se jakýkoliv člen týmu s potřebnými dovednostmi a znalostmi může ujmout jakéhokoliv úkolu. To ale neznamená, že může kdykoliv zastat jakoukoliv roli. Obvykle členové týmu přebírají pouze ty role, ve kterých se cítí kompetentní. Nelze obecně říci, že každý člen týmu zvládne jakoukoli roli.\n"
            "(b) Není správně. Týmový přístup se vztahuje ke způsobu práce jednoho konkrétního týmu (typicky při agilním vývoji softwaru). Nevztahuje se na to, jak má pracovat více týmů na větších projektech a neříká nic o tom, že na celý projekt je zapotřebí pouze jeden „velký“ tým.\n"
            "(c) Není správně. Týmový přístup nepředpokládá, že každý člen týmu bude zapojen do každého důležitého rozhodnutí. Například není nutné, aby se zástupci byznysu (např. vlastník produktu) podíleli na každém technickém rozhodnutí, které nemá vliv na výsledek z pohledu byznysu. Realizace takového přístupu by naopak zbytečně zpomalovala postup týmu.\n"
            "[gold1](d) Je správně.[/gold1] [bold white]Týmový přístup co nejefektivněji využívá rozmanité dovednosti každého člena, a tím podporuje lepší týmovou dynamiku, posiluje efektivní komunikaci a spolupráci a vytváří soudržnost (synergii), z níž těží celý projekt.[/bold white]\n"
        ),
    },
    {
        "id": 9,
        "text": (
            "Které z následujících tvrzení o zvoleném životním cyklu vývoje softwaru je [green]SPRÁVNÉ?[/green]\n"
        ),
        "options": {
            "a": "Pokud se používá [bold]agilní vývoj softwaru[/bold], automatizace systémových testů nahrazuje potřebu regresního testování.",
            "b": "Pokud se používá [bold]sekvenční model vývoje[/bold], pak je pro dynamické testování obvykle vyhrazena jeho pozdější fáze.",
            "c": "Pokud se používá [bold]iterativní vývojový model[/bold], pak je testování komponent obvykle manuálně prováděno vývojáři.",
            "d": "Pokud se používá [bold]inkrementální (přírůstkový) vývojový model[/bold], pak se statické testování provádí v počátečních přírůstcích a dynamické testování v pozdějších přírůstcích.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Při agilním vývoji softwaru jsou výstupy vytvářeny v každé iteraci a časté dodávání přírůstků vyžaduje rozsáhlé regresní testování. Ačkoli některé (nebo všechny) testy z tohoto regresního testování mohou být automatizované, regresní testování (ať už automatizované nebo manuální) nemůže být nahrazeno automatizací systémových testů.\n"
            "[gold1](b) Je správně.[/gold1] [bold white]Pokud se používá sekvenční vývojový model, pak není v raných fázích životního cyklu k dispozici žádný spustitelný kód, a proto se během této doby provádí statické testování (např. revize). V pozdějších fázích životního cyklu (kdy už je k dispozici spustitelný kód) je možné provádět dynamické testování. Je nutno ale poznamenat, že příprava na dynamické testování často probíhá právě v těchto raných fázích životního cyklu vývoje softwaru.[/bold white]\n"
            "(c) Není správně. Pokud se používá iterativní vývojový model (např. agilní vývoj softwaru), pak lze pro regresní testování v každé iteraci použít testy komponent. V takovém případě existuje pádný důvod pro jejich automatizaci, protože budou spouštěny často. Naopak je jen malá pravděpodobnost, že by se našel pádný argument pro to, aby je vývojáři prováděli manuálně.\n"
            "(d) Není správně. Ve většině modelů inkrementálního vývoje jsou výstupy vytvářeny v každém přírůstku, což vyžaduje statické i dynamické testování ve všech úrovních testování pro každý dodaný přírůstek.\n"
        ),
    },
    {
        "id": 10,
        "text": (
            "Které z následujících tvrzení je [bold]příkladem osvědčeného postupu[/bold] v testování, který platí pro [bold]všechny životní cykly vývoje softwaru[/bold]?\n"
        ),
        "options": {
            "a": "Testeři by měli revidovat pracovní produkty v rámci následující fáze vývoje.",
            "b": "Testeři by měli revidovat pracovní produkty, jakmile jsou k dispozici jejich rozpracované verze (drafts).",
            "c": "Testeři by měli revidovat pracovní produkty před zahájením testovací analýzy a návrhu testů.",
            "d": "Testeři by měli pracovní produkty revidovat ihned po jejich vydání",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Testeři by měli revidovat pracovní produkty v okamžiku, kdy jsou k dispozici pracovní verze tak, aby využili včasné testování (jako součást principu shift left). Pokud by čekali do další vývojové fáze, pak by mohly být zahájeny zbytečné vývojové (a testovací) práce na nerevidovaných chybných pracovních produktech.\n"
            "[gold1](b) Je správně.[/gold1] [bold white]Testeři by měli revidovat pracovní produkty v okamžiku, kdy jsou k dispozici pracovní verze tak, aby využili včasné testování (jako součást principu shift left).[/bold white]\n"
            "(c) Není správně. Testeři obvykle revidují ty pracovní produkty, které tvoří testovací bázi v rámci testovací analýzy, nikoli před testovací analýzou a návrhem testů.\n"
            "(d) Není správně. Testeři by měli revidovat pracovní produkty v okamžiku, kdy jsou k dispozici pracovní verze (drafty) tak, aby využili včasné testování (jako součást principu shift left). Čekání na jejich zveřejnění znamená, že všechny defekty, které by mohly být nalezeny pomocí revize, budou ve zveřejněném pracovním produktu.\n"
        ),
    },
    {
        "id": 11,
        "text": (
            "Která z následujících možností je příkladem přístupu k vývoji iniciovaného testy [bold](test first)?[/bold]\n"
        ),
        "options": {
            "a": "Vývoj řízený testy (TDD).",
            "b": "Vývoj řízený pokrytím.",
            "c": "Vývoj řízený kvalitou.",
            "d": "Vývoj řízený užitnými funkcemi (features)",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a)Je správně.[/gold1] [bold white]Vývoj řízený testováním (TDD) je známým příkladem vývoje iniciovaného testy.[/bold white]\n"
            "(b)Není správně. Vývoj řízený pokrytím není správným příkladem vývoje iniciovaného testy.\n"
            "(c)Není správně. Vývoj řízený kvalitou není správným příkladem vývoje iniciovaného testy \n"
            "(d)Není správně. Vývoj řízený (užitnými) vlastnostmi není příkladem vývoje iniciovaného testy, ale jedná se o agilní metodiku vývoje softwaru založenou na dodávání užitných vlastností (na rozdíl od uživatelských scénářů ve Scrumu). \n"
        ),
    },
    {
        "id": 12,
        "text": (
            "Které z následujících tvrzení o [bold]DevOps[/bold] je [green]SPRÁVNÉ?[/green]\n"
        ),
        "options": {
            "a": "Aby se urychlil proces vydávání, používá se průběžná integrace, která vývojáře nabádá k rychlému dodávání kódu bez nutnosti dokončit testování komponent.",
            "b": "Aby bylo možné častěji aktualizovat a vydávat systémy, je zapotřebí mnoho automatizovaných regresních testů s cílem snížit riziko regrese.",
            "c": "Aby testeři přistupovali stejně k vývojářům i zástupcům provozu, navýší pracnost věnovanou testování vydání (releasů) ze strany provozu s využitím principu shift right.",
            "d": "Aby se vytvořila lepší soudržnost (synergie) mezi testery, vývojáři a zástupci provozu, musí být testování plně automatizované (tzn. bez manuálního testování).",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. DevOps obohacuje testování několika způsoby, například poskytováním rychlé zpětné vazby o kvalitě kódu, automatizovaným regresním testováním (které minimalizuje riziko regrese) a podporou principu shift left s dodáváním vysoce kvalitního kódu a testů komponent. To je z velké části zajištěno prostřednictvím průběžné integrace, kdy vývojáři dodávají společně se svým novým kódem také testy komponent, které musí projít, jinak není kód akceptován do sestavení (buildu). Vývojáři proto musí dokončit testování komponent.\n"
            "[gold1](b) Je správně.[/gold1] [bold white]DevOps obohacuje testování několika způsoby, například poskytováním rychlé zpětné vazby o kvalitě kódu, automatizovaným regresním testováním, které minimalizuje riziko regrese, a podporou principu shift left s dodáváním vysoce kvalitního kódu a testů komponent.[/bold white]\n"
            "(c) Není správně. DevOps obohacuje testování několika způsoby, například poskytováním rychlé zpětné vazby o kvalitě kódu, automatizovaným regresním testováním (které minimalizuje riziko regrese) a podporou principu shift left s dodáváním vysoce kvalitního kódu a testů komponent. Testeři se nesnaží vyvažovat svůj přístup k vývojářům a provozu tím, že by věnovali více času testování vydání, ačkoliv je možné tento princip (tzv. shift right neboli testování v produkci) možné klidně používat.\n"
            "(d) Není správně. Automatizované procesy, jako je průběžná integrace/průběžné doručování (CI/CD) v DevOps, pomáhají se stabilizací testovacího prostředí a snižují potřebu manuálního testování, existuje však riziko přehlédnutí důležitosti manuálního testování, zejména z pohledu uživatele.\n"
        ),
    },
    {
        "id": 13,
        "text": (
            "[bold]Která[/bold] z následujících možností bude s [orange1]NEJVĚTŠÍ[/orange1] pravděpodobností provedena v rámci [bold]systémového testování?[/bold]\n"
        ),
        "options": {
            "a": "Testování bezpečnosti úvěrového systému nezávislým testovacím týmem.",
            "b": "Testování rozhraní směnárenského systému s externím bankovním systémem.",
            "c": "Beta testování systému pro vzdálenou výuku přímo vývojáři výukového softwaru.",
            "d": "Testování interakcí mezi uživatelským rozhraním a databází systému pro oddělení lidských zdrojů (HR).",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1] [bold white]Systémové testování zkoumá chování a schopnosti celého systému a zahrnuje nefunkcionální testování kvalitativních charakteristik, například testování bezpečnosti. Tento typ testování je často prováděn nezávislým testovacím týmem na základě specifikací systému.[/bold white]\n"
            "(b) Není správně. [bold]Systémové integrační testování[/bold] zkoumá rozhraní s jinými systémy a externími službami.\n"
            "(c) Není správně. [bold]Beta testování[/bold] je typ [bold]akceptačního testování[/bold] prováděného v externí lokalitě rolemi mimo vývojovou organizaci.\n"
            "(d) Není správně. [bold]Integrační testování komponent[/bold] zahrnuje testování interakcí mezi komponentami systému, což jsou například uživatelská rozhraní a databáze.\n"
        ),
    },
    {
        "id": 14,
        "text": "Které z následujících tvrzení je [green]SPRÁVNÉ?[/green]\n",
        "options": {
            "a": "Počet [bold]regresních testů[/bold] se v průběhu projektu zvyšuje, zatímco počet [bold]konfirmačních testů[/bold] se v průběhu projektu snižuje.",
            "b": "[bold]Regresní testy[/bold] jsou vytvářeny a prováděny při opravách testovaného objektu, zatímco [bold]konfirmační testy[/bold] při jeho vylepšeních.",
            "c": "[bold]Regresní testování[/bold] se zabývá kontrolou, zda provozní prostředí zůstává nezměněno, zatímco [bold]konfirmační testování[/bold] se zabývá testováním změn testovaného objektu.",
            "d": "[bold]Regresní testování[/bold] se zabývá nepříznivými účinky v nezměněném kódu, zatímco [bold]konfirmační testování[/bold] se zabývá testováním změněného kódu.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Počet regresních testů v průběhu projektu roste, protože se změnami v systému jsou obvykle zapotřebí nové regresní testy. Podobně se obvykle zvyšuje také počet konfirmačních testů, protože pro každou opravu systému jsou potřeba nové konfirmační testy.\n"
            "(b) Není správně. Je to naopak. Konfirmační testy jsou vytvořeny a spuštěny, když je testovaný objekt opravován, a regresní testy jsou (v ideálním případě) spuštěny vždy, když je testovaný objekt rozšiřován (měněn).\n"
            "(c) Není správně. Konfirmační testování ověřuje, že defekt byl správně opraven, a proto se týká testování změn testovaného objektu. Regresní testování však zajišťuje, aby změny (včetně změnprovozního prostředí) neměly negativní vliv na nezměněný software,a proto nekontroluje, zda provozní prostředí zůstává nezměněno.\n"
            "[gold1](d) Je správně.[/gold1] [bold white]Regresní testování zajišťuje, že změny nebudou mít negativní vliv na nezměněný software. Konfirmační testování ověřuje, že defekt byl opraven, týká se tedy změněného kódu.[/bold white]\n"
        ),
    },
    {
        "id": 15,
        "text": (
            "Která z následujících možností je příkladem defektu, který lze zjistit [bold]statickým testováním[/bold], ale NE [bold]dynamickým testováním[/bold]?\n"
        ),
        "options": {
            "a": "Nedostatečná použitelnost uživatelského rozhraní.",
            "b": "Nedosažitelný kód.",
            "c": "Vysoká doba odezvy pro většinu uživatelů.",
            "d": "Požadované funkcionality, které ale nejsou implementovány v kódu.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Nedostatečnou použitelnost poskytovanou prostřednictvím uživatelského rozhraní lze zjistit prostřednictvím revize s využitím vhodného kontrolního seznamu. Nedostatečnou použitelnost lze také identifikovat tak, že několik typických uživatelů dynamicky testuje uživatelské rozhraní a poskytuje zpětnou vazbu o jeho použitelnosti.\n"
            "[gold1](b) Je správně.[/gold1] [bold white]Revize kódu může detekovat kód, který nemůže být žádným způsobem spuštěn (tzv. nedosažitelný kód). Dynamické testy mohou testovat pouze dosažitelný kód a nemohou tedy zjistit, že daný kód nelze spustit při všech možných kombinacích vstupů a stavů vstupů.[/bold white]\n"
            "(c) Není správně. Špatnou dobu odezvy u většiny očekávaných uživatelů je obtížné určit bez spuštění kódu (tj. statickým testováním), takže v této situaci by dynamické testování defekt najít mohlo, naopak statické testování jej pravděpodobně nenajde.\n"
            "(d) Není správně. Revize kódu někým, kdo zná požadované funkcionality, by mohla identifikovat, že nebyly implementovány v kódu. Dynamické testování by mohlo být použito ke zjištění, že obecně nebyly implementovány vůbec.\n"
        ),
    },
    {
        "id": 16,
        "text": (
            "Která z následujících možností je výhodou včasné a časté zpětné vazby zainteresovaných stran?\n"
        ),
        "options": {
            "a": "Manažeři mají přehled o méně produktivních vývojářích.",
            "b": "Umožňuje projektovým manažerům upřednostňovat komunikaci se zainteresovanými stranami.",
            "c": "Usnadňuje včasnou komunikaci o potenciálních problémech s kvalitou.",
            "d": "Koncoví uživatelé lépe chápou, proč se dodání pracovního produktu zpožďuje.",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Zpětná vazba pochází od zainteresovaných stran (např. zástupců byznysu nebo koncových uživatelů), nikoli od vývojářů, takže pravděpodobně neinformuje manažery o tom, kteří vývojáři jsou více či méně produktivní.\n"
            "(b) Není správně. Včasnou a častou zpětnou vazbu od zainteresovaných stran nepoužívají projektoví manažeři k tomu, aby upřednostnili způsob, jakým komunikují s různými zainteresovanými stranami.\n"
            "[gold1](c) Je správně.[/gold1] [bold white]Získání zpětné vazby od zainteresovaných stran včasně a často v procesu vývoje softwaru může být velmi přínosné, protože umožňuje včasnou komunikaci o potenciálních problémech s kvalitou, může zabránit nedorozuměním ohledně požadavků a zajišťuje, že jakékoli změny v požadavcích zainteresovaných stran budou pochopeny a implementovány včas.[/bold white]\n"
            "(d) Není správně. Včasná a častá zpětná vazba může zabránit vývoji produktu, který nesplňuje potřeby zainteresovaných stran a/nebo vede k nákladnému přepracování a zmeškání termínů. V ideálním případě by tedy nemělo dojít k žádnému zpoždění. Zpětná vazba navíc směřuje od zainteresovaných stran (což jsou také koncoví uživatelé), nikoliv k nim. Samotné poskytování zpětné vazby ze strany uživatelů tedy nezlepšuje jejich vlastní porozumění.\n"
        ),
    },
    {
        "id": 17,
        "text": (
            "Předpokládejme následující popis úkolů:\n"
            "--------------------------------------------------------------\n"
            "1. Hodnotí se charakteristiky kvality a vybírají výstupní kritéria.\n"
            "2. Každý má přístup k pracovnímu produktu.\n"
            "3. Anomálie v pracovním produktu jsou identifikovány\n"
            "4. Anomálie jsou diskutovány.\n\n"
            "Dále předpokládejme tyto činnosti procesu revize:\n"
            "--------------------------------------------------------------\n"
            "A. Individuální revize.\n"
            "B. Zahájení revize.\n"
            "C. Plánování.\n"
            "D. Komunikace a analýza.\n\n"
            "[bold]Která[/bold] z následujících možností [green]NEJLÉPE[/green] přiřazuje popisy úkolů k činnostem?"
        ),
        "options": {
            "a": "1B, 2C, 3D, 4A",
            "b": "1B, 2D, 3C, 4A",
            "c": "1C, 2A, 3B, 4D",
            "d": "1C, 2B, 3A, 4D",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "S ohledem na každý z uvedených popisů úkolů platí, že:\n"
            "[bold]1. Jsou vybrány hodnocené kvalitativní charakteristiky a výstupní kritéria. Plánování (C):[/bold]\n"
            "Definování rozsahu revize, účelu, pracovního produktu, který má být přezkoumán, kvalitativních charakteristik, které mají být hodnoceny, oblastí zaměření, výstupních kritérií, podpůrných informací, což jsou např. normy, pracnost a časové rámce.\n"
            "[bold]2. Každý má přístup k pracovnímu produktu. Zahájení revize (B):[/bold]\n"
            "Zajistit, aby všichni účastníci měli přístup k pracovnímu produktu a potřebným zdrojům, a vyjasnit jejich role a odpovědnosti.\n"
            "[bold]3. Anomálie v pracovním produktu jsou identifikovány. Individuální revize (A):[/bold]\n"
            "Vyhodnocení kvality pracovního produktu, identifikace a zaznamenání anomálií, doporučení a otázek pomocí technik revize jako je revize založená na kontrolních seznamech a revize založená na scénářích.\n"
            "[bold]4. Anomálie jsou analyzovány a diskutovány. Komunikace a analýza (D):[/bold]\n"
            "Analýza a diskuze o každé anomálii, určení jejího stavu, vlastnictví a požadovaných akcí, a učinit rozhodnutí při revizi, obvykle na schůzce. To by mohlo zahrnovat určení potřeby následné revize.\n\n"
            "Tedy:\n"
            "(a) Není správně.\n"
            "(b) Není správně.\n"
            "(c) Není správně.\n"
            "[gold1](d) Je správně.[/gold1] [bold white]Správná kombinace je: 1C, 2B, 3A, 4D[/bold white]\n"
        ),
    },
    {
        "id": 18,
        "text": (
            "Předpokládejme následující role v procesu revize:\n"
            "--------------------------------------------------------------\n"
            "1. Zapisovatel.\n"
            "2. Vedoucí revize.\n"
            "3. Moderátor (facilitátor).\n"
            "4. Manažer.\n\n"
            "Dále předpokládejme následující seznam zodpovědností:\n"
            "--------------------------------------------------------------\n"
            "A. Zajišťuje efektivní průběh revizních schůzek a nastavení komfortního prostředí pro revize.\n"
            "B. Zaznamenává informace o revizi, jako jsou různá rozhodnutí a nové anomálie zjištěné během revizní schůzky.\n"
            "C. Rozhoduje o tom, co má být revidováno, a rozhoduje o zdrojích, jako jsou lidé nebo čas.\n"
            "D. Přebírá celkovou odpovědnost za revizi, například organizuje, kdy a kde se bude revize konat.\n\n"
            "Která z následujících možností [green]NEJLÉPE[/green] přiřazuje role k zodpovědnostem?"
        ),
        "options": {
            "a": "1A, 2B, 3D, 4C",
            "b": "1A, 2C, 3B, 4D",
            "c": "1B, 2D, 3A, 4C",
            "d": "1B, 2D, 3C, 4A",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "S ohledem na každou z uvedených rolí platí, že:\n"
            "[bold]1. Zapisovatel[/bold] - zodpovídá za shromažďování zpětné vazby od revidujících a zdokumentování informací o revizi jako jsou učiněná rozhodnutí a jakékoli nové anomálie zjištěné během revizní schůzky. B:\n"
            "[bold]Zaznamenává[/bold] informace o revizi, jako jsou rozhodnutí a nové anomálie zjištěné během revizní schůzky.\n"
            "[bold]2. Vedoucí revize[/bold] - zodpovídá za dohled nad procesem revize jako je výběr členů revizního týmu, plánování revizních schůzek a zajištění úspěšného dokončení revize. D:\n"
            "[bold]Přebírá[/bold] celkovou odpovědnost za revizi, například organizuje, kdy a kde se bude revize konat.\n"
            "[bold]3. Facilitátor (nebo moderátor)[/bold] - odpovídá za zajištění efektivního průběhu revizních schůzek včetně řízení času, vedení diskusí a vytvoření komfortního prostředí, kde může každý svobodně vyjádřit svůj názor. A:\n"
            "[bold]Zajišťuje[/bold] efektivní průběh revizních schůzek a nastavení komfortního prostředí pro revizi.\n"
            "[bold]4. Manažer[/bold] - odpovídá za rozhodování o tom, co je třeba revidovat, a za přidělování zdrojů pro revizi (např. lidé nebo čas). C:\n"
            "[bold]Rozhoduje[/bold] o tom, co má být revidováno, a rozhoduje o zdrojích jako jsou lidé nebo čas.\n\n"
            "Tedy:\n"
            "(a) Není správně.\n"
            "(b) Není správně.\n"
            "[gold1](c) Je správně.[/gold1] [bold white]Správná kombinace je: 1B, 2D, 3A, 4C[/bold white]\n"
            "(d) Není správně."
        ),
    },
    {
        "id": 19,
        "text": (
            "Které z následujících tvrzení [orange1]NEJLÉPE[/orange1] popisuje rozdíl mezi testováním dle [blue]rozhodovací tabulky[/blue] a [green]testováním větví[/green]?\n"
        ),
        "options": {
            "a": "Při testování dle rozhodovací tabulky jsou testovací případy odvozeny z rozhodovacích příkazů v kódu. Při testování větví jsou testovací případy odvozeny ze znalosti řídicího toku testovaného objektu. ",
            "b": "Při testování dle rozhodovací tabulky jsou testovací případy odvozeny ze specifikace popisující byznysovou logiku. Při testování větví jsou testovací případy založeny na předvídání potenciálních defektů ve zdrojovém kódu.",
            "c": "Při testování dle rozhodovací tabulky jsou testovací případy odvozeny ze znalosti řídicího toku testovaného objektu. Při testování větví jsou testovací případy odvozeny ze specifikace popisující byznysovou logiku.",
            "d": "Při testování dle rozhodovací tabulky jsou testovací případy nezávislé na tom, jak je software implementován. Při testování větví lze testovací případy vytvořit až po návrhu nebo implementaci kódu.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Testování dle rozhodovací tabulky je technika testování černé skříňky, nikoli technika testování bílé skříňky. Testovací případy nejsou tedy založeny na rozhodnutích ve zdrojovém kódu. Při testování větví jsou testovací případy odvozeny ze znalosti řídicích toků testovaného objektu.\n"
            "(b) Není správně. Předvídání potenciálních defektů se používá při odhadování chyb (technika testování založená na zkušenostech), nikoli při testování větví (technika testování bílé skříňky). Při testování dle rozhodovací tabulky jsou testovací případy odvozeny ze specifikace, která popisuje byznysovou logiku.\n"
            "(c) Není správně. Pokud je testovací případ založen na znalosti řídicího toku testovaného objektu, jedná se o techniku testování bílé skříňky. Testování dle rozhodovací tabulky je obvykle založeno na analýze byznysové logiky, jedná se tedy o techniku testování černé skříňky. Při testování větví nejsou testovací případy odvozeny ze specifikace - to by z něj udělalo techniku testování černé skříňky. Testování větví je technika testování bílé skříňky, kdy jsou testovací případy odvozeny na základě struktury zdrojového kódu.\n"
            "[gold1](d) Je správně.[/gold1] [bold white]Testování dle rozhodovací tabulky je technika testování černé skříňky, takže je založena na analýze specifikovaného chování testovaného objektu bez odkazu na jeho vnitřní strukturu. Testovací případy jsou tedy nezávislé na tom, jak je software implementován. Testování větví je technika testování bílé skříňky, takže testovací případy jsou založeny na analýze vnitřní struktury a procesů testovaného objektu. Vzhledem k tomu, že testovací případy jsou závislé na návrhu a implementaci daného softwaru, mohou být vytvořeny pouze po jeho ukončení nebo po jeho implementaci (pokud není použita technika TDD).[/bold white]\n"
        ),
    },
    {
        "id": 20,
        "text": (
            "Zákazníci sítě mycích linek TestWash mohou využít věrnostní karty se záznamy o počtu provedených mytí. [bold]Počáteční hodnota je 0.[/bold] Po vjezdu do myčky systém [bold]zvýší číslo na kartě o jednu.[/bold] Tato hodnota představuje číslo aktuálního mytí. Na základě tohoto čísla systém rozhodne, na [white]jakou slevu má zákazník nárok.[/white]\n\n"
            "Pro každé [white]desáté[/white] mytí poskytuje systém 10% slevu a pro každé [white]dvacáté[/white] mytí další 40% slevu (tj. 50% slevu celkem).\n\n"
            "Která z následujících sad vstupních dat (chápaná jako čísla aktuálního mytí) dosahuje [white]nejvyššího pokrytí tříd ekvivalence?[/white]\n"
        ),
        "options": {
            "a": "19, 20, 30",
            "b": "11, 12, 20",
            "c": "1, 10, 50",
            "d": "10, 29, 30, 31",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1] [bold white]19 pokrývá třídu 'bez slevy', 20 pokrývá třídu '50 % sleva' a 30 pokrývá třídu '10 % sleva'. Tyto tři hodnoty pokrývají všechny tři platné třídy ekvivalence.[/bold white]\n"
            "(b) Není správně. [bold]11 a 12[/bold] pokrývají třídu 'bez slevy', zatímco [bold]20[/bold] pokrývá třídu '50 % sleva', takže celkově pokrývají dvě ze tří platných tříd ekvivalence\n"
            "(c) Není správně. 1 pokrývá třídu 'bez slevy', zatímco [bold]10[/bold] a [bold]50[/bold] pokrývají třídu '10 % sleva'. Třída '50 % sleva' není pokryta, takže celkově jsou pokryty dvě ze tří platných tříd ekvivalence.\n"
            "(d) Není správně. [bold]29 a 31[/bold] pokrývají třídu 'bez slevy', zatímco [bold]10 a 30[/bold] pokrývají třídu '10 % sleva'. Třída '50 % sleva' není pokryta, takže celkově jsou pokryty dvě ze tří platných tříd ekvivalence.\n"
        ),
    },
    {
        "id": 21,
        "text": (
            "Testujete formulář, který ověřuje správnost délky zadaného hesla. Formulář akceptuje heslo se správnou délkou a odmítne heslo, které je [white]příliš krátké nebo příliš dlouhé[/white]. Délka hesla je správná, pokud má [white]6 až 12 znaků[/white] včetně. Ostatní případy jsou považovány za [white]nesprávné[/white].\n\n"
            "Formulář je nejprve prázdný (délka hesla = 0). Na proměnnou [bold]délka hesla[/bold] aplikujete analýzu hraničních hodnot (BVA).\n\n"
            "Vaše sada testovacích případů dosáhne 100% pokrytí 2-hodnotové analýzy hraničních hodnot. Tým se rozhodl, že vzhledem k vysokému riziku této komponenty by měly být přidány takové testovací případy, aby bylo zajištěno 100% pokrytí 3-hodnotové BVA.\n\n"
            "Jaké další délky hesel by měly být testovány, aby toho bylo dosaženo?\n"
        ),
        "options": {
            "a": "4, 5, 13, 14",
            "b": "7, 11",
            "c": "1, 5, 13",
            "d": "1, 4, 7, 11, 14",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "Obor hodnot pro délku hesla má tři třídy ekvivalence:\n"
            "• hesla příliš krátká [bold]{0, 1, ..., 4, 5}[/bold]\n"
            "• správná hesla [bold]{6, 7, ..., 11, 12}[/bold]\n"
            "• hesla příliš dlouhá [bold]{13, 14, ...}[/bold]\n\n"
            "Abychom dosáhli plného pokrytí pro [white]3-hodnotovou BVA[/white], musíme otestovat následující hodnoty:\n"
            "[white]0, 1, 4, 5, 6, 7, 11, 12, 13, 14[/white].\n\n"
            "Vzhledem k tomu, že 2-hodnotová BVA je již pokryta, znamená to, že jsme již otestovali hesla délky:\n"
            "[white]0, 5, 6, 12 a 13[/white]\n\n"
            "To znamená, že další délky, které je potřeba pokrýt, aby bylo možné přejít z 2-hodnotové na 3-hodnotovou BVA, jsou:\n"
            "[white]1, 4, 7, 11 a 14. [/white].\n\n"
            "tedy:\n"
            "(a) Není správně.\n"
            "(b) Není správně.\n"
            "(c) Není správně.\n"
            "[gold1](d) Je správně.[/gold1]\n"
        ),
    },
    {
        "id": 22,
        "text": (
            "Následující rozhodovací tabulka obsahuje pravidla pro stanovení rizika aterosklerózy\n"
            "[white]┌────────────────────┬────────────┬────────────┬────────────┬────────────┬────────────┐[/white]\n"
            "[white]│                    │ Pravidlo 1 │ Pravidlo 2 │ Pravidlo 3 │ Pravidlo 4 │ Pravidlo 5 │[/white]\n"
            "[white]├────────────────────┴────────────┴────────────┴────────────┴────────────┴────────────┤[/white]\n"
            "[white]│podminky                                                                             │[/white]\n"
            "[white]├────────────────────┬────────────┬────────────┬────────────┬────────────┬────────────┤[/white]\n"
            "[white]│Cholesterol (mg/dl) │   ≤ 124    │   ≤ 124    │ 125 - 200  │ 125 - 200  │   ≥ 201    │[/white]\n"
            "[white]├────────────────────┼────────────┼────────────┼────────────┼────────────┼────────────┤[/white]\n"
            "[white]│Krevní tlak (mm Hg) │   ≤ 140    │   > 140    │   ≤ 140    │   > 140    │     -      │[/white]\n"
            "[white]├────────────────────┴────────────┴────────────┴────────────┴────────────┴────────────┤[/white]\n"
            "[white]│akce                                                                                 │[/white]\n"
            "[white]├────────────────────┬────────────┬────────────┬────────────┬────────────┬────────────┤[/white]\n"
            "[white]│Úroveň rizika       │ velmi nizka│    nizka   │  stredni   │   vysoka   │velmi vysoka│[/white]\n"
            "[white]└────────────────────┴────────────┴────────────┴────────────┴────────────┴────────────┘[/white]\n\n"
            "Navrhli jste testovací případy (TC) s následujícími vstupními daty:\n"
            "[white bold]TC1:[/white bold] [white]Cholesterol = 125 mg/dl Krevní tlak = 141 mm Hg[/white]\n"
            "[white bold]TC2:[/white bold] [white]Cholesterol = 200 mg/dl Krevní tlak = 201 mm Hg[/white]\n"
            "[white bold]TC3:[/white bold] [white]Cholesterol = 124 mg/dl Krevní tlak = 201 mm Hg[/white]\n"
            "[white bold]TC4:[/white bold] [white]Cholesterol = 109 mg/dl Krevní tlak = 200 mm Hg[/white]\n"
            "[white bold]TC5:[/white bold] [white]Cholesterol = 201 mg/dl Krevní tlak = 140 mm Hg[/white]\n\n"
            "Jakého pokrytí rozhodovací tabulky dosáhnou tyto testovací případy?\n"
        ),
        "options": {
            "a": "40 %",
            "b": "60 %",
            "c": "80 %",
            "d": "100 %",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "[bold]V rozhodovací tabulce je pět sloupců. Každý testovací případ pokrývá jeden z nich.[/bold]\n"
            "[white]TC1 a TC2 pokrývají Pravidlo 4.[/white]\n"
            "[white]TC3 a TC4 pokrývají Pravidlo 2.[/white]\n"
            "[white]TC5 pokrývá Pravidlo 5[/white]\n\n"
            "Těchto pět testovacích případů tedy pokrývá tři z pěti sloupců a dosahuje pokrytí (3/5)*100 % = 60 %. Proto je správně možnost (b).\n"
            "Tedy:\n"
            "(a) Není správně.\n"
            "[gold1](b) Je správně.[/gold1]\n"
            "(c) Není správně.\n"
            "(d) Není správně.\n"
        ),
    },
    {
        "id": 23,
        "text": (
            "Úložný systém, jehož model je zobrazen níže ve formě stavového diagramu může ukládat až tři prvky. Proměnná N představuje počet aktuálně uložených prvků.\n"
            "Který z následujících testovacích případů (reprezentovaných jako sekvence událostí) dosahuje nejvyšší úrovně pokrytí platných přechodů?\n\n"
            "              +-----------------------------+\n"
            "              | Přidat [N < 2] / N := N + 1 |\n"
            "              |            (smyčka)         |\n"
            "              v                             |\n"
            "+-------+   Přidat / N := 1          +---------+\n"
            "| START | -------------------------> | ZAPLNĚN |\n"
            "+-------+                            +---------+\n"
            "                                           |\n"
            "                                           | Přidat [N = 2] / N := N + 1\n"
            "                                           v\n"
            "                                   +--------------+\n"
            "                                   | NENÍ ZAPLNĚN |\n"
            "                                   +--------------+\n"
            "                                           |\n"
            "                                           | Odebrat / N := N - 1\n"
            "                                           v\n"
            "                                       +---------+\n"
            "                                       | ZAPLNĚN |\n"
            "                                       +---------+\n"
            "                                           ^\n"
            "                                           |\n"
            "                                       Odebrat [N > 0] / N := N - 1\n"
            "                                       (smyčka zpět)\n"
        ),
        "options": {
            "a": "Přidat, odebrat, přidat, přidat, přidat",
            "b": "Přidat, přidat, přidat, přidat, odebrat, odebrat",
            "c": "Přidat, přidat, přidat, odebrat, odebrat",
            "d": "Přidat, přidat, přidat, odebrat, přidat",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "Označme přechody E1 - E5 (viz obrázek).\n"
            "Proměnná N označuje počet aktuálně uložených prvků. Každá událost [bold]Přidat[/bold] ji zvyšuje o 1 a každá událost [white]Odebrat[/white] ji snižuje o 1. Pokud dojde k události [bold]Přidat[/bold] ve stavu [white]NENÍ ZAPLNĚN[/white], stav se změní na [white]ZAPLNĚN[/white] pouze v případě, že N=2. Pokud je N<2, systém zůstane ve stavu [white]NENÍ ZAPLNĚN[/white]. Pokud N=0, není možná žádná akce [white]Odebrat[/white]. Podobně, pokud N=3, není možná žádná akce [white]Přidat[/white].\n\n"
            "(a) Není správně.\n"
            "(b) Není správně.\n"
            "[gold1](c) Je správně.[/gold1]\n"
            "(d) Není správně.\n"
        ),
    },
    {
        "id": 24,
        "text": (
            "Spouštíte dva testovací případy T1 a T2, oba na stejném kódu.\n"
            "Test T1 dosáhl 40% pokrytí příkazů\n"
            "Test T2 dosáhl 65% pokrytí příkazů.\n"
            "Které z následujících tvrzení musí být nutně pravdivé?\n"
        ),
        "options": {
            "a": "Testovací sada složená z testů T1 a T2 dosahuje 105% pokrytí příkazů.",
            "b": "Existuje alespoň jeden příkaz, který byl spuštěn pomocí T1 i T2.",
            "c": "Alespoň 5 % příkazů v testovaném kódu je nespustitelných.",
            "d": "Testovací sada složená z testů T1 a T2 dosahuje plného pokrytí větví.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Pokrytí je vždy definováno jako procento pokrytých prvků, proto nemůže překročit 100 %\n"
            "[gold1](b)[/gold1] [white bold]Je správně. Pokud by příkazy prováděné T1 a T2 byly disjunktní, pokrytí testovací sadou {T1, T2} by bylo 105 %, což je nemožné (viz odpověď a). Proto musí být alespoň 5 % spustitelných příkazů provedeno T1 i T2.[/white bold]\n"
            "(c) Není správně. Pokrytí příkazů nám neříká nic o počtu nespustitelných příkazů v kódu.\n"
            "(d) Není správně. I v případě, že testovací sada dosáhne úplného pokrytí příkazů, neznamená to, že dosáhne úplného pokrytí větví.\n"
        ),
    },
    {
        "id": 25,
        "text": (
            "Nechť je metrika pokrytí větví definována jako BCov = (X / Y) * 100 %.\n"
            "Co představují [bold white]X a Y[/bold white] v tomto vzorci?\n"
        ),
        "options": {
            "a": "X = počet výsledků rozhodnutí pokrytých testovacími případy\n     Y = celkový počet výsledků rozhodnutí v kódu.",
            "b": "X = počet podmíněných větví pokrytých testovacími případy,\n     Y = celkový počet větví v kódu.",
            "c": "X = počet větví pokrytých testovacími případy,\n     Y = celkový počet větví v kódu.",
            "d": "X = počet podmíněných větví pokrytých testovacími případy,\n     Y = celkový počet výsledků rozhodnutí v kódu.",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "Testování větví je technika testování [white]bílé skříňky[/white], ve které jsou položkami pokrytí větve. Větev je přenos řízení mezi dvěma uzly v grafu řídicího toku zobrazujícího možné sekvence, ve kterých jsou příkazy zdrojového kódu v testovacím objektu prováděny. Každý přenos řízení může být buď nepodmíněný (tj. lineární kód) nebo podmíněný (tj. výsledek rozhodnutí). Pokrytí se měří jako počet větví pokrytých testy k celkovému počtu větví (obvykle vyjádřeno v procentech).\n\n"
            "Tedy:\n"
            "(a) Není správně. Výsledek rozhodnutí je podmíněná větev. Pro testování větví se do X započítávají nejen podmíněné, ale inepodmíněné větve.\n"
            "(b) Není správně. Pokrytí větví počítá nejen podmíněné, ale i nepodmíněné větve\n"
            "[gold1](c) Je správně.[/gold1] [bold white]Pokrytí se měří jako počet větví pokrytých testy k celkovému počtu větví (obvykle vyjádřeno v procentech).[/bold white]\n"
            "(d) Není správně. X i Y počítají pouze podmíněné větve a neberou v úvahu nepodmíněné větve.\n"
        ),
    },
    {
        "id": 26,
        "text": (
            "Která DVĚ z následujících tvrzení poskytují [bold white]NEJLEPŠÍ[/bold white] zdůvodnění pro použití [bold]průzkumného testování?[/bold] \n"
        ),
        "options": {
            "a": "Testeři neměli dostatek času na návrh a provedení testů.",
            "b": "Stávající strategie testování vyžaduje, aby testeři používali formální techniky testování černé skříňky",
            "c": "Specifikace je napsána ve formálním jazyce, který může být zpracován softwarovým nástrojem.",
            "d": "Testeři jsou členy agilního týmu a mají dobré programátorské dovednosti.",
            "e": "Testeři mají zkušenosti z daného odvětví (domény) a dobré analytické schopnosti.",
        },
        "correct": ["a", "e"],
        "points": 1,
        "explanation": (
            "[white]Průzkumné testování[/white] je nejvíce užitečné v případech, kdy je specifikace nedostatečná nebo úplně chybí, taktéž je vhodnou metodou v případě [white]výrazného časového tlaku na testování[/white].\n"
            "[white]Průzkumné testování[/white] je také výhodné jako doplněk jiných (formálnějších) technik testování. [white]Průzkumné testování[/white] bude účinnější v případech, kdy je tester zkušený, má znalosti z daného odvětví a vysokou úroveň klíčových dovedností jako jsou [white]analytické schopnosti, zvídavost a kreativita[/white].\n\n"
            "tedy:\n"
            "[gold1](a) Je správně.[/gold1] [white bold]Průzkumné testování je nejvíce užitečné v případech, kdy je specifikace nedostatečná nebo úplně chybí, taktéž je vhodnou metodou v případě výrazného časového tlaku na testování[/white bold].\n"
            "(b) Není správně. Průzkumné testování není technikou testování černé skříňky.\n"
            "(c) Není správně. Průzkumné testování je užitečné, když jsou specifikace napsané špatně.\n"
            "(d) Není správně. Programátorské dovednosti v zásadě nemají s průzkumným testováním nic společného.\n"
            "[gold1](e) Je správně.[/gold1] [white bold]Průzkumné testování bude účinnější v případech, kdy je tester zkušený, má znalosti z daného odvětví a vysokou úroveň klíčových dovedností jako jsou analytické schopnosti, zvídavost a kreativita[/white bold]\n"
        ),
    },
    {
        "id": 27,
        "text": (
            "Která z následujících možností se [green1]NEJLÉPE[/green1] hodí jako prvek seznamu používaného při testování založeném na [white]kontrolních seznamech[/white]?\n"
        ),
        "options": {
            "a": "Vývojář udělal chybu při implementaci kódu.",
            "b": "Dosažené pokrytí příkazů přesahuje 85 %.",
            "c": "Program funguje správně co se týče funkcionálních a nefunkcionálních požadavků.",
            "d": "Chybové zprávy jsou psány jazykem, kterému uživatel porozumí.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Kontrolní seznamy by měly obsahovat testovací podmínky, které mají být ověřeny. Tato odpověď je příkladem chyby, nikoli testovací podmínky. I kdyby byl tester schopen odvodit některé možné testovací podmínky z možných chyb, je tento popis chyby i tak příliš obecný.\n"
            "(b) Není správně. Kontrolní seznamy by neměly obsahovat položky, které jsou vhodnější jako výstupní kritéria. Tato odpověď je příkladem výstupního kritéria.\n"
            "(c) Není správně. Kontrolní seznamy by neměly obsahovat položky, které jsou příliš obecné. Tato odpověď je velmi obecná věta, která vlastně popisuje cíl testování.\n"
            "[gold1](d) Je správně.[/gold1] [white bold]Toto je příklad testovací podmínky, kterou může prověřit člověk.[/white bold]\n"
        ),
    },
    {
        "id": 28,
        "text": (
            "Uvažujme následující [bold]akceptační kritéria[/bold] uživatelského scénáře napsaná z pohledu vlastníka internetového obchodu.\n\n"
            "[white bold]GIVEN [/white bold]uživatel je přihlášen a je na domovské stránce\n"
            "[white bold]WHEN[/white bold] uživatel klikne na tlačítko Přidat položku\n"
            "[white bold]THEN[/white bold] objeví se formulář Vytvořit položku\n"
            "[white bold]AND[/white bold] uživatel je schopen zadat název a cenu nové položky\n\n"
            "V jakém formátu jsou tato akceptační kritéria napsána?\n"
        ),
        "options": {
            "a": "S orientací na pravidla.",
            "b": "S orientací na scénáře.",
            "c": "S orientací na produkt.",
            "d": "S orientací na proces.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Formát orientovaný na pravidla zahrnuje formáty, jako jsou ověřovací seznamy (checklisty) ve formě odrážek nebo tabulky mapující vstupy na výstupy zobrazující explicitně pravidla, která je třeba dodržovat. Given/When/Then je formát orientovaný na scénáře, protože popisuje scénář, který má být ověřen. \n"
            "[gold1](b) Je správně.[/gold1] [white bold]Jedná se o formát Given/When/Then, který je orientován na scénáře.[/white bold]\n"
            "(c) Není správně. Neexistuje žádný formát akceptačních kritérií orientovaný na produkt.\n"
            "d) Není správně. Neexistuje žádný formát akceptačních kritérií orientovaný na proces.\n"
        ),
    },
    {
        "id": 29,
        "text": (
            "Váš tým analyzuje následující uživatelský scénář s cílem definovat [white]akceptační kritéria:[/white] \n\n"
            "JAKO registrovaný zákazník CHCI mít možnost prohlížet si své předchozí objednávky na webových stránkách společnosti, ABYCH měl přehled o svých nákupech.\n\n"
            "Který z následujících testovacích případů [red]NENÍ[/red] pro tento uživatelský scénář relevantní?\n"
        ),
        "options": {
            "a": "Vstup: zákazník se přihlásí ke svému účtu na webových stránkách a klikne na tlačítko 'Zobrazit historii objednávek'. Očekávaný výsledek: systém zobrazí seznam všech předchozích objednávek zákazníka včetně data, čísla objednávky a celkové ceny.",
            "b": "Vstup: zákazník klikne na objednávku ze seznamu objednávek. Očekávaný výsledek: systém zobrazí jednotlivé nakoupené položky, jejich ceny a množství.",
            "c": "Vstup: zákazník klikne na tlačítko 'Seřadit vzestupně' na stránce historie objednávek. Očekávaný výsledek: systém zobrazí historii objednávek seřazenou vzestupně podle čísla objednávky.",
            "d": "Vstup: neregistrovaný zákazník se zaregistruje jako nový zákazník s platnou e-mailovou adresou, která ještě neexistuje v databázi zákazníků. Očekávaný výsledek: systém přijme registraci a vytvoří účet.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Testovací případ souvisí se zobrazením předchozích objednávek v historii objednávek.\n"
            "(b) Není správně. Testovací případ souvisí se zobrazením jednotlivých položek v objednávce.\n"
            "(c)  Není správně. Testovací případ souvisí se zobrazením předchozích objednávek v historii objednávek.\n"
            "[gold1](d) Je správně.[/gold1] [white bold]Testovací případ souvisí s procesem registrace, který ale není v tomto uživatelském scénáři popisován (tento uživatelský scénář popisuje zobrazení předchozích objednávek).[/white bold]\n"
        ),
    },
    {
        "id": 30,
        "text": (
            "Váš tým postupuje podle procesu, který používá DevOps pipeline. První tři kroky tohoto procesu jsou:\n\n"
            "(1) Vývoj kódu.\n"
            "(2) Odeslání kódu do systému pro správu verzí a jeho sloučení (merge) do větve `Test`.\n"
            "(3) Provedení testování komponent pro odeslaný kód.\n\n"
            "Která z následujících možností je [green]NEJVHODNĚJŠÍ[/green] jako vstupní kritérium pro krok (2) této pipeline?\n"
        ),
        "options": {
            "a": "Statická analýza odeslaného kódu nevrací žádná varování s vysokou závažností.",
            "b": "Systém pro správu verzí nehlásí žádné konflikty při sloučení kódu do větve `Test`",
            "c": "Testy komponent jsou sestaveny (zkompilovány) a připraveny ke spuštění.",
            "d": "Pokrytí příkazů je minimálně 80 %.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1] [white bold]To je něco, co může (a mělo by) být zkontrolováno před odesláním kódu do repozitáře.[/white bold]\n"
            "(b) Není správně. To je něco, co lze zkontrolovat po provedení kroku (2), protože hlášení konfliktů při sloučení lze provést po odeslání a sloučení kódu.\n"
            "(c) Není správně. To se lépe hodí jako vstupní kritérium pro krok (3).\n"
            "(d) Není správně. To se lépe hodí jako vstupní kritérium pro krok (3).\n"
        ),
    },
    {
        "id": 31,
        "text": (
            "Chcete odhadnout pracnost potřebnou pro testování nového projektu pomocí odhadu založeného\n"
            "na poměrech. Hodnotu poměru pracnosti vývoje a testování vypočítáte na základě\n"
            "zprůměrovaných dat ze čtyř již realizovaných projektů podobných novému projektu. Tato historická\n"
            "data jsou uvedena v následující tabulce:\n"
            "[white on black] ┌───────────┬─────────────────┬────────────────────┐ [/white on black]\n"
            "[white on black] │ Projekt   │ Pracnost vývoje │ Pracnost testování │ [/white on black]\n"
            "[white on black] │           │      [KČ]       │       [KČ]         │ [/white on black]\n"
            "[white on black] ├───────────┼─────────────────┼────────────────────┤ [/white on black]\n"
            "[white on black] │ Projekt 1 │     800 000     │      40 000        │ [/white on black]\n"
            "[white on black] │ Projekt 2 │   1 200 000     │     130 000        │ [/white on black]\n"
            "[white on black] │ Projekt 3 │     600 000     │      70 000        │ [/white on black]\n"
            "[white on black] │ Projekt 4 │   1 000 000     │     120 000        │ [/white on black]\n"
            "[white on black] └───────────┴─────────────────┴────────────────────┘ [/white on black]\n\n"
            "Odhadované náklady (pracnost) na vývoj nového projektu jsou 800 000 Kč. Jaký je váš odhad\n"
            "pracnosti testování v tomto projektu?\n"
        ),
        "options": {
            "a": "40 000 Kč",
            "b": "80 000 Kč",
            "c": "81 250 Kč",
            "d": "82 500 Kč",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "Průměrná pracnost vývoje je [white on black] 900 000 Kč [/white on black] a průměrná pracnost testování je [white on black] 90 000 Kč [/white on black] (počítáno ze čtyř projektů).\n"
            "Průměrný poměr pracnosti mezi testováním a vývojem je 1:10 (90 000Kč : 900 000 Kč), což znamená, že historicky tvoří testování v průměru [white on black]10 % pracnosti vývoje.[/white on black]\n"
            "Pokud se tedy pracnost vývoje odhaduje na [white]800 000 Kč[/white], pracnost testování se odhaduje takto:\n"
            "[white on black] 10% * 800 000 Kč = 0,1 * 800 000 Kč = 80 000 Kč. [/white on black]\n\n"
            "Tedy:\n"
            "(a) Není správně.\n"
            "[gold1](b) Je správně.[/gold1]\n"
            "(c) Není správně.\n"
            "(d) Není správně."
        ),
    },
    {
        "id": 32,
        "text": (
            "Testujete webovou aplikaci, která uživatelům umožňuje [white]VYHLEDAT[/white] produkty, [white]ZOBRAZIT[/white]\n"
            "podrobnosti o produktech, [white]PŘIDAT[/white] produkty do nákupního košíku a [white]VYTVOŘIT[/white] objednávku. \n\n"
            "Připravili jste následujících sedm testovacích případů (TC), které chcete všechny provést. Testy by měly být spouštěny v optimálním pořadí na základě jejich priority [bold on black] (1 = nejvyšší priorita): [/bold on black]\n\n"
            "[white on black] ┌─────┬──────────────────────────────────────┬────────────┐ [/white on black]\n"
            "[white on black] │ TCs │ Test                                 │  Priorita  │ [/white on black]\n"
            "[white on black] ├─────┼──────────────────────────────────────┼────────────┤ [/white on black]\n"
            "[white on black] │ TC1 │ VYHLEDAT produkt A                   │     4      │ [/white on black]\n"
            "[white on black] ├─────┼──────────────────────────────────────┼────────────┤ [/white on black]\n"
            "[white on black] │ TC2 │ VYHLEDAT produkt B                   │     4      │ [/white on black]\n"
            "[white on black] ├─────┼──────────────────────────────────────┼────────────┤ [/white on black]\n"
            "[white on black] │ TC3 │ ZOBRAZIT podrobnosti o produktu A    │     3      │ [/white on black]\n"
            "[white on black] ├─────┼──────────────────────────────────────┼────────────┤ [/white on black]\n"
            "[white on black] │ TC4 │ ZOBRAZIT podrobnosti o produktu B    │     2      │ [/white on black]\n"
            "[white on black] ├─────┼──────────────────────────────────────┼────────────┤ [/white on black]\n"
            "[white on black] │ TC5 │ PŘIDAT produkt A do nákupního košíku │     3      │ [/white on black]\n"
            "[white on black] ├─────┼──────────────────────────────────────┼────────────┤ [/white on black]\n"
            "[white on black] │ TC6 │ PŘIDAT produkt B do nákupního košíku │     1      │ [/white on black]\n"
            "[white on black] ├─────┼──────────────────────────────────────┼────────────┤ [/white on black]\n"
            "[white on black] │ TC7 │ VYTVOŘIT objednávku                  │     5      │ [/white on black]\n"
            "[white on black] └─────┴──────────────────────────────────────┴────────────┘ [/white on black]\n\n"
            "Identifikovali jste také následující logické závislosti mezi testovacími případy:\n"
            "• [white] Funkcionalita VYHLEDAT [/white] musí být otestována před funkcionalitou [white] ZOBRAZIT [/white].\n"
            "• [white] Funkcionalita ZOBRAZIT [/white] musí být otestována před funkcionalitou [white] PŘIDAT [/white].\n"
            "• [white] Funkcionalita PŘIDAT [/white] musí být otestována před funkcionalitou [white] VYTVOŘIT objednávku [/white].\n\n"
            "Který testovací případ by měl být proveden jako čtvrtý?\n"
        ),
        "options": {
            "a": "TC3",
            "b": "TC1",
            "c": "TC7",
            "d": "TC2",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "Podle závislostí musí být nejprve provedeny testy [white] VYHLEDAT,ZOBRAZIT a PŘIDAT [/white], a to před provedením [white] VYTVOŘIT [/white]. Předspuštěním [white] VYTVOŘIT [/white] je možné přidat více produktů (použitím stejného postupu).\n\n"
            "Na základě toho musí být [white] TC1 [/white] nebo [white] TC2 [/white] proveden jako první. Prvními testy by měly být ZOBRAZIT a PŘIDAT produkt B, protože jeho testovací případy (TC6, TC4) mají přiřazenou vyšší prioritu. První 3 testy k provedení jsou tedy [white] TC2 -> TC4 -> TC6 [/white].\n"
            "Nyní musíme zvážit, zda spustit [white] TC7 [/white] a poté celý průběh pro produkt A, nebo nejprve spustit všechny testy pro produkt A. Pokud má [white] TC7 [/white] nižší prioritu než ostatní testy, měly  by být tyto testy provedeny jako první. Proto by celý postup měl být:\n"
            "[white] TC2 -> TC4 -> TC6 -> TC1 -> TC3 -> TC5 -> TC7. [/white].\n\n"
            "(a) Není správně. TC1 musí být proveden před TC3.\n"
            "[gold1](b) Je správně.[/gold1]\n"
            "(c) Není správně. Jak je uvedeno výše, TC7 je v provedení testů poslední.\n"
            "(d) Není správně. Produkt B musí být proveden před produktem A.\n"
        ),
    },
    {
        "id": 33,
        "text": (
            "Která z následujících možností spadá podle modelu testovacích kvadrantů do kvadrantu [white] Q1  (tj.zaměřené na technologii a podporující tým)?[/white]\n"
        ),
        "options": {
            "a": "Testování použitelnosti.",
            "b": "Funkcionální testování",
            "c": "Uživatelské akceptační testování.",
            "d": "Integrační testování komponent.",
        },
        "correct": ["d"],
        "points": 1,
        "explanation": (
            "(a) Není správně. Testování použitelnosti je testování zaměřené na byznys a kritiku produktu (Q3).\n"
            "(b) Není správně. Funkcionální testování je testování zaměřené na byznys a podporující tým (Q2).\n"
            "(c) Není správně. Uživatelské akceptační testování je testování zaměřené na byznys a kritiku produktu (Q3).\n"
            "[gold1](d) Je správně.[/gold1] [white bold]Integrační testování komponent je testování zaměřené na technologii, které podporuje tým (vede vývoj) (Q1).[/white bold]\n"
        ),
    },
    {
        "id": 34,
        "text": (
            "Uvažujme následující rizika:\n"
            "1. Neefektivní implementace smyčky způsobuje dlouhé odezvy systému.\n"
            "2. Spotřebitelé mění své preference.\n"
            "3. Vytopení serverovny.\n"
            "4. Pacienti nad určitý věk dostávají nepřesné reporty.\n\n"
            "Dále uvažujme následující opatření ke zmírnění:\n"
            "A. Akceptace rizika.\n"
            "B. Testování výkonnostní efektivity (výkonnosti).\n"
            "C. Použití analýzy hraničních hodnot.\n"
            "D. Přenos rizika.\n\n"
            "Která z následujících kombinací [green1]NEJLÉPE[/green1] přiřazuje rizika k opatřením?\n"
        ),
        "options": {
            "a": "1C 2D 3A 4B",
            "b": "1B 2D 3A 4C",
            "c": "1B 2A 3D 4C",
            "d": "1C 2A 3D 4B",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "S ohledem na každé z uvedených rizik a opatření k jejich zmírnění platí,že:\n"
            "1. Dlouhé odezvy systému (1) lze testovat při testování výkonnostní efektivity (výkonnosti) (B).\n"
            "2. Změny preferencí spotřebitelů (2) jsou obvykle mimo naši kontrolu, proto je toto riziko obvykle akceptováno (A).\n"
            "3. Vytopení serverovny (3) může způsobit značné ztráty, proto by mělo dojít k přenosu (transferu) rizika, např. sjednáním pojistky (D).\n"
            "4. To, že pacienti nad určitý věk dostávají nepřesné reporty (4), naznačuje potenciální hraniční problém, který lze účinně detekovat technikami, jako je analýza hraničních hodnot (C).\n"
            "Tedy:\n"
            "(a) Není správně.\n"
            "(b) Není správně.\n"
            "[gold1](c) Je správně.[/gold1] [white bold]Správné kombinace rizik a opatření k jejich zmírnění jsou: 1B, 2A, 3D a 4C.[/white bold]\n"
            "(d) Není správně.\n"
        ),
    },
    {
        "id": 35,
        "text": (
            "Která z následujících možností je metrikou týkající se kvality produktu?\n"
        ),
        "options": {
            "a": "Střední doba do poruchy (MTTF).",
            "b": "Počet nalezených defektů.",
            "c": "Pokrytí požadavků.",
            "d": "Procento zjištěných defektů (DDP).",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1] [white bold]Metriky týkající se kvality produktu měří charakteristiky kvality. Střední doba do poruchy (MTTF) měří vyspělost, takže se jedná o metriku týkající se kvality produktu.[/white bold]\n"
            "b) Není správně. Toto je příklad metriky týkající se defektů, nikoli metriky týkající se kvality produktu.\n"
            "c) Není správně. Toto je příklad metriky pokrytí, nikoli metriky týkající se kvality produktu.\n"
            "d) Není správně. Toto je příklad metriky týkající se defektů, nikoli metriky týkající se kvality produktu.\n"
        ),
    },
    {
        "id": 36,
        "text": (
            "Jste členem testovacího týmu se sídlem v Severní Americe, který vyvíjí produkt pro klienta v Evropě. Tým je agilní, používá DevOps a používá CI/CD pipeline (průběžná integrace / průběžné doručování).\n\n"
            "Která z následujících možností je [orange1]NEJMÉNĚ[/orange1] efektivní způsob, jak sdílet zákazníkovi postup prací při testování?\n"
        ),
        "options": {
            "a": "Osobně tváří v tvář (face-to-face).",
            "b": "Pomocí ukazatelů (dashboardů).",
            "c": "E-mailem.",
            "d": "Ústně pomocí videokonference.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1] [white bold]Klient se nachází na jiném místě a v jiném časovém pásmu, takže může být obtížné komunikovat osobně (tváří v tvář).[/white bold]\n"
            "(b) Není správně. Dashboardy jsou obvykle dostupné kterémukoli uživateli kdykoli, takže rozdíl v časových pásmech není takovou překážkou v komunikaci jako verbální osobní komunikace\n"
            "(c) Není správně. Přestože je mezi Evropou a Amerikou několikahodinový časový posun, což může působit jisté komplikace, rozhodně to není tak velká překážka jako je pro osobní komunikaci.\n"
            "(d) Není správně. Videokonferenční nástroje jsou vhodným komunikačním prostředkem. Ačkoli komunikace mezi Evropou a Amerikou v pracovní době obvykle vyžaduje, aby se jedna strana připojila ve velmi časných nebo velmi pozdních hodinách, není tak velkou překážkou jako je pro osobní komunikaci.\n"
        ),
    },
    {
        "id": 37,
        "text": (
            "Které z následujících tvrzení [green1]NEJLÉPE[/green1] popisuje příklad toho, jak konfigurační management (CM) podporuje testování?\n"
        ),
        "options": {
            "a": "S číslem verze prostředí může CM nástroj zjistit čísla verzí knihoven, stubů a ovladačů používaných v tomto prostředí.",
            "b": "Díky záznamu hodnot vstupů může CM nástroj provádět testovací případy pro tyto konfigurace a vypočítat pokrytí.",
            "c": "S informací o datu zakoupení licence softwaru CM nástroj automaticky poskytne informaci o tom, že platnost licence bude končit.",
            "d": "S číslem verze testovacího případu může CM nástroj automaticky vytvořit testovací data pro tento testovací případ.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1] [white bold]V případě komplexní konfigurační položky (např. testovací prostředí) lze v rámci CM zaznamenávat dílčí položky, ze kterých se tato komplexní položka skládá, jejich vztahy a verze.[/white bold]\n"
            "(b) Není správně. Nástroje CM neprovádějí testovací případy a nepočítají pokrytí.\n"
            "(c) Není správně. Nástroj CM není nástroj pro management licencí.\n"
            "(d) Není správně. CM nástroje negenerují testovací data.\n"
        ),
    },
    {
        "id": 38,
        "text": (
            "Testujete funkci [white bold]SORT[/white bold], která na přijímá na vstupu sadu čísel a vrací ji na výstupu vzestupněseřazenou. Protokol z provedení testu vypadá následovně:\n\n"
            "Konfigurace prostředí: funkce SORT, sestavení 2.002.2182, sada testovacích případů (TCS): TCS3, počet testovacích případů (TC): 5\n"
            "ID běhu testu: 736\n"
            "Start 12:43:21.003\n\n"
            "[white on black] ┌──────────────┬────────────────┬───────────────────────┬───────────────────────┬──────────────────┐ [/white on black]\n"
            "[white on black] │ 12:43:21.003 │ Provedeni TC1  │ vstup: 3              │ Výstup:3              │ Výsledek: [green]prošel[/green] │ [/white on black]\n"
            "[white on black] ├──────────────┼────────────────┼───────────────────────┤───────────────────────┤──────────────────┤ [/white on black]\n"
            "[white on black] │ 12:43:21.003 │ Provedeni TC2  │ Vstup: 3 11 6 5       │ Výstup: 3 5 6 11      │ Výsledek: [green]prošel[/green] │ [/white on black]\n"
            "[white on black] ├──────────────┼────────────────┼───────────────────────┤───────────────────────┤──────────────────┤ [/white on black]\n"
            "[white on black] │ 12:43:21.004 │ Provedeni TC3  │ Vstup: 8 7 3 7 1      │ Výstup: 1 3 7 8       │ Výsledek: [red1]selhal[/red1] │ [/white on black]\n"
            "[white on black] ├──────────────┼────────────────┼───────────────────────┤───────────────────────┤──────────────────┤ [/white on black]\n"
            "[white on black] │ 12:43:21.005 │ Provedeni TC4  │ Vstup: -2 -2 -2 -3 -3 │ Výstup: -3 -2         │ Výsledek: [red1]selhal[/red1] │ [/white on black]\n"
            "[white on black] ├──────────────┼────────────────┼───────────────────────┤───────────────────────┤──────────────────┤ [/white on black]\n"
            "[white on black] │ 12:43:21.005 │ Provedeni TC5  │ Vstup: 0 -2 0 3 4 4   │ Výstup: -2 0 3 4      │ Výsledek: [red1]selhal[/red1] │ [/white on black]\n"
            "[white on black] └──────────────┴────────────────────────────────────────┴───────────────────────┴──────────────────┘ [/white on black]\n"
            "Konec 12:43:21.005\n"
            "Celková doba testovacího cyklu: 0:00:00.002\n\n"
            "Která z následujících možností poskytuje NEJLEPŠÍ popis selhání, který lze použít v reportu o defektu?\n"
        ),
        "options": {
            "a": "Systém nedokáže seřadit několik sad čísel. Odkaz na testovací případy: TC3, TC4, TC5",
            "b": "Zdá se, že systém při řazení ignoruje duplicitní vstupy. Odkaz na testovací případy: TC3, TC4, TC5.",
            "c": "Systém nedokáže seřadit záporná čísla. Odkaz na testovací případy: TC4, TC5.",
            "d": "TC3, TC4 a TC5 mají defekty (duplicitní vstupní data) a měly by být opraveny.",
        },
        "correct": ["b"],
        "points": 1,
        "explanation": (
            "(a) Není správně. I když je tato věta pravdivá, neposkytuje vývojářům velkou hodnotu.\n"
            "[gold1](b) Je správně.[/gold1] [white bold]Z výsledků testů se zdá, že systém ignoruje duplicity a řadí seznam bez ohledu na opakování, což je pravděpodobně příčina selhání v TC3, TC4, TC5. Tyto informace mohou vývojáři pomoci při nalezení a opravě defektu.[/white bold]\n"
            "(c) Není správně. Systém nevykazuje selhání při řazení záporných čísel. Problém je spíše v tom, že se neberou v potaz duplicity.\n"
            "(d) Není správně. Testovací případy TC3, TC4 a TC5 selžou, ale neexistuje žádná informace o tom, že by testovací případy měly nějaké defekty.\n"
        ),
    },
    {
        "id": 39,
        "text": (
            "Předpokládejme následující charakteristiky testovacích nástrojů:\n"
            "1. Podpora sledování pracovních postupů (workflows).\n"
            "2. Usnadnění komunikace.\n"
            "3. Virtuální počítač.\n"
            "4. Podpora revidujících.\n\n"
            "A jejich následující kategorie:\n"
            "A. Nástroj pro statické testování.\n"
            "B. Nástroje podporující škálovatelnost a standardizaci nasazení.\n"
            "C. Nástroje DevOps.\n"
            "D. Nástroje pro spolupráci. \n\n"
            "Která z následujících možností [green]NEJLÉPE[/green] přiřazuje kategorie nástrojů k jejich charakteristikám?\n"
        ),
        "options": {
            "a": "1A, 2B, 3C, 4D",
            "b": "1B, 2D, 3C, 4A",
            "c": "1C, 2D, 3B, 4A",
            "d": "1D, 2C, 3A, 4B",
        },
        "correct": ["c"],
        "points": 1,
        "explanation": (
            "S ohledem na každou z uvedených kategorií nástrojů a jejich popisy platí, že:\n"
            "A. Nástroje pro statické testování - poskytují podporu při\n"
            "provádění revizí a statické analýzy (4).\n"
            "B. Nástroje podporující škálovatelnost a standardizaci nasazení, např. virtuální počítače, nástroje pro práci s kontejnery (3).\n"
            "C. Nástroje DevOps - podpora DevOps pipelines, sledování pracovních postupů, automatizovaný proces sestavování (build process), průběžná integrace/průběžné dodávání (CI/CD) (1).\n"
            "D. Nástroje pro spolupráci - usnadňují komunikaci (2).\n\n"
            "Tedy:\n"
            "(a) Není správně.\n"
            "(b) Není správně.\n"
            "[gold1](c) Je správně.[/gold1] [white bold]Je správně. Správná kombinace je: 1C, 2D, 3B, 4A.[/white bold]\n"
            "(d) Není správně.\n"
        ),
    },
    {
        "id": 40,
        "text": (
            "Která z následujících možností bude s [green]NEJVĚTŠÍ[/green] pravděpodobností přínosem automatizace testů?\n"
        ),
        "options": {
            "a": "Poskytuje metriky pokrytí, které jsou pro člověka příliš komplikované na to, aby je bylo možné ručně vypočítat.",
            "b": "Přenáší část zodpovědnosti za testování na dodavatele nástroje.",
            "c": "Odstraňuje potřebu kritického myšlení při analýze výsledků testů.",
            "d": "Generuje testovací případy z analýzy programového kódu.",
        },
        "correct": ["a"],
        "points": 1,
        "explanation": (
            "[gold1](a) Je správně.[/gold1] [white bold]Automatizace testování může poskytovat metriky, které jsou příliš komplikované pro manuální výpočet, např. míry pokrytí testů bílé skříňky (pro jakýkoliv komplexnější kód).[/white bold]\n"
            "(b) Není správně. Při použití testovacích nástrojů odpovídá za testování tester a tato odpovědnost NENÍ sdílena s dodavatelem nástroje, protože dodavatel se na testování nepodílí. Jedinou možnou odpovědností, která by mohla být přiřazena dodavateli nástroje, je situace, kdy nástroj nefunguje podle očekávání a poskytuje nesprávné výsledky testů.\n"
            "(c) Není správně. Testeři stále musí při analýze anomálií ve výsledcích testů aplikovat kritické myšlení, aby určili jejich pravděpodobnou příčinu.\n"
            "(d) Není správně. Testeři ani nástroje nemohou generovat testovací případy jednoduše z analýzy programového kódu, protože kód je implementací a neposkytuje žádné informace o očekávaných výsledcích. Ty budou muset pocházet z jiné části testovací báze, jako je např. specifikace návrhu.\n"
        ),
    },
]
