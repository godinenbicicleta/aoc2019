defmodule Day2 do
  def read do
    nums =
      File.read!("input.txt")
      |> String.trim()
      |> String.split(",")
      |> Enum.map(&String.to_integer/1)
      |> Enum.to_list()

    for i1 <- 0..99, i2 <- 0..99 do
      case attempt(nums, i1, i2) do
        [19_690_720 | _] ->
          IO.inspect(100 * i1 + i2)
          System.halt(0)

        _ ->
          nil
      end
    end
  end

  defp attempt(nums, i1, i2) do
    nums =
      List.replace_at(nums, 1, i1)
      |> List.replace_at(2, i2)

    process({:ok, nums, 0})
  end

  defp process({:ok, nums, index}) do
    [code, pos1, pos2, pos3] = Enum.slice(nums, index, 4)

    case code do
      1 -> {:ok, sum(pos1, pos2, pos3, nums), index + 4}
      2 -> {:ok, multiply(pos1, pos2, pos3, nums), index + 4}
      99 -> {:stop, nums}
    end
    |> process
  end

  defp process({:stop, nums}) do
    nums
  end

  defp sum(pos1, pos2, pos3, nums) do
    List.replace_at(nums, pos3, Enum.at(nums, pos1) + Enum.at(nums, pos2))
  end

  defp multiply(pos1, pos2, pos3, nums) do
    List.replace_at(nums, pos3, Enum.at(nums, pos1) * Enum.at(nums, pos2))
  end
end

Day2.read()
