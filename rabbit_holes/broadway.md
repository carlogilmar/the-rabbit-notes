# Broadway Elixir

> Build concurrent and multi-stage data ingestion and data processing pipelines with Elixir.

References:

- [Samuel Mullen Post](https://samuelmullen.com/articles/understanding-elixirs-broadway)

Notes about Broadway:

- Broadway is a sort of mini-framework for the GenStage library.
- Broadway grew out of a focus “on events and on operational features, such as metrics, automatic acknowledgements, failure handling, and so on.
- In both libraries, back-pressure allows “consumers” to signal producers their availability to receive data. Producers stop sending data to a consumer when it meets its capacity, and begins sending data again once the consumer has dealt with its backlog. 
- We only get the amount of events necessary from upstream sources, never flooding the pipeline.
- Broadway automatically acknowledges messages at the end of the pipeline or in case of errors.
- Broadway enables you to choose how best to handle the errors and the data that caused them.
- Broadway provides built-in batching, allowing you to group messages either by size and/or by time.
- Broadway pipelines are carefully designed to minimize data loss. 
- Broadway ships with a built-in test API, making it easy to push test messages through the pipeline and making sure the event was properly processed.
- Broadway allows developers to batch messages based on dynamic partitions.

## Example

- A broadway app has two components: producers and consumers. 
- Producers are GenStage modules which produces events.
- The Consumers processes the events generated by producers.
- Transformers are only needed if your producer doesn’t return a `%Broadway.Message{}`

How to implement:
* 1. Create a producer module using `GenStage`.
* 2. Implement a transformer module to create Broadway Messages from producers.
* 3. Implement Broadway configuration and setup
  * Handle the configuration in the `start_link`
  * The previous implementation starts a Broadway process linked to the current one.
  * `Name` option is used for name registration.
  * `Producers` is a key for define multiple producers. (We need to declare the producer module, the transformer module and number of processes to be started)
  * `Processors`: Single processor could be defined here.
  * `handle_message/3`: Here you can do any kind of processing with the incoming message.


1. Add the broadway dep: `{:broadway, "~> 1.0"}`.
2. Create the broadway module with the configuration to start.
3. Add the broadway module in your supervisor.
4. Create the producer module.
5. Create the transformer module.
6. Add the functions to handle the producer info.

<details>
  <summary>Producer</summary>

`Producer`
``` elixir
defmodule MyApp.Counter do
  use GenStage

  def start_link(number) do
    GenStage.start_link(Counter, number)
  end

  def init(counter) do
    {:producer, counter}
  end

  //We create the handle_demand/2 function to receive “demand” from processors
  def handle_demand(demand, counter) when demand > 0 do
    events = Enum.to_list(counter..counter+demand-1)

    {:noreply, events, counter + demand}
  end
end
```  
</details>

<details>
  <summary>Transformer</summary>

  `Transformer`
```elixir
defmodule MyApp.CounterMessage do
  def transform(event, _opts) do
    message = %Broadway.Message{
      data: event,
      acknowledger: {__MODULE__, :ack_id, event}
    }
  end

  def ack(_ref, _successes, _failures) do
    :ok
  end
end
```
</details>

<details>
  <summary>Configuration</summary>

  
`Configuration`
```elixir
defmodule MyApp do
  use Broadway

  alias Broadway.Message

  def start_link(_opts) do
    Broadway.start_link(__MODULE__,
      name: MyAppExample,
      producer: [
        default: [
          module: {MyApp.Counter, 0},
          transformer: {MyApp.CounterMessage, :transform, []},
          concurrency: 1 // rename stages to concurrency
        ]
      ],
      processors: [
        default: [stages: 2]
      ],
    )
  end

  def handle_message(:default, %Message{data: data} = message, _context) do
    Process.sleep 1000

    message
    |> IO.inspect
  end
end
```

</details>

<details>
  <summary>Broadway Message</summary>

`Configuration`
```elixir
  %Broadway.Message{
  acknowledger: {MyApp.CounterMessage, :ack_id, 0},
  batch_key: :default,
  batcher: :default,
  data: 0,
  metadata: %{},
  status: :ok
}
```
</details>