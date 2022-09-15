# Build the Docker image
`docker build --tag potd_solo_clears .`

# Collect leaderboard data
`docker run --rm --mount type=bind,source=$(pwd),target=/root/psc potd_solo_clears scrapy runspider ./potd_solo_clears/spiders/potd_solo_leaderboard_spider.py -o ./database/out.json`

# Postprocessing
Specify the input path in `config.py`. This corresponds to the value passed to the `-o` option when running scrapy.
## Tabulate collected data
`docker run --rm --mount type=bind,source=$(pwd),target=/root/psc potd_solo_clears python3 -c "import postprocessing; postprocessing.json_to_csv()"`

Drop it in a spreadsheet, have fun.

## Print number of clears by job (not pretty)
`docker run --rm --mount type=bind,source=$(pwd),target=/root/psc potd_solo_clears python3 -c "import postprocessing as post; print(sorted(post.all_clears_by_job()))"`

# Run Unit Tests
`docker run --rm --mount type=bind,source=$(pwd),target=/root/psc potd_solo_clears pytest`
