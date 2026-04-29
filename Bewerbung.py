"""
Bewerbung als Charakterbogen - Patrick Carillo

Eine kreative Variante eines Anschreibens für das Praktikum
Softwareentwicklung C#/.NET bei der Lorent IT-Lösungen GmbH.
Inspiriert von Dungeons & Dragons sind Charakter, Quest und Würfelproben
als Metapher für Bewerber, Stelle und Eignung dargestellt.

Hinweis: Die "Praktikumseignung" mit Würfelproben ist humorvoll
gemeint und nicht als ernsthafte Selbstbewertung zu verstehen –
über meine tatsächliche Eignung freue ich mich, in einem Gespräch
zu sprechen.
"""

import random


class Colours:
    """ Farbcodes für Terminal-Ausgabe """
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"


class Bewerber:
    """ Repräsentiert einen Bewerber als D&D-inspirierten Charakter. """

    def __init__(self,
                 name: str,
                 char_class: str,
                 level: int,
                 stats: dict[str, int],
                 proficiencies: list[str],
                 inventory: list[str],
                 backstory: str,
                 quest: str
                ) -> None:
        self.name = name
        self.char_class = char_class
        self.level = level
        self.stats = stats
        self.proficiencies = proficiencies
        self.inventory = inventory
        self.backstory = backstory
        self.quest = quest

    def skill_check(self, stat: str, dc: int) -> bool:
        """
        Führt einen Würfelwurf gegen eine Schwierigkeit (DC) durch.

        Wirft einen 20-seitigen Würfel und addiert den Wert des angegebenen Attributs.
        Liegt das Ergebnis bei oder über dem DC, gilt der Check als bestanden.

        Args:
            stat:   Wert des im Charakterbogen angegebenen Attributs
            dc:     Schwierigkeitswert definiert durch d. Liste checks in Methode run_application_checks()
        Returns:
            True bei Erfolg, sonst False
        """

        roll = random.randint(1, 20)
        # In D&D ist d. Modifier eine Addition zum Würfelwurf abhängig v. Charakterwert
        stat_value = self.stats.get(stat, 10)
        modifier = (stat_value - 10) // 2
        total = roll + modifier
        success = total >= dc

        colour = Colours.GREEN if success else Colours.RED
        result = "✓ Erfolg" if success else "✗ Fehlschlag"

        print(f"  {Colours.BOLD}{stat}-Check (DC {dc}):{Colours.RESET}")
        print(f"    Wurf: {roll} + Modifikator {modifier} = {total}")
        print(f"    Ergebnis: {colour}{result}{Colours.RESET}\n")
        return success

    def run_application_checks(self) -> None:
        """ Führt die für die Bewerbung relevanten Skill-Checks durch. """

        print(f"{Colours.BOLD}{Colours.CYAN}=== Praktikumseignung ==={Colours.RESET}\n")

        # Die DC-Werte sind bewusst moderat gewählt, sie sollen Eigenschaften
        # widerspiegeln, die laut Stellenausschreibung wichtig sind.
        checks = [
            ("Lernbereitschaft", 15),
            ("Motivation", 15),
            ("Technik-Begeisterung", 10),
            ("Kommunikation", 15),
        ]
        # sum() über bool-Werte zählt, wie viele Checks True zurückgegeben haben
        erfolge = sum(self.skill_check(stat, dc) for stat, dc in checks)

        print(f"Bestandene Checks: {Colours.BOLD}{erfolge} von {len(checks)}{Colours.RESET}")
        if erfolge == len(checks):
            print("→ Der Praktikumsplatz ist verdient.")
        elif erfolge >= len(checks) // 2:
            print("→ Ein Gespräch wäre die beste Gelegenheit, den Rest zu beweisen.")
        else:
            print("→ Die Würfel waren heute nicht günstig – aber Patrick gibt nicht auf und "
                  "wird weiter an sich arbeiten.")  # An einem Gespräch wäre ich trotzdem noch sehr interessiert.


    def print_character_sheet(self):
        """ Gibt den vollständigen Charakterbogen formatiert aus. """

        print(f"{Colours.BOLD}{Colours.CYAN}=== Charakterbogen ==={Colours.RESET}")
        print(f"Name: {self.name}")
        print(f"Klasse: {self.char_class} (Stufe {self.level})\n")

        # Tabellarische Ausrichtung mit Punkten als Füllzeichen (wie in einem Char-Bogen)
        print(f"{Colours.BOLD}Attribute{Colours.RESET}")
        for stat, value in self.stats.items():
            print(f"{stat:.<25} {value}")
        print()

        print(f"{Colours.BOLD}Fertigkeiten:{Colours.RESET} {', '.join(self.proficiencies)}\n")

        print(f"{Colours.BOLD}Inventar{Colours.RESET}")
        for item in self.inventory:
            print(f"- {item}")
        print()

        print(f"{Colours.BOLD}Hintergrund:{Colours.RESET}\n {self.backstory}\n")
        print(f"{Colours.BOLD}Aktuelle Quest:{Colours.RESET}\n {self.quest}\n")


def main() -> None:
    pc = Bewerber(
        name="Patrick Carillo",
        char_class="Apprentice Software Developer",
        level=1,
        stats={
            "Lernbereitschaft": 17,
            "Motivation": 14,
            "Technik-Begeisterung": 14,
            "Kommunikation": 16,
            "Schlafbedarf": 6   # niedrig dank Sohnemann :)
        },
        proficiencies=["Python", "Lua", "Git", "SQL", "HTML"],
        inventory=[
            "Mechanische Tastatur +1",  # Silent Switches
            "Cheat-Sheet der Pythonbefehle",
            "Trank der säurigen Kohlenwasser"
        ],
        backstory=(
            "Patrick begann seine Reise in einem Studium der 3D-Animation mit\n "
            "dem Fokus auf Game Development. Dieser Weg war ein Resultat von\n "
            "früher Begegnung von Technologie (C64, Win 95 & Suse Linux waren die\n "
            "ersten Betriebssysteme), Informatiklehrer (brachte ihm Scratch, HTML & Java\n "
            "näher) und eine Affinität zu Videospielen sowie einem Bedürfnis zum kreativem Output.\n "
            "Während des Studiums fand Patrick schnell Gefallen an der Rolle des Technical Artists,\n "
            "eine Verbindungsrolle von Programmierern und Art, dadurch kamen auch die anfänglichen\n "
            "Begegnungen mit Skriptsprachen wie LUA und generell relevante Programmiersprachen.\n\n "
            "Das Studium sowie eine gleichzeitig erfolgte Arbeit in einem neu gegründeten\n "
            "Entwicklerstudio wurden aufgrund familiärer Umstände aufgegeben und er bereitete\n "
            "sich mithilfe eines BWL-Studiums auf eine kaufmännische Karriere im Familien-Unternehmen vor.\n "
            "Während der Universitäts-Zeit befasste er sich nebenbei mit d. Aktienmarkt und fing an,\n "
            "aktiv mit diesen zu handeln.\n\n "
            "Wegen der wirtschaftlichen Lage seit 2018 und der Corona-Pandemie wurde die Arbeit\n "
            "im Unternehmen beendet. Die Jahre 2020 bis 2022 waren geprägt von einer Orientierungs-\n "
            "phase, die weltweit zu spüren war und zu einer Realisierung der Wichtigkeit von Familie\n "
            "und Beziehungen führte. Seine Partnerin und die Geburt seines Sohnes brachten ihn dazu,\n "
            "die Faszination seines ersten Studiums neu aufzugreifen und endlich umzusetzen. Den Anfang\n "
            "machte er mit einer Umschulung bei der BBQ. Diese Bewerbung ist der nächste Schritt."
        ),
        quest=(
            "Eine Anstellung als Praktikant bei der Lorent IT-Lösungen GmbH "
            "im Reich der C#/.NET-Entwicklung, von April bis Oktober 2027."
        )
    )

    pc.print_character_sheet()

    print(f"{Colours.BOLD}\nMöchten Sie die Eignung von Patrick per Würfelwurf feststellen?{Colours.RESET}")
    choice = input(f"Drücken Sie {Colours.BOLD}Ja(j){Colours.RESET} oder {Colours.BOLD}Nein(n):{Colours.RESET} ")
    if choice == "j" or "y":
        pc.run_application_checks()
        print()
        # Die beiden Outputs sind identisch, da ich wirklich dankbar bin, die Chance zu haben auch kreativ
        # eine Bewerbung gestalten zu können.
        print("Vielen Dank für Ihre Zeit! Ich hoffe, dieses kleine Projekt konnte Ihnen\n"
              "einen ersten Eindruck vermitteln. Persönlich würde ich Ihnen gerne zeigen\n"
              "wie viel Motivation und Neugierde dahintersteckt.\n"
              "Weitere Informationen befinden sich in der README-Datei.")
    else:
        print()
        print("Vielen Dank für Ihre Zeit! Ich hoffe, dieses kleine Projekt konnte Ihnen\n"
              "einen ersten Eindruck vermitteln. Persönlich würde ich Ihnen gerne zeigen\n"
              "wie viel Motivation und Neugierde dahintersteckt.\n"
              "Weitere Informationen befinden sich in der README-Datei.")


if __name__ == "__main__":
    main()