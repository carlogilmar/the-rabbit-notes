# Mox

> Mox is a library for defining concurrent mocks in Elixir.

[Mox Dashbit by Jose Valim](https://dashbit.co/blog/mocks-and-explicit-contracts)

- No ad-hoc mocks. You can only create mocks based on behaviours
- No dynamic generation of modules during tests. Mocks are preferably defined in your test_helper.exs or in a setup_all block and not per test
- Concurrency support. Tests using the same mock can still use async: true
- Rely on pattern matching and function clauses for asserting on the input instead of complex expectation rules

## Example

1. Create the API implementation based on the adapter implementation. Include `@callbacks`, and the `impl()` function for call the API.
2. Create the module where you're using the API implementation.
3. In the `test_helper.exs` you can mock the API.

```elixir
Mox.defmock(MyApp.MockWeatherAPI, for: MyApp.WeatherAPI)
Application.put_env(:my_app, :weather, MyApp.MockWeatherAPI)
```

4. Use in the tests.

```elixir
  test "gets and formats temperature and humidity" do
    MyApp.MockWeatherAPI
    |> expect(:temp, fn {_lat, _long} -> {:ok, 30} end)
    |> expect(:humidity, fn {_lat, _long} -> {:ok, 60} end)

    assert MyApp.HumanizedWeather.display_temp({50.06, 19.94}) ==
             "Current temperature is 30 degrees"

    assert MyApp.HumanizedWeather.display_humidity({50.06, 19.94}) ==
             "Current humidity is 60%"
  end
```
