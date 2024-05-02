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

# Code Maat
## Read git output to get a summarize

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

4. Create a revisions analysis

> java -jar code-maat-1.0.5-SNAPSHOT-standalone.jar -l /Users/carlogilmar/Code/ESL/estee_lauder/bifrost/git_log.txt -c git2 -a revisions > revisions.txt

```csv
entity,n-revs
apps/foundation/mix.exs,372
mix.lock,342
.github/workflows/ci.yml,325
apps/site_web/lib/site_web/router.ex,308
config/config.exs,260
apps/foundation/priv/cockroach/seeds.exs,212
apps/foundation/lib/foundation/commerce/checkouts/checkouts.ex,208
apps/foundation/lib/foundation/promotions/promotions.ex,192
config/test.exs,181
apps/foundation/lib/foundation/carts/carts.ex,178
apps/foundation/lib/foundation/orders/orders.ex,163
apps/foundation/test/foundation/commerce/checkouts/checkouts_test.exs,154
apps/foundation/lib/foundation/commerce/commerce.ex,151
apps/foundation/lib/foundation/checkouts/checkouts.ex,150
apps/foundation/test/foundation/commerce/commerce_test.exs,150
apps/foundation/test/foundation/promotions/promotions_test.exs,147
```

## Cloc

> cloc ./ --unix --by-file --csv --quiet --report-file=bifrost_complexity.csv

```
language,filename,blank,comment,code,"github.com/AlDanial/cloc v 2.00  T=8.98 s (271.8 files/s 44193.8 lines/s)"
Text,./git_log.txt,8053,0,39057
JavaScript,./apps/site_web/priv/static/assets/base.js,138,838,11353
CSV,./react_complexity.csv,0,0,7637
JavaScript,./apps/sidekick_web/priv/static/assets/app.js,8,296,6149
CSV,./revisions.csv,0,0,5273
HTML,./apps/foundation/cover/Elixir.Foundation.BenefitMock.html,6,0,4443
HTML,./apps/foundation/cover/Elixir.Foundation.Commerce.Taxes.Vertex.Mock.html,6,0,4443
HTML,./apps/foundation/cover/Elixir.Foundation.ConditionMock.html,6,0,4443
HTML,./apps/foundation/cover/Elixir.Foundation.Engine.Step.Mock.html,6,0,4443
HTML,./apps/foundation/cover/Elixir.Foundation.HTTP.Mock.html,6,0,4443
HTML,./apps/foundation/cover/Elixir.Foundation.Orders.Radial.Mock.html,6,0,4443
```

## Merge both CSV with python

```python
#!/usr/bin/env python3

# Merges two CSV documents.
##

import csv
import sys
import os


class MergeError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class Merged(object):
    def __init__(self):
        self._all_modules_with_complexity = {}
        self._merged = {}

    def sorted_result(self):
        # Sort on descending order:
        ordered = sorted(
            list(
                self._merged.items()), key=lambda item: int(
                item[1][0]), reverse=True)
        return ordered

    def extend_with(self, name, freqs):
        if name in self._all_modules_with_complexity:
            complexity = self._all_modules_with_complexity[name]
            self._merged[name] = freqs, complexity

    def record_detected(self, name, complexity):
        self._all_modules_with_complexity[name] = complexity


def skip_heading(f):
    next(f)


def read_heading_from(r):
    p = next(r)
    while p == []:
        p = next(r)
    return p


def validate_content_by(heading, expected):
    comparison = expected.split(',')
    stripped = heading[0:len(comparison)]  # allow extra fields
    if stripped != comparison:
        raise MergeError(
            'Erroneous content. Expected = ' +
            expected +
            ', got = ' +
            ','.join(heading))


def parse_csv(merged, filename, parse_action, expected_format):
    with open(filename, 'rt') as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        heading = read_heading_from(r)
        validate_content_by(heading, expected_format)
        for row in r:
            parse_action(merged, row)


def write_csv(stats):
    print('module,revisions,code')
    for s in stats:
        name, (f, c) = s
        print(name + ',' + f + ',' + c)


def as_os_aware_path(name):
    return os.path.normpath(name)


def parse_complexity(merged, row):
    name = as_os_aware_path(row[1])
    complexity = row[4]
    merged.record_detected(name, complexity)


def parse_freqs(merged, row):
    name = as_os_aware_path(row[0])
    freqs = row[1]
    merged.extend_with(name, freqs)


def merge(revs_file, comp_file):
    merged = Merged()
    parse_csv(merged, comp_file, parse_complexity,
              expected_format='language,filename,blank,comment,code')
    parse_csv(merged, revs_file, parse_freqs, expected_format='entity,n-revs')
    write_csv(merged.sorted_result())


if __name__ == '__main__':
    if len(sys.argv) != 3:
        msg = ('Wrong arguments. Require one CSV file with frequencies and one'
               ' with the complexity')
        raise MergeError(msg)
    revs_file = sys.argv[1]
    comp_file = sys.argv[2]
    merge(revs_file, comp_file)
```

Running this script:

>  python3 merge.py revisions.csv bifrost_complexity.csv > merge.csv

```
module,revisions,code
apps/foundation/mix.exs,372,174
.github/workflows/ci.yml,325,494
apps/site_web/lib/site_web/router.ex,308,216
config/config.exs,260,202
apps/foundation/priv/cockroach/seeds.exs,212,1542
apps/foundation/lib/foundation/commerce/checkouts/checkouts.ex,208,289
apps/foundation/lib/foundation/promotions/promotions.ex,192,281
config/test.exs,181,142
apps/foundation/test/foundation/commerce/checkouts/checkouts_test.exs,154,732
apps/foundation/lib/foundation/commerce/commerce.ex,151,263
apps/foundation/test/foundation/commerce/commerce_test.exs,150,1162
apps/foundation/test/foundation/promotions/promotions_test.exs,147,690
config/runtime.exs,140,160
apps/foundation/lib/foundation/storefront/storefront.ex,120,74
apps/site_web/lib/site_web/templates/templates.ex,118,269
apps/foundation/lib/foundation/commerce/messages/order_message.ex,117,253
apps/site_web/lib/site_web/controllers/checkout/payment_controller.ex,106,60
apps/foundation/lib/foundation/commerce/accounts/accounts.ex,103,423
apps/foundation/lib/foundation/commerce/orders/order.ex,102,195
```
