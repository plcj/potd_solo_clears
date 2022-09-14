# Build the Docker image
`docker build --tag potd_solo_clears .`

# Collect leaderboard data
`docker run --rm --mount type=bind,source=$(pwd),target=/root/psc potd_solo_clears scrapy runspider ./potd_solo_clears/spiders/leaderboard_spider.py -o out.json`

# Process collected data and print results
`docker run --rm --mount type=bind,source=$(pwd),target=/root/psc potd_solo_clears python3 postprocessing.py`

Specify the input path in `config.py`.

# Run Unit Tests
`docker run --rm --mount type=bind,source=$(pwd),target=/root/psc potd_solo_clears pytest`
