class bewerber:
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


def main():
    pc = bewerber(
        name="Patrick Carillo",
        char_class="Apprentice Software Developer",
        level=1,
        stats={
            "Lernbereitschaft":       17,
            "Motivation":             14,
            "Technik-Begeisterung":   14,
            "Kommunikation":          16,
            "Schlafbedarf":           6
        },
        proficiencies=["Python", "Lua", "Git", "SQL", "HTML"],
        inventory=[
            "Mechanische Tastatur +1",
            "Cheat-Sheet der Pythonbefehle",
            "Trank der säurigen Kohlenwasser"
        ],
        backstory=(
            "Patrick begann seine Reise in einem Studium der 3D-Animation mit\n"
            " dem Fokus auf Game Development. Dieser Weg war ein Resultat von\n"
            " früher Begegnung von Technologie (C64, Win 95 & Suse Linux waren die\n"
            " ersten Betriebssysteme), Informatiklehrer (brachte ihm Scratch und HTML\n"
            " näher) und Affinität zu Videospielen sowie Bedürfnis zum kreativem Output."
        ),
        quest=(
            "Eine Anstellung als Praktikant bei der Lorent IT-Lösungen GmbH"
            "im Reich der C#/Net-Entwicklung, von April bis Oktober 2027."
        )
     )

    print(f"=== Charakterbogen ===")
    print(f"Name: {pc.name}")
    print(f"Klasse: {pc.char_class} (Stufe {pc.level})\n")

    print("Attribute")
    for stat, value in pc.stats.items():
        print(f"{stat:.<25} {value}")
    print()

    print(f"Fertigkeiten: {', '.join(pc.proficiencies)}\n")

    print("Inventar")
    for item in pc.inventory:
        print(f"- {item}")
    print()

    print(f"Hintergrund:\n {pc.backstory}\n")
    print(f"Aktuelle Quest:\n {pc.quest} ")

if __name__ == "__main__":
    main()

