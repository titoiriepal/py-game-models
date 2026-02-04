import json

# import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for nickname, data in players.items():
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )
        for sk in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=sk["name"],
                defaults={"bonus": sk["bonus"], "race":race}
            )

        guild = None
        guild_data = data.get("guild")
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )

if __name__ == "__main__":
    main()
