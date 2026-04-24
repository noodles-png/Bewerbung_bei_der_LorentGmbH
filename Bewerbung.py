class bewerber:
    def __init__(self,
                 name,
                 position,
                 company,
                 tech_stack,
    ) -> None:
        self.name = name
        self.position = position
        self.company = company
        self.tech_stack = tech_stack

def main() -> None:
    bewerbung = bewerber(
        name="Patrick Carillo",
        position="Praktikum Softwareentwicklung C#/.NET",
        company="Lorent IT-Lösungen GmbH",
        tech_stack=["Python", "LUA", "Git", "SQL", "HTML"] # TODO explain the level as mostly basic
    )

    print(f"Lorem Ipsum")

if __name__ == "__main__":
    main()