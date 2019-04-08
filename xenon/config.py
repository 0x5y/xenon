from os import environ as env


token = env.get('TOKEN')
# shard_count and shard_ids can be overridden by Command Line Arguments
shard_count = None  # ~ guilds // 1000
shard_ids = None

prefix = "#!"

extensions = [
    "cogs.errors",
    "cogs.help",
    "cogs.admin",
    "cogs.backups",
    "cogs.templates",
    "cogs.users",
    "cogs.basics",
    "cogs.sharding",
    "cogs.stats"
]

support_guild = 410488579140354049
owner_id = 386861188891279362

dbl_token = env.get('DBL_TOKEN')
