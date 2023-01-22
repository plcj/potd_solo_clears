# Build the Docker image
`docker build --tag ddlb .`

# Configuration
Example configuration is provided in `config.py`.

# Collect leaderboard data
Specify the dungeon you want data for in `config.py`.
`docker run --rm --mount type=bind,source=$(pwd),target=/root/ddlb ddlb scrapy runspider ./ddlb/spiders/deep_dungeon_leaderboard_spider.py -o ./database/out.json`

# Postprocessing
Specify the input path in `config.py`. This corresponds to the value passed to the `-o` option when running scrapy.
## Tabulate collected data
`docker run --rm --mount type=bind,source=$(pwd),target=/root/ddlb ddlb python3 -c "import postprocessing; postprocessing.json_to_csv()"`

Drop it in a spreadsheet, have fun.

## Print number of clears by job (not pretty)
`docker run --rm --mount type=bind,source=$(pwd),target=/root/ddlb ddlb python3 -c "import postprocessing as post; print(sorted(post.all_clears_by_job()))"`

# Run Unit Tests
`docker run --rm --mount type=bind,source=$(pwd),target=/root/ddlb ddlb pytest`
