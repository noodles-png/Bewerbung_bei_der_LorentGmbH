class bewerber:
    def __init__(self,
                 name,
                 position,
                 company,
                 tech_stack,
                 duration
    ) -> None:
        self.name = name
        self.position = position
        self.company = company
        self.tech_stack = tech_stack
        self.duration = duration

def main() -> None:
    bewerbung = bewerber(
        name="Patrick Carillo",
        position="Praktikum Softwareentwicklung C#/.NET",
        company="Lorent IT-Lösungen GmbH",
        tech_stack=["Python", "LUA", "Git", "SQL", "HTML"], # TODO explain the level as mostly basic
        duration="April 2027 bis Oktober 2027"
    )

    print(f"Sehr geehrtes Team  der {bewerbung.company},\n")
    print(f"mein Name ist {bewerbung.name} und dies ist meine Bewerbung")
    print(f"auf die Stelle {bewerbung.position} im Zeitraum {bewerbung.duration}.")


if __name__ == "__main__":
    main()