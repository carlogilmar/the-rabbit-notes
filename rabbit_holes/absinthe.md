## Absthinte & GraphQL & Hammer

### Middleware

[Absinthe Middleware](https://hexdocs.pm/absinthe/middleware-and-plugins.html#create-a-middleware)

**Creating a Middleware**
1. Create a module to implement the `middleware` behaviour.
2. Inside this module you need to implement the `call/2` function to modify the `resolution` struct.
3. In this part you can handle errors inside this function and update the resolution params.

``` elixir
defmodule MyApp.Middlewares.HandleChangesetErrors do
  @behaviour Absinthe.Middleware
  def call(resolution, _) do
    %{resolution |
      errors: Enum.flat_map(resolution.errors, &handle_error/1)
    }
  end

  defp handle_error(%Ecto.Changeset{} = changeset) do
    changeset
      |> Ecto.Changeset.traverse_errors(fn {err, _opts} -> err end)
      |> Enum.map(fn({k,v}) -> "#{k}: #{v}" end)
  end
  defp handle_error(error), do: [error]
end
```

**Using Middlewares**

After wrote your middleware module:

- You can implement the middleware in the `fields`. 
- You can specify in which order you need to handle the middleware.
- You can implement many middlewares as you need.
- You can implement the middleware in the `schema` for a group of fields.





