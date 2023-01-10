## Hammer Elixir

1. Concepts: `Limit` (limit of operations) and `scale_ms` (timespan in milliseconds). Hammer uses a Token Bucket algorithm.
2. Dependencies:

```elixir
def deps do
  [{:hammer_backend_redis, "~> 6.1"},
   {:hammer, "~> 6.0"}]
end
```

3. Installation in `config/config.exs`:

``` elixir
config :hammer,
  backend: {Hammer.Backend.ETS,
            [expiry_ms: 60_000 * 60 * 4,
             cleanup_interval_ms: 60_000 * 10]}
```

4. Hammer API

```elixir
check_rate(id::string, scale_ms::integer, limit::integer)
check_rate_inc(id::string, scale_ms::integer, limit::integer, increment::integer)
inspect_bucket(id::string, scale_ms::integer, limit::integer)
delete_buckets(id::string)
make_rate_checker(id_prefix, scale_ms, limit)
```

## Hammer Plug

1. Installation

```elixir
def deps do
  [
    {:hammer, "~> 6.0"},
    {:hammer_plug, "~> 3.0"}
  ]
end
```

2. Implementation in plug

```elixir
# Allow ten uploads per 60 seconds
plug Hammer.Plug, [
  rate_limit: {"video:upload", 60_000, 10},
  by: {:session, :user_id}
] when action == :upload_video_file

def upload_video_file(conn, _opts) do
  # ...
end
```
