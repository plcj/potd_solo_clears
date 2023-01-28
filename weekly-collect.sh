##!/bin/zsh

# Commands for "normal" collection
# Todo: wrap spider so cfg can be passed in with fire

# Set cfg to potd
docker run --rm --mount type=bind,source=$(pwd),target=/root/ddlb ddlb scrapy runspider ./ddlb/spiders/deep_dungeon_leaderboard_spider.py -o ./database/potd-230128.json
docker run --rm --mount type=bind,source=$(pwd),target=/root/ddlb ddlb python3 -c "import postprocessing; postprocessing.json_to_csv()"

# Set cfg to hoh
docker run --rm --mount type=bind,source=$(pwd),target=/root/ddlb ddlb scrapy runspider ./ddlb/spiders/deep_dungeon_leaderboard_spider.py -o ./database/hoh-230128.json
docker run --rm --mount type=bind,source=$(pwd),target=/root/ddlb ddlb python3 -c "import postprocessing; postprocessing.json_to_csv()"
