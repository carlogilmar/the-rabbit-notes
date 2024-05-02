# Crime Scene Book

## Git 

Show all the files changes by lines added/removed in a git project.
> git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames > git_log.txt

```
--a6466da7c--2024-05-01--Ben Munat
--7a01abe98--2024-05-01--Ben Munat
5	0	apps/site_web/lib/site_web/plugs/cart_plug.ex
7	0	apps/site_web/lib/site_web/plugs/global_context_plug.ex
8	0	apps/site_web/lib/site_web/templates/controller.ex

--8107db5ed--2024-05-01--Fernando Rovitto
--4fdf9c145--2024-05-01--Fernando Rovitto
2	2	apps/foundation/test/foundation/platform/platform_test.exs
```

## Code Maat

1. Install a JDK and Lein project to run clojure apps.
2. Install the project locally: https://github.com/adamtornhill/code-maat
3. Run the project with your git data:

> java -jar code-maat-1.0.5-SNAPSHOT-standalone.jar -l /Users/carlogilmar/Code/ESL/estee_lauder/bifrost/git_log.txt -c git2 -a summary

Output:
```
statistic,value
number-of-commits,8054
number-of-entities,5272
number-of-entities-changed,28975
number-of-authors,107
```
