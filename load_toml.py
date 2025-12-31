import tomllib

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

print(config["model"]["sequence_length"])
print(config["aws"]["region"])
